#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════════════════
# Legion Linux Toolkit — Installer  v0.6.3  (LLL backend)
# Installs the PyQt6 GUI + tray alongside LLL (LenovoLegionLinux) for hardware.
# ══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'
YELLOW='\033[1;33m'; BOLD='\033[1m'; NC='\033[0m'
ok()   { echo -e "  ${GREEN}✓${NC}  $*"; }
info() { echo -e "  ${CYAN}→${NC}  $*"; }
warn() { echo -e "  ${YELLOW}⚠${NC}  $*"; }
err()  { echo -e "  ${RED}✗${NC}  $*"; exit 1; }

[[ $EUID -ne 0 ]] && err "Run as root: sudo bash install.sh"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "\n${BOLD}╔══════════════════════════════════════════╗"
echo      "║   Legion Linux Toolkit — Installer       ║"
echo      "║              v0.6.3 (LLL)                ║"
echo -e   "╚══════════════════════════════════════════╝${NC}\n"

# ── 1. Core dependencies ──────────────────────────────────────────────────────
info "Installing core dependencies…"
MISSING=()
python3 -c "import PyQt6" 2>/dev/null      || MISSING+=("python-pyqt6")
command -v notify-send &>/dev/null         || MISSING+=("libnotify")
pacman -Q qt6-wayland &>/dev/null          || MISSING+=("qt6-wayland")
command -v git &>/dev/null                || MISSING+=("git")
[[ ${#MISSING[@]} -gt 0 ]] && pacman -S --noconfirm --needed "${MISSING[@]}"
ok "Core packages ready"

# ── 2. Install LLL (LenovoLegionLinux) ────────────────────────────────────────
info "Installing LenovoLegionLinux (LLL)…"
if ! pacman -Q lenovolegionlinux &>/dev/null; then
    pacman -S --noconfirm --needed lenovolegionlinux lenovolegionlinux-dkms 2>/dev/null \
        && ok "LLL installed from repos" \
        || warn "LLL not in your distro repos"
fi

if ! lsmod 2>/dev/null | grep -q "legion_laptop"; then
    modprobe legion_laptop 2>/dev/null || true
    sleep 1
fi

if dmesg 2>/dev/null | grep -q "probe with driver legion failed\|Could not init ACPI access"; then
    echo 'options legion_laptop force=1' > /etc/modprobe.d/legion_laptop_force.conf
    modprobe -r legion_laptop 2>/dev/null || true
    modprobe legion_laptop force=1 2>/dev/null && ok "Force-load applied" || warn "Force-load failed"
fi

# Install LLL Python package
if ! python3 -c "import legion_linux" 2>/dev/null; then
    info "Installing legion_linux Python package…"
    TMP_DIR=$(mktemp -d)
    cd "$TMP_DIR"
    git clone --depth=1 https://github.com/johnfanv2/LenovoLegionLinux.git
    cd LenovoLegionLinux/python
    pip install . 2>/dev/null && ok "legion_linux Python package installed" \
        || warn "legion_linux install failed"
    cd /
    rm -rf "$TMP_DIR"
fi

ok "LLL ready"

# ── 3. Install GUI + tray ─────────────────────────────────────────────────────
info "Installing Legion Linux Toolkit GUI…"
mkdir -p /usr/lib/legion-toolkit
install -m 755 "$SCRIPT_DIR/tray/legion-gui.py"  /usr/lib/legion-toolkit/legion-gui.py
install -m 755 "$SCRIPT_DIR/tray/legion-tray.py" /usr/lib/legion-toolkit/legion-tray.py
install -m 644 "$SCRIPT_DIR/tray/kernel_check.py" /usr/lib/legion-toolkit/kernel_check.py
install -m 755 -d /usr/lib/legion-toolkit/lib
cp -r "$SCRIPT_DIR/lib/lll_adapter.py" /usr/lib/legion-toolkit/lib/lll_adapter.py
install -m 644 "$SCRIPT_DIR/tray/org.legion-toolkit.policy" \
    /usr/share/polkit-1/actions/org.legion-toolkit.policy
install -m 755 "$SCRIPT_DIR/scripts/legion-helper.sh" \
    /usr/lib/legion-toolkit/legion-helper.sh
install -m 644 "$SCRIPT_DIR/polkit/49-legion-toolkit.rules" \
    /etc/polkit-1/rules.d/49-legion-toolkit.rules
ok "GUI and tray installed"

# ── 4. Install CLI ────────────────────────────────────────────────────────────
info "Installing CLI…"
install -m 755 "$SCRIPT_DIR/scripts/legion-ctl" /usr/local/bin/legion-ctl
ok "CLI → /usr/local/bin/legion-ctl (delegates to legion_cli)"

# ── 5. Autostart ──────────────────────────────────────────────────────────────
info "Configuring autostart…"
cat > /etc/xdg/autostart/legion-toolkit.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=Legion Linux Toolkit
Exec=/usr/lib/legion-toolkit/legion-tray.py
Icon=computer
Terminal=false
Categories=System;
X-GNOME-Autostart-enabled=true
EOF
ok "Autostart configured"

# ── 6. LLL daemon ─────────────────────────────────────────────────────────────
info "Setting up LLL legiond daemon…"
if command -v legiond &>/dev/null; then
    systemctl enable --now legiond.service 2>/dev/null && ok "legiond started" \
        || warn "legiond not available — install LLL first"
fi
ok "Service configured"

# ── 7. udev (keyboard RGB permissions) ────────────────────────────────────────
info "Installing udev rules…"
install -m 644 "$SCRIPT_DIR/udev/99-legion-toolkit.rules" /etc/udev/rules.d/
udevadm control --reload-rules && udevadm trigger
ok "udev rules installed"

# ── 8. Launch tray immediately ────────────────────────────────────────────────
info "Starting tray for current user…"
REAL_USER="${SUDO_USER:-$(logname 2>/dev/null || echo "")}"
if [[ -n "$REAL_USER" ]]; then
    pkill -f "legion-tray" 2>/dev/null || true
    sleep 0.5
    sudo -u "$REAL_USER" nohup python3 /usr/lib/legion-toolkit/legion-tray.py \
        > /dev/null 2>&1 &
    ok "Tray launched — no reboot needed"
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo -e "\n${GREEN}${BOLD}✓ Installation complete!${NC}"
echo -e "  ${CYAN}LLL${NC}     : ${GREEN}installed${NC}"
echo -e "  ${CYAN}Tray${NC}    : ${GREEN}running now${NC} (autostart on next login)"
echo -e "  ${CYAN}CLI${NC}     : legion-ctl (wraps legion_cli)"
echo -e "  ${CYAN}Daemon${NC}  : legiond (from LLL)"
echo -e "  ${CYAN}Logs${NC}    : journalctl -fu legiond.service"
echo ""

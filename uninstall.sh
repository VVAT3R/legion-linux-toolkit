#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════════════════
# Legion Linux Toolkit — Uninstaller (LLL backend)
# ══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'
NC='\033[0m'
ok()   { echo -e "  ${GREEN}✓${NC}  $*"; }
info() { echo -e "  ${CYAN}→${NC}  $*"; }
err()  { echo -e "  ${RED}✗${NC}  $*"; exit 1; }

[[ $EUID -ne 0 ]] && err "Run as root: sudo bash uninstall.sh"

echo -e "\n${CYAN}Uninstalling Legion Linux Toolkit (LLL backend)…${NC}\n"

# Stop and remove toolkit files
pkill -f "legion-tray" 2>/dev/null || true
pkill -f "legion-gui"  2>/dev/null || true

# Remove installed files
rm -rf /usr/lib/legion-toolkit
rm -f /usr/local/bin/legion-ctl
rm -f /etc/xdg/autostart/legion-toolkit.desktop
rm -f /etc/udev/rules.d/99-legion-toolkit.rules
rm -f /usr/share/polkit-1/actions/org.legion-toolkit.policy

udevadm control --reload-rules 2>/dev/null || true

# Note: LLL packages (lenovolegionlinux, legion_linux) are NOT removed
# as they may be used by other applications. Remove them manually:
#   sudo pacman -Rns lenovolegionlinux lenovolegionlinux-dkms
#   sudo pip uninstall legion_linux

echo ""
ok "Legion Linux Toolkit removed"
echo ""
info "LLL packages were NOT removed. To remove them:"
info "  sudo pacman -Rns lenovolegionlinux lenovolegionlinux-dkms (if installed via pacman)"
info "  sudo pip uninstall legion_linux"
echo ""

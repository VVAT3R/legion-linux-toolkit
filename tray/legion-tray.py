#!/usr/bin/env python3
"""
Legion Linux Toolkit — System Tray
Hardware: Lenovo Legion via LLL (LenovoLegionLinux)
Left-click   → open dashboard
Middle-click → cycle power profile
Right-click  → full menu
"""
import os, sys, subprocess, socket
from pathlib import Path

os.environ["QT_QPA_PLATFORM"]                 = "wayland"
os.environ["QT_WAYLAND_DISABLE_WINDOWDECORATION"] = "1"
os.environ.setdefault("WAYLAND_DISPLAY", "wayland-0")
if "XDG_RUNTIME_DIR" not in os.environ:
    os.environ["XDG_RUNTIME_DIR"] = f"/run/user/{os.getuid()}"

_LEGION_ICON_B64 = "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"

try:
    from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
    from PyQt6.QtGui import (QIcon, QPixmap, QColor, QPainter,
                              QBrush, QFont, QAction, QActionGroup)
    from PyQt6.QtCore import Qt, QTimer
except ImportError:
    sys.exit("PyQt6 not found — sudo pacman -S python-pyqt6")

# ── Use LLL backend ──────────────────────────────────────────────────────
_lib = Path(__file__).resolve().parent / "lib"
if not (_lib / "lll_adapter.py").exists():
    _lib = Path(__file__).resolve().parent.parent / "lib"
sys.path.insert(0, str(_lib))
import lll_adapter as lll

GUI_BIN = Path("/usr/lib/legion-toolkit/legion-gui.py")

_PROFILE_INFO = {
    "quiet":       {"label": "Quiet",       "icon": "🔵", "color": "#4a9eff", "letter": "Q", "desc": "15W · Silent"},
    "balanced":    {"label": "Balanced",    "icon": "⚪", "color": "#e0e0e0", "letter": "B", "desc": "35W · Everyday"},
    "performance": {"label": "Performance", "icon": "🔴", "color": "#ff4757", "letter": "P", "desc": "54W · Gaming"},
    "custom":      {"label": "Custom",      "icon": "🩷", "color": "#ff69b4", "letter": "C", "desc": "54W · Custom"},
}

def _get_profiles() -> list[str]:
    return ["quiet", "balanced", "performance", "custom"]

def _label(name: str) -> str:
    return _PROFILE_INFO.get(name, {}).get("label", name.title())

def _color(name: str) -> str:
    return _PROFILE_INFO.get(name, {}).get("color", "#888888")

def _make_legion_tray_icon(profile: str) -> QIcon:
    import base64 as _b64
    size = 64
    px = QPixmap(size, size)
    px.fill(Qt.GlobalColor.transparent)
    p = QPainter(px)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    logo_data = _b64.b64decode(_LEGION_ICON_B64)
    logo_pm = QPixmap()
    logo_pm.loadFromData(logo_data)
    logo_pm = logo_pm.scaled(size, size,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation)
    ox = (size - logo_pm.width()) // 2
    oy = (size - logo_pm.height()) // 2
    p.drawPixmap(ox, oy, logo_pm)
    color = QColor(_color(profile))
    p.setBrush(QBrush(color))
    p.setPen(Qt.PenStyle.NoPen)
    dot = 14
    p.drawEllipse(size - dot - 1, size - dot - 1, dot, dot)
    p.end()
    return QIcon(px)

class LegionTray:
    def __init__(self, app: QApplication):
        self.app      = app
        self._profiles = _get_profiles()
        self._profile  = lll.read_powermode()

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(_make_legion_tray_icon(self._profile))
        self.tray.activated.connect(self._on_click)

        self.menu = QMenu()
        self._build_menu()
        self.tray.setContextMenu(self.menu)
        self._update_tooltip()

        self._timer = QTimer()
        self._timer.timeout.connect(self._poll)
        self._timer.start(500)
        self.tray.show()

    def _build_menu(self):
        self.menu.clear()
        m = self.menu

        h = QAction("⚡  Legion Toolkit", m); h.setEnabled(False)
        m.addAction(h)

        pct = lll.get_battery_pct()
        ac  = lll.get_ac_connected()
        bat_icon = "🔌" if ac else "🔋"
        bat_str = f"{bat_icon}  Battery: {pct}%" if pct >= 0 else f"{bat_icon}  Battery"
        ba = QAction(bat_str, m); ba.setEnabled(False)
        m.addAction(ba)
        m.addSeparator()

        prof_title = QAction("  Power Mode", m); prof_title.setEnabled(False)
        m.addAction(prof_title)

        self._profile_group   = QActionGroup(m)
        self._profile_actions = {}
        self._profile_group.setExclusive(True)

        for p in self._profiles:
            info  = _PROFILE_INFO.get(p, {})
            icon  = info.get("icon", "")
            label = info.get("label", p.title())
            desc  = info.get("desc", "")
            a = QAction(f"  {icon}  {label}  —  {desc}", m)
            a.setCheckable(True)
            a.setChecked(p == self._profile)
            a.triggered.connect(lambda chk, prof=p: self._set_profile(prof))
            self._profile_group.addAction(a)
            m.addAction(a)
            self._profile_actions[p] = a

        m.addSeparator()

        bat_title = QAction("  Battery", m); bat_title.setEnabled(False)
        m.addAction(bat_title)

        cons = lll.get_conservation_mode()
        rapid = lll.get_rapid_charge()

        self._cons_action  = QAction(
            ("🔋  Conservation Mode  ●" if cons else "🔋  Conservation Mode  ○"), m)
        self._rapid_action = QAction(
            ("⚡  Rapid Charge  ●" if rapid else "🐢  Rapid Charge  ○"), m)
        self._cons_action.triggered.connect(self._toggle_conservation)
        self._rapid_action.triggered.connect(self._toggle_rapid)
        m.addAction(self._cons_action)
        m.addAction(self._rapid_action)
        self._usb_menu = QMenu("🔌  USB Charging")
        usb_mode = lll.get_usb_charging_mode()
        self._usb_actions = []
        for i, label in enumerate(lll.USB_CHARGING_LABELS):
            a = QAction(label, m)
            a.setCheckable(True)
            a.setChecked(i == usb_mode)
            a.triggered.connect(lambda checked, idx=i: self._set_usb_mode(idx))
            self._usb_actions.append(a)
            self._usb_menu.addAction(a)
        m.addAction(self._usb_menu.menuAction())
        m.addSeparator()

        disp_title = QAction("  Display", m); disp_title.setEnabled(False)
        m.addAction(disp_title)
        od_val    = lll.get_overdrive()
        self._od_action = QAction(
            ("🖥️   Display Overdrive  ●" if od_val else "🖥️   Display Overdrive  ○"), m)
        self._od_action.triggered.connect(self._toggle_overdrive)
        m.addAction(self._od_action)

        gsync_val = lll.get_gsync()
        self._gsync_action = QAction(
            ("🔄  G-Sync  ●" if gsync_val else "🔄  G-Sync  ○"), m)
        self._gsync_action.triggered.connect(self._toggle_gsync)
        m.addAction(self._gsync_action)
        m.addSeparator()

        sys_title = QAction("  System", m); sys_title.setEnabled(False)
        m.addAction(sys_title)
        fn  = lll.get_fn_lock()
        cam = lll.get_camera_power()
        wk  = lll.get_winkey()
        self._fn_action  = QAction(("⌨️   Fn Lock  ●" if fn else "⌨️   Fn Lock  ○"), m)
        self._cam_action = QAction(("📷  Camera  ●" if cam else "📷  Camera  ○"), m)
        self._winkey_action = QAction(("🪟  Super Key  ●" if wk else "🪟  Super Key  ○"), m)
        self._fn_action.triggered.connect(self._toggle_fn)
        self._cam_action.triggered.connect(self._toggle_cam)
        self._winkey_action.triggered.connect(self._toggle_winkey)
        m.addAction(self._fn_action)
        m.addAction(self._cam_action)
        m.addAction(self._winkey_action)
        m.addSeparator()

        fan_title = QAction("  Fan", m); fan_title.setEnabled(False)
        m.addAction(fan_title)
        fan_val = lll.get_fan_fullspeed()
        self._fan_action = QAction(
            ("🌀  Fan Full Speed  ●" if fan_val else "🌀  Fan Full Speed  ○"), m)
        self._fan_action.triggered.connect(self._toggle_fan)
        m.addAction(self._fan_action)
        m.addSeparator()

        boost = lll.get_cpu_boost()
        s = QAction(f"  CPU Boost: {'ON' if boost else 'OFF'}", m)
        s.setEnabled(False)
        m.addAction(s)
        m.addSeparator()

        dash = QAction("📊  Open Dashboard", m)
        dash.triggered.connect(self._open_dashboard)
        m.addAction(dash)
        m.addSeparator()

        quit_a = QAction("✕  Quit", m)
        quit_a.triggered.connect(self.app.quit)
        m.addAction(quit_a)

    def _update_tooltip(self):
        lbl = _label(self._profile)
        pct = lll.get_battery_pct()
        bat = f" · 🔋 {pct}%" if pct >= 0 else ""
        self.tray.setToolTip(f"Legion Toolkit — {lbl}{bat}")

    def _on_click(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self._open_dashboard()
        elif reason == QSystemTrayIcon.ActivationReason.MiddleClick:
            self._cycle()

    def _open_dashboard(self):
        try:
            subprocess.run(["pkill", "-f", "legion-gui.py"],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass
        import time as _t; _t.sleep(0.15)
        try:
            subprocess.Popen(
                ["python3", str(GUI_BIN)],
                stdout=open("/tmp/legion-gui.log","w"),
                stderr=open("/tmp/legion-gui.log","w")
            )
        except Exception as e:
            self.tray.showMessage("Legion Toolkit",
                                  f"Could not launch dashboard: {e}",
                                  QSystemTrayIcon.MessageIcon.Critical, 4000)

    def _cycle(self):
        profiles = self._profiles
        idx = profiles.index(self._profile) if self._profile in profiles else 0
        self._set_profile(profiles[(idx + 1) % len(profiles)])

    def _set_profile(self, name: str):
        lll.apply_profile(name)
        self._update_ui(name)
        info = _PROFILE_INFO.get(name, {})
        self.tray.showMessage(
            "Legion Toolkit",
            f"{info.get('icon','')} {info.get('label', name)}  —  {info.get('desc','')}",
            QSystemTrayIcon.MessageIcon.Information, 2000
        )

    def _tog(self, get_fn, set_fn, action, on_lbl, off_lbl,
             notif_on="", notif_off=""):
        cur = get_fn()
        new = not cur
        set_fn(new)
        action.setText(on_lbl if new else off_lbl)
        msg = notif_on if new else notif_off
        if msg:
            self.tray.showMessage("Legion Toolkit", msg,
                                  QSystemTrayIcon.MessageIcon.Information, 2000)

    def _toggle_conservation(self):
        self._tog(lll.get_conservation_mode, lll.set_conservation_mode,
                  self._cons_action,
                  "🔋  Conservation Mode  ●", "🔋  Conservation Mode  ○",
                  "Conservation ON — charging capped at ~60%",
                  "Conservation OFF — normal charging")

    def _toggle_rapid(self):
        self._tog(lll.get_rapid_charge, lll.set_rapid_charge,
                  self._rapid_action,
                  "⚡  Rapid Charge  ●", "🐢  Rapid Charge  ○",
                  "Rapid charge ON", "Rapid charge OFF")

    def _set_usb_mode(self, idx):
        lll.set_usb_charging_mode(idx)
        for i, a in enumerate(self._usb_actions):
            a.setChecked(i == idx)
        self._usb_menu.setTitle(f"🔌  {lll.USB_CHARGING_LABELS[idx]}")
        self._usb_menu.menuAction().setText(f"🔌  {lll.USB_CHARGING_LABELS[idx]}")

    def _toggle_overdrive(self):
        self._tog(lll.get_overdrive, lll.set_overdrive,
                  self._od_action,
                  "🖥️   Display Overdrive  ●", "🖥️   Display Overdrive  ○",
                  "Display overdrive ON", "Display overdrive OFF")

    def _toggle_gsync(self):
        self._tog(lll.get_gsync, lll.set_gsync,
                  self._gsync_action,
                  "🔄  G-Sync  ●", "🔄  G-Sync  ○",
                  "G-Sync ON", "G-Sync OFF")

    def _toggle_fn(self):
        self._tog(lll.get_fn_lock, lll.set_fn_lock,
                  self._fn_action,
                  "⌨️   Fn Lock  ●", "⌨️   Fn Lock  ○",
                  "Fn Lock ON", "Fn Lock OFF")

    def _toggle_cam(self):
        self._tog(lll.get_camera_power, lll.set_camera_power,
                  self._cam_action,
                  "📷  Camera  ●", "📷  Camera  ○",
                  "Camera ON", "Camera OFF")

    def _toggle_winkey(self):
        self._tog(lll.get_winkey, lll.set_winkey,
                  self._winkey_action,
                  "🪟  Super Key  ●", "🪟  Super Key  ○",
                  "Super key enabled", "Super key disabled")

    def _toggle_fan(self):
        self._tog(lll.get_fan_fullspeed, lll.set_fan_fullspeed,
                  self._fan_action,
                  "🌀  Fan Full Speed  ●", "🌀  Fan Full Speed  ○",
                  "Fan → full speed", "Fan → auto")

    def _update_ui(self, profile: str):
        self._profile = profile
        self.tray.setIcon(_make_legion_tray_icon(profile))
        self._update_tooltip()
        if profile in self._profile_actions:
            self._profile_actions[profile].setChecked(True)

    def _poll(self):
        current = lll.read_powermode()
        if current != self._profile:
            lll.set_cpu_boost(current in ("balanced", "performance"))
            self._update_ui(current)
            self._build_menu()
            self.tray.setContextMenu(self.menu)
        else:
            self._update_tooltip()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Legion Toolkit")
    app.setQuitOnLastWindowClosed(False)
    if not QSystemTrayIcon.isSystemTrayAvailable():
        sys.exit("No system tray available")
    LegionTray(app)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

# Legion Linux Toolkit

A PyQt6 GUI dashboard for Lenovo Legion laptops.  
Hardware backend: [LenovoLegionLinux (LLL)](https://github.com/johnfanv2/LenovoLegionLinux)  
KDE Plasma 6 · Wayland — works on any Arch-based distro.

![version](https://img.shields.io/badge/version-v0.6.3--LLL-red?style=flat-square)
![platform](https://img.shields.io/badge/platform-Linux-blue?style=flat-square)
![python](https://img.shields.io/badge/python-PyQt6-green?style=flat-square)
![backend](https://img.shields.io/badge/backend-LLL-blueviolet?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-white?style=flat-square)

All hardware control is delegated to LLL — power profiles, fan curves, battery conservation, overclocking, RGB, and more.

## Screenshots

| Page | Preview |
|------|---------|
| Home | ![](screenshots/Home.png) |
| Battery / Performance | ![](screenshots/Battery.png) ![](screenshots/Perf.png) |
| Display / Keyboard RGB | ![](screenshots/Display.png) ![](screenshots/Keyboard.png) |
| System / Fan | ![](screenshots/system.png) ![](screenshots/fan.png) |
| Overclock / Actions | ![](screenshots/OC.png) ![](screenshots/Action.png) |
| About | ![](screenshots/about.png) |

## Supported Hardware

| Brand | Models | Support |
|-------|--------|---------|
| Legion | 5, 5 Pro, 7, Slim 5/7 | Full — RGB, OC, fan, G-Sync (via LLL) |

Support is determined by LLL's `legion_laptop` kernel module. Only Legion/LOQ models with the module are fully supported.

## Features

- **Home** — Power mode (Quiet/Balanced/Performance/Custom), battery mode, GPU switching (envycontrol), G-Sync/Display Overdrive toggles, Fn Lock, live CPU/GPU/IC stats
- **Battery** — Live stats (%, voltage, health, cycles, power draw, temp), conservation/rapid charge modes, ThinkPad charge threshold
- **Display** — Brightness slider, resolution/refresh rate selectors (kscreen), Display Overdrive, G-Sync
- **Keyboard RGB** — 4-zone RGB via LegionAura (Static/Breath/Wave/Hue/Off), per-zone colour pickers, presets, backlight brightness
- **System** — Fn Lock, Super Key, Touchpad, Camera toggles, theme switcher, ThinkPad TrackPoint / ThinkLight / Yoga hinge mode
- **Fan** — Animated RPM icons, Auto/Full Speed modes, LLL driver status, custom fan curve when available, Kernel 7.x fallback, ThinkPad fan level
- **Overclock** — Master OC toggle, CPU frequency/TDP sliders (PL1/PL2), GPU core offset, memory offset, power limit, temp target

## Power Profiles

| Profile | LED | TDP |
|---------|-----|-----|
| `low-power` (Quiet) | Blue | 15W |
| `balanced` (Balanced) | White | 35W |
| `balanced-performance` (Performance) | Red | 45W |
| `performance` (Custom) | Pink | 54W |

## Languages

First-run language selector: English, Français, Deutsch, Español, Português, Türkçe, Русский, 中文, 日本語, 한국어, العربية

## Requirements

**Core:** `python-pyqt6 qt6-wayland libnotify kscreen git`

**Optional (auto-installed by brand):**

| Package | Brand | Feature |
|---------|-------|---------|
| `lenovolegionlinux` + `-dkms` | Legion/LOQ | Fan RPM, IC temp, custom curve |
| `envycontrol` | Legion/LOQ | GPU mode switching |
| `legionaura` | Legion | Keyboard RGB |
| `fprintd` | ThinkPad/Yoga | Fingerprint |
| `iio-sensor-proxy` | Yoga | Auto-rotate |

## Install

```bash
git clone https://github.com/VVAT3R/legion-linux-toolkit
cd legion-linux-toolkit
sudo bash install.sh
```

The installer installs PyQt6 + deps, LLL packages (from repos or AUR), the GUI + tray + CLI, autostart, and enables `legiond`.

## Update

```bash
sudo bash update.sh
```

## Uninstall

```bash
sudo bash uninstall.sh
```

## Architecture

All hardware control delegated to LLL:

| Component | LLL |
|-----------|-----|
| Daemon | `legiond` (C) |
| CLI | `legion-ctl` → `legion_cli` |
| Kernel module | `legion_laptop.ko` |
| Python library | `legion_linux.LegionModelFacade` |
| Fan curve | `FanCurveIO` |
| Power profiles | `PlatformProfileFeature` |
| Overclocking | `CPUOverclock`, `GPUOverclock` |

## License

MIT

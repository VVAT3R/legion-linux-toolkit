<div align="center">
  <img src="logo.png" width="80" alt="Legion Linux Toolkit"/>
  <h1>Legion Linux Toolkit</h1>
  <p><strong>A PyQt6 GUI dashboard for Lenovo Legion laptops</strong></p>
  <p>Hardware backend: <a href="https://github.com/johnfanv2/LenovoLegionLinux">LLL (LenovoLegionLinux)</a></p>
  <p>KDE Plasma 6 · Wayland — works on any Arch-based distro</p>

  <p>
    <img src="https://img.shields.io/badge/version-v0.6.3--LLL-red?style=flat-square"/>
    <img src="https://img.shields.io/badge/platform-Linux-blue?style=flat-square"/>
    <img src="https://img.shields.io/badge/python-PyQt6-green?style=flat-square"/>
    <img src="https://img.shields.io/badge/backend-LLL-blueviolet?style=flat-square"/>
    <img src="https://img.shields.io/badge/license-MIT-white?style=flat-square"/>
  </p>
</div>

> **LLL Backend:** This toolkit uses [LenovoLegionLinux (LLL)](https://github.com/johnfanv2/LenovoLegionLinux) for all hardware control — power profiles, fan curves, battery conservation, overclocking, and more. The Python `legion_linux` library replaces direct sysfs access. Uses LLL's `legiond` daemon instead of a custom one.

<p align="center">
  <a href="https://v4cachy.github.io/legion-linux-toolkit/">
  </a>
</p>

---

## 🌐 Website

Visit our website: **[https://v4cachy.github.io/legion-linux-toolkit/](https://v4cachy.github.io/legion-linux-toolkit/)**

Learn more about features, supported hardware, and installation instructions.

---

## 📸 Screenshots

<div align="center">

### 🏠 Home
![Home](screenshots/Home.png)

### 🔋 Battery &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚡ Performance
<p>
  <img src="screenshots/Battery.png" width="49%"/>
  <img src="screenshots/Perf.png" width="49%"/>
</p>

### 🖥️ Display &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⌨️ Keyboard RGB
<p>
  <img src="screenshots/Display.png" width="49%"/>
  <img src="screenshots/Keyboard.png" width="49%"/>
</p>

### ⚙️ System &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🌀 Fan
<p>
  <img src="screenshots/system.png" width="49%"/>
  <img src="screenshots/fan.png" width="49%"/>
</p>

### 🚀 Overclock &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🎯 Actions
<p>
  <img src="screenshots/OC.png" width="49%"/>
  <img src="screenshots/Action.png" width="49%"/>
</p>

### ℹ️ About
![About](screenshots/about.png)

</div>

---

## 🖥️ Supported Hardware

| Brand | Models | Support |
|-------|--------|---------|
| 🎮 **Legion** | Legion 5, 5 Pro, 7, Slim 5/7 | ✅ Full — RGB, OC, fan, G-Sync (via LLL) |

> Hardware support is determined by LLL (LenovoLegionLinux) kernel module. Only Legion/LOQ models with the `legion_laptop` kernel module are fully supported.

---

## ✨ Features

<details>
<summary><b>🏠 Home Page</b></summary>

- ⚡ Power Mode dropdown — Quiet / Balanced / Performance / Custom (also Fn+Q)
- 🔋 Battery Mode — Normal / Conservation (~60%) / Rapid Charge
- 🎮 GPU Working Mode — Hybrid / NVIDIA / Integrated (via envycontrol)
- 🔄 G-Sync & Display Overdrive toggles
- 🔌 Always on USB & Fn Lock toggles
- 📊 Live CPU, GPU & IC stats — utilization, clock, temp, fan RPM, VRAM
- 🌡️ **IC Temperature** — Integrated Controller temp (when LLL loaded)

</details>

<details>
<summary><b>🔋 Battery Page</b></summary>

- 📈 Live battery %, voltage, health, charge cycles, power draw, temperature
- ⚙️ Conservation (~60%), Rapid Charge, USB Charging, Power Charge Mode
- 🔧 **ThinkPad only** — Start/Stop charge threshold (e.g. 40%–80%)

</details>

<details>
<summary><b>🖥️ Display Page</b></summary>

- ☀️ Screen brightness slider — auto-detects `nvidia_wmi_ec_backlight`, `amdgpu_bl0` etc.
- 📐 Resolution & Refresh Rate selectors (independent, via kscreen)
- ✨ Display Overdrive & G-Sync toggles

</details>

<details>
<summary><b>⌨️ Keyboard RGB (Legion)</b></summary>

- 🌈 4-zone RGB via LegionAura — Static, Breath, Wave, Hue, Off
- 🎨 Per-zone colour pickers + hex input
- 💡 Quick presets — Legion Red, Ocean, Sunset, Aurora
- 🔆 Keyboard backlight brightness slider

</details>

<details>
<summary><b>⚙️ System Page</b></summary>

- 🔒 Fn Lock, Super Key, Touchpad, Camera toggles
- 🎨 Theme — Dark / Dark Dimmed / OLED Black / Light
- 🔴 **ThinkPad only** — TrackPoint sensitivity & speed sliders
- 💡 **ThinkPad only** — ThinkLight & Mic Mute LED toggles
- 🔄 **Yoga only** — Hinge mode display, orientation lock toggle

</details>

<details>
<summary><b>🌀 Fan Page</b></summary>

- 🎡 Animated fan icons — real-time spin driven by actual RPM
- 🌡️ Auto mode — firmware thermal curves
- 💨 Full Speed mode — locks both fans to 100%
- 📊 **LLL status** — shows if LenovoLegionLinux driver is loaded
- ⚡ **Fan curve info** — displays custom curve availability (when LLL loaded)
- 🔌 **Kernel 7.x handling** — graceful fallback on newer kernels
- 🌀 **ThinkPad only** — Fan level dropdown (0–7, Auto, Disengaged)

</details>

<details>
<summary><b>🚀 Overclock Page</b></summary>

- 🔛 Master OC enable/disable toggle
- 🔧 CPU max/min frequency + TDP (PL1/PL2) sliders
- 🎮 GPU core offset, memory offset, power limit, temp target

</details>

---

## 🌍 Languages

First-run wizard — choose your language on first launch:

🇬🇧 English · 🇫🇷 Français · 🇩🇪 Deutsch · 🇪🇸 Español · 🇵🇹 Português · 🇹🇷 Türkçe · 🇷🇺 Русский · 🇨🇳 中文 · 🇯🇵 日本語 · 🇰🇷 한국어 · 🇸🇦 العربية

---

## 🎨 Power Profiles

| Profile | Label | LED | TDP |
|---------|-------|-----|-----|
| `low-power` | Quiet | 🔵 Blue | 15W |
| `balanced` | Balanced | ⚪ White | 35W |
| `balanced-performance` | Performance | 🔴 Red | 45W |
| `performance` | Custom | 🩷 Pink | 54W |

---

## 📦 Requirements

**Core — auto-installed:**
```
python-pyqt6   qt6-wayland   libnotify   kscreen   git
```

**Optional — auto-installed by brand:**

| Package | Manager | Brand | Feature |
|---------|---------|-------|---------|
| `lenovolegionlinux` + `lenovolegionlinux-dkms` | `pacman` | Legion / LOQ | Fan RPM, IC temp, custom fan curve |
| `envycontrol` | `paru` | Legion / LOQ | GPU mode switching |
| `legionaura` | `yay` | Legion | Keyboard RGB |
| `fprintd` | `pacman` | ThinkPad / Yoga | Fingerprint |
| `iio-sensor-proxy` | `pacman` | Yoga | Auto-rotate |

> ⚠️ **Kernel Compatibility:** The toolkit automatically detects if LLL works on your kernel.
> If not supported, it shows a message in the Fan page — auto-updates when LLL adds support.

---

## 🚀 Install

### Prerequisites
- Arch-based distro (Arch, CachyOS, EndeavourOS, Manjaro)
- LLL kernel module: `lenovolegionlinux` + `lenovolegionlinux-dkms` from AUR/repos

### Quick Install
```bash
git clone https://github.com/v4cachy/legion-linux-toolkit
cd legion-linux-toolkit
sudo bash install.sh
```

The installer will:
1. Install PyQt6 and other dependencies
2. Install LLL (LenovoLegionLinux) packages from repos or AUR
3. Install the GUI, tray app, and CLI wrapper
4. Set up autostart for the tray
5. Enable LLL's `legiond` daemon

---

## 🔄 Update

```bash
sudo bash update.sh
```

Pulls latest toolkit code, reinstalls files.

---

## 🗑️ Uninstall

```bash
sudo bash uninstall.sh
```

---

## 🛠️ Architecture

This is the **LLL backend version** of Legion Linux Toolkit. All hardware control is delegated to [LenovoLegionLinux](https://github.com/johnfanv2/LenovoLegionLinux):

| Component | LLT Custom (removed) | LLL (used now) |
|-----------|---------------------|----------------|
| **Daemon** | `legion-daemon.py` (Python) | `legiond` (C) |
| **CLI** | `legion-ctl` → daemon | `legion-ctl` → `legion_cli` |
| **Kernel module** | Direct sysfs reads | `legion_laptop.ko` |
| **Python library** | Direct sysfs writes | `legion_linux.LegionModelFacade` |
| **Fan curve** | Debugfs via pkexec | `FanCurveIO` |
| **Power profiles** | Custom daemon | `PlatformProfileFeature` |
| **Overclocking** | Direct sysfs | `CPUOverclock`, `GPUOverclock`, etc. |

---

## 📄 License

MIT — free to use, modify and distribute.

---

<div align="center">
  <sub>· PyQt6 GUI + LLL backend ·

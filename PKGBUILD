# Maintainer: Your Name <your@email.com>
# Contributor: VVAT3R
# 
# Legion Linux Toolkit — PyQt6 GUI/tray for Lenovo Legion laptops.
# Requires LenovoLegionLinux (LLL) for hardware access.
# Install LLL from AUR:
#   yay -S lenovolegionlinux-git lenovolegionlinux-dkms-git
# Or from chaotic-aur / cachyos repos.

pkgname=legion-linux-toolkit
pkgver=0.7.0
pkgrel=1
pkgdesc="PyQt6 GUI and system tray for Lenovo Legion laptops (LLL backend)"
arch=('any')
url="https://github.com/VVAT3R/legion-linux-toolkit"
license=('GPL3')
depends=(
    'python-pyqt6'
    'python'
    'libnotify'
    'qt6-wayland'
)
optdepends=(
    'lenovolegionlinux-git: LLL kernel module + Python library (AUR)'
    'lenovolegionlinux-dkms-git: LLL DKMS kernel module (AUR)'
)
makedepends=('git')
install=legion-linux-toolkit.install
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/VVAT3R/legion-linux-toolkit/archive/v${pkgver}.tar.gz")
sha256sums=('SKIP')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    # Core library
    install -dm755 "${pkgdir}/usr/lib/legion-toolkit/lib"
    install -m755 lib/lll_adapter.py "${pkgdir}/usr/lib/legion-toolkit/lib/"

    # GUI + Tray
    install -m755 tray/legion-gui.py  "${pkgdir}/usr/lib/legion-toolkit/"
    install -m755 tray/legion-tray.py "${pkgdir}/usr/lib/legion-toolkit/"
    install -m644 tray/kernel_check.py "${pkgdir}/usr/lib/legion-toolkit/"

    # Scripts
    install -m755 scripts/legion-helper.sh "${pkgdir}/usr/lib/legion-toolkit/"
    install -dm755 "${pkgdir}/usr/local/bin"
    install -m755 scripts/legion-ctl "${pkgdir}/usr/local/bin/"

    # Polkit rules (passwordless pkexec for helper)
    install -dm755 "${pkgdir}/etc/polkit-1/rules.d"
    install -m644 polkit/49-legion-toolkit.rules "${pkgdir}/etc/polkit-1/rules.d/"

    # Polkit action (legacy, kept for compatibility)
    install -dm755 "${pkgdir}/usr/share/polkit-1/actions"
    install -m644 tray/org.legion-toolkit.policy "${pkgdir}/usr/share/polkit-1/actions/"

    # udev rules (keyboard RGB permissions)
    install -dm755 "${pkgdir}/etc/udev/rules.d"
    install -m644 udev/99-legion-toolkit.rules "${pkgdir}/etc/udev/rules.d/"

    # Autostart
    install -dm755 "${pkgdir}/etc/xdg/autostart"
    install -m644 tray/legion-toolkit.desktop "${pkgdir}/etc/xdg/autostart/"
}

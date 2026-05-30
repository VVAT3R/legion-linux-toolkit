PREFIX ?= /usr
LIBDIR  = $(PREFIX)/lib/legion-toolkit
BINDIR  = $(PREFIX)/local/bin
POLKIT  = $(PREFIX)/share/polkit-1/rules.d
UDEV    = /etc/udev/rules.d
POLKIT_ACTIONS = $(PREFIX)/share/polkit-1/actions
AUTOSTART = /etc/xdg/autostart

.PHONY: install uninstall

install:
	install -d $(DESTDIR)$(LIBDIR)
	install -d $(DESTDIR)$(LIBDIR)/lib
	install -m755 tray/legion-gui.py  $(DESTDIR)$(LIBDIR)/
	install -m755 tray/legion-tray.py $(DESTDIR)$(LIBDIR)/
	install -m644 tray/kernel_check.py $(DESTDIR)$(LIBDIR)/
	install -m644 lib/lll_adapter.py   $(DESTDIR)$(LIBDIR)/lib/
	install -m755 scripts/legion-helper.sh $(DESTDIR)$(LIBDIR)/
	install -m755 scripts/legion-ctl  $(DESTDIR)$(BINDIR)/legion-ctl
	install -d $(DESTDIR)$(POLKIT)
	install -m644 polkit/49-legion-toolkit.rules $(DESTDIR)$(POLKIT)/
	install -m644 tray/org.legion-toolkit.policy $(DESTDIR)$(POLKIT_ACTIONS)/
	install -d $(DESTDIR)$(UDEV)
	install -m644 udev/99-legion-toolkit.rules $(DESTDIR)$(UDEV)/
	install -d $(DESTDIR)$(AUTOSTART)
	install -m644 tray/legion-toolkit.desktop $(DESTDIR)$(AUTOSTART)/
	udevadm control --reload-rules 2>/dev/null || true

uninstall:
	rm -rf $(DESTDIR)$(LIBDIR)
	rm -f $(DESTDIR)$(BINDIR)/legion-ctl
	rm -f $(DESTDIR)$(POLKIT)/49-legion-toolkit.rules
	rm -f $(DESTDIR)$(POLKIT_ACTIONS)/org.legion-toolkit.policy
	rm -f $(DESTDIR)$(UDEV)/99-legion-toolkit.rules
	rm -f $(DESTDIR)$(AUTOSTART)/legion-toolkit.desktop
	udevadm control --reload-rules 2>/dev/null || true

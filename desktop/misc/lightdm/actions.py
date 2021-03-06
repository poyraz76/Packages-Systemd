#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
  #  shelltools.export("MOC5", "moc-qt5")

    autotools.configure("--prefix=/usr \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --sbindir=/usr/bin \
                         --libexecdir=/usr/libexec/ \
                         --disable-static \
                         --disable-tests \
			             --disable-liblightdm-qt5 \
                         --with-greeter-user='lightdm' \
                         --with-greeter-session='lightdm-gtk-greeter'")
    
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir ("/usr/lib/systemd/system/graphical.target.wants")
    pisitools.dosym ("/usr/lib/systemd/system/lightdm.service", "/usr/lib/systemd/system/displaymanager.service")
    pisitools.dosym ("/usr/lib/systemd/system/lightdm.service", "/usr/lib/systemd/system/graphical.target.wants/lightdm.service")


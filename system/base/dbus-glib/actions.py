#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
	autotools.configure ("--prefix=/usr \
            --sysconfdir=/etc \
            --localstatedir=/var \
            --libexecdir=/usr/lib/dbus-1.0 \
            --with-console-auth-dir=/run/console/\
            --with-systemdsystemunitdir=/usr/lib/systemd/system\
            --disable-static")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())

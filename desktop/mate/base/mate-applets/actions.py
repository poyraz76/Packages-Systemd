#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/ \
                         --enable-polkit \
                         --enable-ipv6 \
                         --with-gtk=2.0 \
                         --with-gtk=3.0 \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")


#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools

def setup():
	shelltools.system ("sed -i -e '/gets is a/d' grub-core/gnulib/stdio.in.h")
	cflags = get.CFLAGS().replace("-fstack-protector","") # Fix build issue.
	shelltools.export ("CFLAGS", cflags)
	autotools.configure ("--prefix=/usr\
						  --sysconfdir=/etc\
						  --disable-werror")
						
def build():
	autotools.make ()
	
def install():
	autotools.rawInstall ("DESTDIR=%s" % get.installDIR())
	

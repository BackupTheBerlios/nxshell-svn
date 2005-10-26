# /.../
# spec file for package nxshell (Version 1.3)
#
# Copyright (c) 2004 SUSE LINUX AG, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#

# neededforbuild x-devel-packages
# usedforbuild aaa_base acl attr bash bind9-utils bison bzip2 coreutils cpio cpp cvs cyrus-sasl db devs diffutils e2fsprogs file filesystem fillup findutils flex gawk gdbm-devel glibc glibc-devel glibc-locale gpm grep groff gzip info insserv kbd less libacl libattr libgcc libstdc++ libxcrypt m4 make man mktemp modutils ncurses ncurses-devel net-tools netcfg openldap2-client openssl pam pam-devel pam-modules patch permissions popt ps rcs readline sed sendmail shadow strace syslogd sysvinit tar texinfo timezone unzip util-linux vim zlib zlib-devel autoconf automake binutils cracklib gcc gdbm gettext libtool perl rpm

Name:         nxshell
Requires:     netcat NX bash perl
Summary:      NX Tool to start single application via NX protocol
Version:      1.3
Release:      2
Group:        System/X11/Utilities
License:      GPL
Source:       nxshell.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%description
nxshell make use of the NX proxy system to run a remote
X11 application over a slow line like Modem ISDN or DSL
connections.

Authors:
--------
    Marcus Sch�fer <ms@suse.de>

%prep
%setup -n nxshell

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make buildroot=$RPM_BUILD_ROOT install

%files
%dir /usr/share/nxshell
/usr/bin/nxshell
/usr/bin/nxshell-agent.sh
/usr/bin/nxshell-proxy.sh
/usr/share/nxshell/functions.sh
/usr/share/nxshell/testX
/usr/share/nxshell/xkbctrl
/usr/share/nxshell/Keyboard.map
/usr/share/nxshell/remote.tgz

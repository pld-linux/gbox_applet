%define name	@PACKAGE@
%define ver 	@VERSION@
%define RELEASE 1
%define rel 	%{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix  /usr

Summary: a mbox mail checker applet for gnome
Name: %name
Version: %ver
Release: %rel
Source: ftp://gbox-applet.sourceforge.net/pub/gbox-applet/gbox_applet-%{ver}.tar.gz
Copyright: GPL
Group: Applications/Internet
BuildRoot: /var/tmp/%{name}-buildroot
Prefix: %{_prefix}
#Docdir: %{prefix}/doc


%description
A Gnome applet which monitors several mailbox files of type mbox. Each
mailbox can be assigned to a priority between 0 and 2 and it can have
its own time interval for checking. For each priority there is a
different icon. As additional Information Gbox can count the mails in
the boxes and show the subject and/or the sender of each mail in the
applet's menu. A tooltip can shows a summary of the information in
three different kinds.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --localstatedir=/var/lib --sysconfdir=/etc
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/pixmaps/gbox_applet
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/applets/Network
mkdir -p $RPM_BUILD_ROOT%{_prefix}/etc/CORBA/servers
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README TODO 
%{_prefix}/bin/gbox_applet
%{_prefix}/share/pixmaps/gbox_applet/*
%{_prefix}/share/applets/Network/gbox_applet.desktop
/etc/CORBA/servers/gbox_applet.gnorba

%changelog
* Fri May 26 2000 Ian Campbell <ijc25@cam.ac.uk> 0.6.1-1
- it works better with non-root builds and such like
* Wed Feb 2 2000 Glenn Attwood <gattwood@home.com> 0.4.0-1
- first rpm
# end of file

Summary:	A mbox mail checker applet for gnome
Summary(pl):	Aplet GNOME sprawdzaj�cy skrzynk� pocztow�
Name:		gbox_applet
Version:	0.7.0
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://gbox-applet.sourceforge.net/pub/gbox-applet/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
A Gnome applet which monitors several mailbox files of type mbox. Each
mailbox can be assigned to a priority between 0 and 2 and it can have
its own time interval for checking. For each priority there is a
different icon. As additional Information Gbox can count the mails in
the boxes and show the subject and/or the sender of each mail in the
applet's menu. A tooltip can show a summary of the information in
three different kinds.

%description -l pl
To jest aplet GNOME kontroluj�cy skrzynki pocztowe typu mbox. Ka�da
skrzynka mo�e mie� przypisany priorytet od 0 do 2 i mie� w�asny okres
sprawdzania. Ka�dy priorytet ma inn� ikon�. Jako dodatkow� informacj�
Gbox mo�e podawa� liczb� list�w w skrzynce i pokazywa� temat lub
nadawc� ka�dego listu w menu apletu. Tooltip mo�e pokazywa�
zestawienie informacji na trzy r�ne sposoby.

%prep
%setup -q

%build
rm -f missing acinclude.m4
gettextize --copy --force
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gbox_applet
%{_datadir}/applets/Network/gbox_applet.desktop
%{_sysconfdir}/CORBA/servers/gbox_applet.gnorba
%{_pixmapsdir}/*

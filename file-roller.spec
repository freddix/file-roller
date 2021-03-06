Summary:	An archive manager for GNOME
Name:		file-roller
Version:	3.14.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/file-roller/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	8b2d75bdf50e27a5f63e6202ba270ce2
Patch0:		%{name}-libexecdir.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 3.14.0
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Suggests:	bzip2
Suggests:	gzip
Suggests:	p7zip
Suggests:	tar
Suggests:	unrar
Suggests:	unzip
Suggests:	xz
Suggests:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
File Roller is an archive manager for the GNOME environment. With File
Roller you can: create and modify archives; view the content of an
archive; view a file contained in the archive; extract files from the
archive. File Roller is only a front-end (a graphical interface) to
various archiving programs.

%package -n nautilus-extension-file-roller
Summary:	File Roller extension for Nautilus
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus

%description -n nautilus-extension-file-roller
File Roller extension for Nautilus.

%prep
%setup -q
%patch -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/GConf
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{_libexecdir}
%attr(755,root,root) %{_bindir}/file-roller
%attr(755,root,root) %{_libexecdir}/*.sh
%attr(755,root,root) %{_libexecdir}/rpm2cpio
%{_datadir}/dbus-1/services/org.gnome.FileRoller.ArchiveManager1.service
%{_datadir}/dbus-1/services/org.gnome.FileRoller.service
%{_datadir}/file-roller
%{_datadir}/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/file-roller.*

%files -n nautilus-extension-file-roller
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/*.so


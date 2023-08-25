#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static libraries
#
Summary:	Gedit Technology - Source code editing widget
Summary(pl.UTF-8):	Widżet projektu Gedit Technology do edycji kodu źródłowego
Name:		libgedit-gtksourceview
Version:	299.0.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://gedit-technology.net/tarballs/libgedit-gtksourceview/%{name}-%{version}.tar.xz
# Source0-md5:	3f96094715a897567e3df7f72ec6c9f0
URL:		https://gedit-technology.net/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.74
BuildRequires:	gtk+3-devel >= 3.20
%{?with_apidocs:BuildRequires:	gtk-doc}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.74
Requires:	gtk+3 >= 3.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgedit-gtksourceview is part of Gedit Technology
<https://gedit-technology.net/>. It is a library that extends
GtkTextView, the standard GTK widget for multiline text editing. This
library adds support for syntax highlighting, undo/redo, file loading
and saving, search and replace, a completion system, printing,
displaying line numbers, and other features typical of a source code
editor.

%description -l pl.UTF-8
libgedit-gtksourceview to część projektu Gedit Technology
<https://gedit-technology.net/>. Jest to biblioteka rozszerzająca
GtkTextView - standardowy widżet GTK do edycji tekstu wieloliniowego.
Biblioteka dodaje obsługę podświetlania składni, cofania/przywracania,
wczytywania i zapisu plików, wyszukiwania i podmiany, dopełniania
nazw, drukowania, wyświetlania numerów linii i innych funkcji typowych
dla edytora kodu źródłowego.

%package devel
Summary:	Header files for libgedit-gtksourceview library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgedit-gtksourceview
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.74
Requires:	gtk+3-devel >= 3.20
Requires:	libxml2-devel >= 2.0

%description devel
Header files for libgedit-gtksourceview library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgedit-gtksourceview.

%package static
Summary:	Static libgedit-gtksourceview library
Summary(pl.UTF-8):	Statyczna biblioteka libgedit-gtksourceview
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgedit-gtksourceview library.

%description static -l pl.UTF-8
Statyczna biblioteka libgedit-gtksourceview.

%package apidocs
Summary:	API documentation for libgedit-gtksourceview library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgedit-gtksourceview
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libgedit-gtksourceview library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgedit-gtksourceview.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	%{!?with_apidocs:-Dgtk_doc=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}-300

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-300.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libgedit-gtksourceview-300.so.0
%{_libdir}/girepository-1.0/GtkSource-300.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgedit-gtksourceview-300.so
%{_includedir}/libgedit-gtksourceview-300
%{_datadir}/gir-1.0/GtkSource-300.gir
%{_datadir}/libgedit-gtksourceview-300
%{_pkgconfigdir}/libgedit-gtksourceview-300.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgedit-gtksourceview-300.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgedit-gtksourceview-300
%endif

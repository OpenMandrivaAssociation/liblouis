%define major 2
%define libname %mklibname louis %{major}
%define devname %mklibname -d louis

Summary:	Braille Translator and Back-Translator
Name:		liblouis
Version:	3.35.0
Release:	1
License:	LGPLv3+
Group:		System/Libraries
Url:		https://code.google.com/p/liblouis/
Source0:	https://github.com/liblouis/liblouis/releases/download/v%{version}/liblouis-%{version}.tar.gz

# for the man pages
BuildRequires:	help2man
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(yaml-0.1)


%description
Liblouis is an open-source braille translator and back-translator.
It features support for computer and literary braille, supports
contracted and uncontracted translation for many, many languages
and has support for hyphenation. New languages can easily be added
through tables that support a rule- or dictionary based approach.

Liblouis also supports math braille (Nemeth and Marburg). The
formatting of braille is provided by the companion project
liblouisxml.

Liblouis is based on the translation routines in the BRLTTY
screenreader for Linux. It has, however, gone far beyond these
routines. It is named in honor of Louis Braille.

%package -n louis-tools
Summary:	Braille Translator and Back-Translator - Tools
License:	GPLv3+
Group:		System/Libraries

%description -n louis-tools
Liblouis is an open-source braille translator and back-translator.
It features support for computer and literary braille, supports
contracted and uncontracted translation for many, many languages
and has support for hyphenation. New languages can easily be added
through tables that support a rule- or dictionary based approach.

%package data
Summary:	Braille Translator and Back-Translator - Tables
Group:		System/Libraries
BuildArch:	noarch

%description data
This package contains the tables for %{name}.

%package -n %{libname}
Summary:	Braille Translator and Back-Translator - Shared Library
Group:		System/Libraries
Requires:	%{name}-data = %{version}-%{release}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Braille Translator and Back-Translator - Development Files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%package -n python-louis
Summary:	Braille Translator and Back-Translator - Python3 Bindings
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
%rename		python3-louis

%description -n python-louis
This package contains the python bindings for %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static --enable-ucs4
%make_build

# build python binding
pushd python
%py_build
popd

%install
%make_install
# doc is only auto-installed when makeinfo is present
%make_install -C doc
find %{buildroot} -type f -name "*.la" -delete -print
# install python binding
pushd python
%py_install
popd

%files -n louis-tools
%doc COPYING
%{_bindir}/lou_*
%{_infodir}/%{name}.info.*
%{_mandir}/man1/lou_*

%files data
%{_datadir}/liblouis/

%files -n %{libname}
%{_libdir}/liblouis.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/liblouis

%files -n python-louis
%{python3_sitelib}/louis*.egg-info
%{python3_sitelib}/louis


Name:       libexiv2

Summary:    C++ library for metadata handling for image files
Version:    0.2.4
Release:    1
Group:      System/Libraries
License:    GPLv2
Url:        http://www.exiv2.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: expat-devel
BuildRequires: zlib-devel

%description
C++ library for metadata handling for image files.

%package devel
Summary:   Development headers
Requires:  %{name} = %{version}

%description devel
Development headers.

%package -n exiv2-tools
Summary:   Exiv2 binary

%description -n exiv2-tools
Exiv2 binary for image metadata manipulation.


%prep
%setup -q -n %{name}-%{version}/exiv2

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang exiv2

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libexiv2.so.*

%files devel
%defattr(-,root,root,-)
/usr/include/exiv2/*
%{_libdir}/libexiv2.so
%{_libdir}/pkgconfig/exiv2.pc
%exclude %{_libdir}/libexiv2.la
%exclude %{_libdir}/libexiv2.a

%files -n exiv2-tools -f exiv2.lang
%defattr(-,root,root,-)
%{_bindir}/exiv2
%{_datadir}/man/man1/*

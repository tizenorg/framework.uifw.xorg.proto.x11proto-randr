
Name:       xorg-x11-proto-randrproto
Summary:    X.Org X11 Protocol randrproto
Version:    1.3.2
Release:    1
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/randrproto-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-randrproto.manifest 
Provides:   randrproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-shared

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}




%files
%manifest xorg-x11-proto-randrproto.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/randrproto.pc
%{_includedir}/X11/extensions/randrproto.h
%{_includedir}/X11/extensions/randr.h
%doc %{_datadir}/doc/randrproto



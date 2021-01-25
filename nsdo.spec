Name:		nsdo
Version:	2.0
Release:	1%{?dist}
Summary:	Helper for running a command inside a given Linux network namespace
License:	GPLv3
URL:		https://github.com/ausbin/nsdo
Source0:    https://github.com/ausbin/nsdo/archive/master.tar.gz

#ExclusiveArch:	x86_64
BuildRequires:	binutils, gcc, make

#Depends: gconf2, gconf-service, libnotify4, libappindicator1, libxtst6, libnss3, libasound2, libxss1
#Requires:   GConf2, libnotify, libappindicator, libXtst, nss

%description
Helper for running a command inside a given Linux network namespace

%prep
pwd
rm -rf nsdo* etc*
tar xf %{S:0}

# increase compatibility with epel-7
sed -i 's/gzip --best -f -k $</gzip --best -f -c $(MANPAGE) > $(MANPAGEGZ)/' %{_builddir}/%{name}-master/Makefile

%build
cd %{_builddir}/%{name}-master
make

%install
cd %{_builddir}/%{name}-master
PREFIX=%{_prefix} DESTDIR=%{buildroot} make install
PREFIX=%{_prefix} DESTDIR=%{buildroot} make install-anyconnect
PREFIX=%{_prefix} DESTDIR=%{buildroot} make install-openvpn


%post
%postun

%files
%defattr(-,root,root)
# /usr
%{_bindir}/*
%{_exec_prefix}/lib/systemd/system/*
%{_datadir}/*
%{_sysconfdir}/bash_completion.d/nsdo


%changelog
* Mon Jan 25 2021 Guilherme Cardoso <gjc@ua.pt> 2.0-1
- Clean up RPM spec because of upstream fixes
- Rely on upstream Makefile

* Thu May 10 2018 Guilherme Cardoso <gjc@ua.pt> 1.0-2
- RPM spec cleanup

* Mon Feb 19 2018 Guilherme Cardoso <gjc@ua.pt> 1.0-1
- Initial packaging


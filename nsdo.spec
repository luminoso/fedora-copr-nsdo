Name:		nsdo
Version:	1.0
Release:	2%{?dist}
Summary:	Helper for running a command inside a given Linux network namespace
License:	GPLv3
URL:		https://github.com/ausbin/nsdo
Source0:    https://github.com/ausbin/nsdo/archive/master.tar.gz
Source1:    https://github.com/ausbin/nsdo/archive/feature/etc-netns.tar.gz
Source2:    https://github.com/ausbin/nsdo/archive/feature/etc-netns-overlay.tar.gz

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
tar xf %{S:1}
tar xf %{S:2}

# increase compatibility with epel-7-ppc64le
sed -i "s/gzip --best -f -k/gzip --best -f/" %{_builddir}/%{name}-master/Makefile
sed -i "s/gzip --best -f -k/gzip --best -f/" %{_builddir}/%{name}-feature-etc-netns/Makefile
sed -i "s/gzip --best -f -k/gzip --best -f/" %{_builddir}/%{name}-feature-etc-netns-overlay/Makefile


%build
cd %{_builddir}/%{name}-master
make

cd %{_builddir}/%{name}-feature-etc-netns
make

cd %{_builddir}/%{name}-feature-etc-netns-overlay
make


%install

# Original install
#install -Dm4755 $< $(DESTDIR)$(PREFIX)/bin/$<
#install -Dm644 $(word 2,$^) $(DESTDIR)$(PREFIX)/share/man/man$(MANSECTION)/$(word 2,$^)
#install -Dm644 bash_completion/$(PROG) $(DESTDIR)$(BASH_COMPLETION_DIR)/$(PROG)

# copy each version
install -Dm4755 %{_builddir}/%{name}-master/nsdo %{buildroot}%{_bindir}/nsdo
install -Dm4755 %{_builddir}/%{name}-feature-etc-netns/nsdo %{buildroot}%{_bindir}/nsdo-etc-netns
install -Dm4755 %{_builddir}/%{name}-feature-etc-netns-overlay/nsdo %{buildroot}%{_bindir}/nsdo-etc-netns-overlay

# install manpage and bash bash completion
install -Dm644 %{_builddir}/%{name}-master/nsdo.1.gz  %{buildroot}%{_datadir}/man/man1/nsdo.1.gz
install -Dm644 %{_builddir}/%{name}-master/bash_completion/nsdo %{buildroot}%{_sysconfdir}/bash_completion.d/nsdo

# copy examples and auxiliary files
install -Dm644 %{_builddir}/%{name}-master/README.md %{buildroot}%{_datadir}/%{name}/README.md
install -Dm644 %{_builddir}/%{name}-master/LICENSE %{buildroot}%{_datadir}/%{name}/LICENSE
install -Dm644 %{_builddir}/%{name}-master/openvpn-example.md %{buildroot}%{_datadir}/%{name}/openvpn-example.md
install -Dm644 %{_builddir}/%{name}-feature-etc-netns-overlay/netns.sh %{buildroot}%{_datadir}/%{name}/netns.sh


%post
%postun

%files
%defattr(-,root,root)
%{_datadir}/*
%{_bindir}/nsdo
%{_bindir}/nsdo-etc-netns
%{_bindir}/nsdo-etc-netns-overlay
%{_sysconfdir}/bash_completion.d/nsdo


%changelog
* Thu May 10 2018 Guilherme Cardoso <gjc@ua.pt> 1.0-2
  - RPM spec cleanup

* Mon Feb 19 2018 Guilherme Cardoso <gjc@ua.pt> 1.0-1
  - Initial packaging


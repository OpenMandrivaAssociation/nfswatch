Summary:	An NFS traffic monitoring tool
Name:		nfswatch
Version:	4.99.13
Release:	1
License:	BSD
Group:		Monitoring
URL:		https://nfswatch.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	nfswatch.init
Source2:	nfswatch.sysconfig
Source3:	nfswatch.logrotate
BuildRequires:	ncurses-devel
BuildRequires:	pcap-devel
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Nfswatch is a command-line tool for monitoring NFS traffic. Nfswatch can
capture and analyze the NFS packets on a particular network interface or on all
interfaces.

Install nfswatch if you need a program to monitor NFS traffic.

%prep

%setup -q
mkdir -p Mandriva
cp %{SOURCE1} Mandriva/nfswatch.init
cp %{SOURCE2} Mandriva/nfswatch.sysconfig
cp %{SOURCE3} Mandriva/nfswatch.logrotate

%build
%serverbuild

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_var}/log
install -d %{buildroot}%{_mandir}/man8

install -m0755 nfswatch %{buildroot}%{_sbindir}/
install -m0755 nfslogsum %{buildroot}%{_sbindir}/
install -m0644 nfswatch.8 %{buildroot}%{_mandir}/man8/nfswatch.8
install -m0644 nfslogsum.8 %{buildroot}%{_mandir}/man8/nfslogsum.8

install -m755 Mandriva/nfswatch.init %{buildroot}%{_initrddir}/nfswatch
install -m644 Mandriva/nfswatch.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/nfswatch
install -m644 Mandriva/nfswatch.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/nfswatch

touch %{buildroot}%{_var}/log/nfswatch.log

%post
%_post_service nfswatch
%create_ghostfile %{_var}/log/nfswatch.log root root 0644

%preun
%_preun_service nfswatch

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%{_initrddir}/nfswatch
%config(noreplace) %{_sysconfdir}/sysconfig/nfswatch
%config(noreplace) %{_sysconfdir}/logrotate.d/nfswatch
%{_sbindir}/nfswatch
%{_sbindir}/nfslogsum
%{_mandir}/man8/*
%ghost %{_var}/log/nfswatch.log


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 4.99.11-1mdv2011.0
+ Revision: 645331
- update to new version 4.99.11

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Sun Jun 21 2009 Jérôme Brenier <incubusss@mandriva.org> 4.99.10-1mdv2010.0
+ Revision: 387865
- add BR pcap-devel
- update to new version 4.99.10

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 4.99.9-5mdv2009.0
+ Revision: 253943
- rebuild

* Thu Feb 14 2008 Oden Eriksson <oeriksson@mandriva.com> 4.99.9-3mdv2008.1
+ Revision: 167703
- added LFS tags
- don't start it per default
- use the %%serverbuild macro

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 4.99.9-2mdv2008.0
+ Revision: 81479
- bump release
- 4.99.9


* Wed Mar 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.99.8-1mdv2007.1
+ Revision: 143637
- new version

  + Oden Eriksson <oeriksson@mandriva.com>
    - Import nfswatch

* Tue Feb 27 2007 Oden Eriksson <oeriksson@mandriva.com> 4.99.7-1mdv2007.1
- 4.99.7
- bunzip sources

* Mon Jun 19 2006 Emmanuel Andry <eandry@mandriva.org> 4.99.6-1mdv2007.0
- 4.99.6

* Fri Mar 03 2006 Oden Eriksson <oeriksson@mandriva.com> 4.99.5-2mdk
- use the %%mkrel macro
- fix post and preun deps syntax

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 4.99.5-1mdk
- 4.99.5 (Major feature enhancements)

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 4.99.4-1mdk
- 4.99.4 (Minor feature enhancements)

* Sun May 22 2005 Oden Eriksson <oeriksson@mandriva.com> 4.99.2-1mdk
- initial Mandriva package
- used parts of the provided spec file


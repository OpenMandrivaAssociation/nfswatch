Summary:	An NFS traffic monitoring tool
Name:		nfswatch
Version:	4.99.10
Release:	%mkrel 1
License:	BSD
Group:		Monitoring
URL:		http://nfswatch.sourceforge.net
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

%define name drakcluster
%define version 1.4
%define release %mkrel 8

Summary: Graphic interface tool to setup server cluster
Name: %{name}
Version: %{version}
Release: %{release}
#Source0: %{name}-%{version}.tar.bz2
Source0: %{name}-devel.tar.bz2
License: 	GPL
Group: 		System/Cluster
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Prefix: 	%{_prefix}
URL:		http://www.mandriva.com
buildarch:	noarch
requires:	perl-GTK2, clusterscripts-server => 1.9
# drakxtools2,

%description
Graphic interface to admin and setup the servr cluster.

%prep
rm -rf ${buildroot}
%setup -q -n %{name}-devel

%build
make build

%install
rm -rf $RPM_BUILD_ROOT
make installd DESTDIR=$RPM_BUILD_ROOT
%find_lang drakcluster

%clean
rm -fr %{buildroot}

%files -f drakcluster.lang
%defattr(-,root,root)
%{_datadir}/pixmaps/cluster/*
%{perl_vendorlib}/drakcluster/*
%{perl_vendorlib}/interface_cluster.pm
%attr(755,root,root) %{_sbindir}/drakcluster.pl
%attr(755,root,root) %{_sbindir}/draktab*
%attr(755,root,root) %{_bindir}/cluster_applet.pl
%attr(755,root,root) %{_sbindir}/drakka



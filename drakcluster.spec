Summary:	Graphic interface tool to setup server cluster
Name:		drakcluster
Version:	1.6
Release:	5
#Source0: %{name}-%{version}.tar.bz2
Source0:	%{name}-devel.tar.bz2
License:	GPL
Group:		System/Cluster
URL:		https://www.mandriva.com
BuildArch:	noarch
Requires:	perl-Gtk2
Requires:	clusterscripts-server
Requires:	xli
Requires:	xterm
Requires:	xpdf
Requires:	drakxtools

%description
Graphic interface to admin and setup the servr cluster.

%prep
%setup -q -n %{name}-devel

%build
make build

%install
make installd DESTDIR=%{buildroot}
%find_lang drakcluster

%files -f drakcluster.lang
%{_datadir}/pixmaps/cluster/*
%{perl_vendorlib}/drakcluster/*
%{perl_vendorlib}/interface_cluster.pm
%attr(755,root,root) %{_sbindir}/drakcluster.pl
%attr(755,root,root) %{_sbindir}/draktab*
%attr(755,root,root) %{_bindir}/cluster_applet.pl
%attr(755,root,root) %{_sbindir}/drakka


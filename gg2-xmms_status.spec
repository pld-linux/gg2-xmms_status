%define         _snap	20040330
Summary:	XMMS status - GNU Gadu 2 plugin
Summary(pl):	XMMS status - GNU Gadu 2 plugin
Name:		gg2-xmms_status
Version:	%{_snap}
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Communications
Source0:	http://fran86.w.interia.pl/xmms_status-%{version}.tar.gz
# Source0-md5:	eab5cfee91c46e36fb3d4d9fb55f7a45
URL:		http://fran86.w.interia.pl
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	glib2-devel  >= 2.2.0
BuildRequires:	gtk+2-devel  >= 2.2.0
BuildRequires:	gg2-devel
BuildRequires:	xmms-devel
Requires:	gg2
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Change GNU Gadu 2 status description to XMMS song title.

%description -l pl
Zmienia opis statusu GNU Gadu 2 na nazwê aktualnie odtwarzanego utworu
w XMMS.

%prep
%setup -q -c %{name}-%{version} -a0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gg2
cp -f libxmms_status_plugin.so $RPM_BUILD_ROOT%{_libdir}/gg2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gg2/libxmms_status_plugin.so

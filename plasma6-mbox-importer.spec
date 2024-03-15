#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	MBox Importer allows to migrate data from MBox
Name:		plasma6-mbox-importer
Version:	24.02.0
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/mbox-importer/-/archive/%{gitbranch}/mbox-importer-%{gitbranchd}.tar.bz2#/mbox-importer-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/mbox-importer-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6MailCommon)
BuildRequires:	cmake(KPim6MailImporterAkonadi)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)

%description
MBox Importer allows to migrate data from MBox.

%files -f mboximporter.lang
%{_datadir}/applications/org.kde.mboximporter.desktop
%{_bindir}/mboximporter

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n mbox-importer-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang mboximporter

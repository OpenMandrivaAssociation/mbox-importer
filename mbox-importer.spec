#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	MBox Importer allows to migrate data from MBox
Name:		mbox-importer
Version:	25.08.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
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

%rename plasma6-mbox-importer

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
MBox Importer allows to migrate data from MBox.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.mboximporter.desktop
%{_bindir}/mboximporter

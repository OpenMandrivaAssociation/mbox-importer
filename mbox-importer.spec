%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	MBox Importer allows to migrate data from MBox
Name:		mbox-importer
Version:	23.08.5
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5MailCommon)
BuildRequires:	cmake(KPim5MailImporterAkonadi)
BuildRequires:	cmake(KPim5PimCommonAkonadi)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
Provides:	mboximporter = %{EVRD}
Conflicts:	mboximporter < 3:17.04.0
Obsoletes:	mboximporter < 3:17.04.0

%description
MBox Importer allows to migrate data from MBox.

%files -f mboximporter.lang
%{_kde5_applicationsdir}/org.kde.mboximporter.desktop
%{_bindir}/mboximporter

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang mboximporter

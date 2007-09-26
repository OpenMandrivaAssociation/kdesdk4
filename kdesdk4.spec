%define revision 714320

%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname kdesdk4 %lib_major
%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif


Name: kdesdk4
Summary: K Desktop Environment - Software Development Kit
Version: 3.93.0
Release: %mkrel 0.%revision.1
Epoch: 1
License: GPL
URL: ftp://ftp.kde.org/pub/kde/stable/%version/src/
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%version.%revision.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%version.tar.bz2
%endif
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-%version-%release-root
Requires: cvs
BuildRequires: db4-devel 
BuildRequires: freetype2-devel
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires: kdepimlibs4-devel >= %version-%mini_release
BuildRequires: kdepim4-devel 
BuildRequires: kdebase4-workspace-devel
BuildRequires: bzip2-devel 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel 
BuildRequires: png-devel 
BuildRequires: zlib-devel
BuildRequires: flex
#BuildRequires: kdepim-devel
BuildRequires: binutils-devel
BuildRequires: subversion-devel
BuildRequires:	libxslt-devel
BuildRequires:	mesaglut-devel 
BuildRequires: libx11-devel 
BuildRequires:	libltdl-devel

%description
Software Development Kit for the K Desktop Environment.

%files
%defattr(-,root,root)
%_kde_bindir/*
%_kde_iconsdir/*/*/*/kuiviewer*
%_kde_iconsdir/*/*/*/kbugbuster*
%_kde_appsdir/katepart/syntax/*
%_kde_libdir/kde4/*
%_kde_datadir/applications/kde4/kbugbuster.desktop
%_kde_datadir/applications/kde4/kuiviewer.desktop
%dir %_kde_appsdir/kbugbuster
%_kde_appsdir/kbugbuster/*
%dir %_kde_appsdir/kapptemplate/
%_kde_appsdir/kapptemplate/*
%dir %_kde_appsdir/kuiviewer/
%_kde_appsdir/kuiviewer/*
%dir %_kde_appsdir/kuiviewerpart/
%_kde_appsdir/kuiviewerpart/*
%_kde_datadir/kde4/servicetypes/*
%_kde_appsdir/kmtrace/kde.excludes
%_kde_appsdir/kabc/*
%_kde_datadir/kde4/services/*
%_kde_datadir/applications/kde4/kapptemplate.desktop
%exclude %_kde_bindir/kcachegrind
%exclude %_kde_bindir/umbrello
%_kde_iconsdir/*/*/actions/svn_add.*
%_kde_iconsdir/*/*/actions/svn_branch.*
%_kde_iconsdir/*/*/actions/svn_merge.*
%_kde_iconsdir/*/*/actions/svn_remove.*
%_kde_iconsdir/*/*/actions/svn_status.*
%_kde_iconsdir/*/*/actions/svn_switch.*
%_kde_appsdir/konqueror/servicemenus/subversion.desktop
%_kde_appsdir/konqueror/servicemenus/subversion_toplevel.desktop
%_datadir/dbus-1/interfaces/org.kde.ksvnd.xml

%doc %_kde_docdir/HTML/en/kdesvn-build/*.docbook
%doc %_kde_docdir/HTML/en/kdesvn-build/index.cache.bz2

%doc %_kde_docdir/HTML/en/kbugbuster/*.bz2
%doc %_kde_docdir/HTML/en/kbugbuster/*.docbook

%doc %_kde_docdir/HTML/en/kapptemplate/*.bz2
%doc %_kde_docdir/HTML/en/kapptemplate/*.docbook
%doc %_kde_docdir/HTML/en/kapptemplate/*.png

%package strigi-analyzer
Summary: Strigi Analyzer
Group: Graphical desktop/KDE

%description strigi-analyzer
Strigi analyzer

%files strigi-analyzer
%defattr(-,root,root)
%_kde_libdir/strigi/strigi*

%package kate
Summary: Kate
Group: Graphical desktop/KDE
Requires: %lib_name-kate = %epoch:%version-%release
Provides: kate4
Obsoletes: kdebase4-kate <= 1:3.80.2
Provides: kdebase4-kate > 1:3.80.2
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kate
A fast and advanced text editor with nice plugins

%files kate
%defattr(-,root,root)
%_kde_datadir/applications/kde4/kate.desktop
%_kde_appsdir/kate/externaltools
%_kde_appsdir/kate/icons/*/*/actions/curfiledir.*
%_kde_appsdir/kate/icons/*/*/actions/modified.*
%_kde_appsdir/kate/icons/*/*/actions/modmod.*
%_kde_appsdir/kate/icons/*/*/actions/modonhd.*
%_kde_appsdir/kate/icons/*/*/actions/null.*
%_kde_appsdir/kate/kateui.rc
%_kde_appsdir/kate/pics/sessionchooser.png
%_kde_appsdir/kate/plugins/*
%_kde_appsdir/kate/tips
%_kde_appsdir/kate/default.katesession
%_kde_appsdir/kconf_update/kate-2.4.upd
%_kde_appsdir/kicker/menuext/katesessionmenu.desktop
%_kde_datadir/config/katerc
%_kde_datadir/config/katefiletemplates.knsrc
%doc %_kde_docdir/HTML/en/kate-plugins/*.png
%doc %_kde_docdir/HTML/en/kate-plugins/*.bz2
%doc %_kde_docdir/HTML/en/kate-plugins/*.docbook
%doc %_kde_docdir/HTML/en/kate/*.png
%doc %_kde_docdir/HTML/en/kate/*.bz2
%doc %_kde_docdir/HTML/en/kate/*.docbook

%package -n %lib_name-kate
Summary: Libraries for Kate
Group: Graphical desktop/KDE
%define kdebase_lib_name %mklibname kdebase4 6
Obsoletes: %kdebase_lib_name-kate <= 1:3.80.2
Provides: %kdebase_lib_name-kate > 1:3.80.2


%description -n %lib_name-kate
Libraries for kate program

%post -n %lib_name-kate -p /sbin/ldconfig
%postun -n %lib_name-kate -p /sbin/ldconfig

%files -n %lib_name-kate
%defattr(-,root,root)
%_kde_libdir/libkateinterfaces.so.*
%_kde_libdir/libkdeinit4_kate.so

%package -n %lib_name-kate-devel
Summary: Development file for Kate
Group: Development/KDE and Qt
Requires: %lib_name-kate = %epoch:%version-%release
%define kdebase_lib_name %mklibname kdebase4 6
Obsoletes: %kdebase_lib_name-kate-devel <= 1:3.80.2
Provides: %kdebase_lib_name-kate-devel > 1:3.80.2


%description -n %lib_name-kate-devel
Development file for kate program

%files -n %lib_name-kate-devel
%defattr(-,root,root)
%_kde_libdir/libkateinterfaces.so
%dir %_kde_includedir/kate
%_kde_includedir/kate/*
%_kde_includedir/kate_export.h

#---------------------------------------------------------------

%package -n %lib_name-devel
Summary: Header files for kdesdk
Group: Development/KDE and Qt
Requires: %lib_name = %epoch:%version-%release
Provides: kdesdk4-devel =  %epoch:%version-%release
Provides: %lib_name_orig-devel = %epoch:%version-%release


%description -n %lib_name-devel	
This package includes the header files you will need to compile
applications for kdesdk.

%files -n %lib_name-devel
%defattr(-,root,root,-)
%_kde_includedir/kprofilemethod.h
%_kde_includedir/ktrace.h
%_kde_libdir/libktrace.so
%_kde_libdir/libkstartperf.so

#---------------------------------------------------------------

%package -n %lib_name
Summary: Lib files for kdesdk
Group: Graphical desktop/KDE
Conflicts: %lib_name-kbabel <= 3.3.2-1mdk
 
%description -n %lib_name
Lib files for kdesdk

%post -n %lib_name -p /sbin/ldconfig
%postun -n %lib_name -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root,-)
%_kde_libdir/libktrace.so.*
%_kde_libdir/libkstartperf.so.*
#---------------------------------------------------------------

%package umbrello
Summary: UML Modeller
Group: Graphical desktop/KDE
Provides: umbrello4

%description umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files umbrello
%defattr(-,root,root,-)
%_kde_bindir/umbrello
%_kde_datadir/applications/kde4/umbrello.desktop
%dir %_kde_appsdir/umbrello/
%_kde_appsdir/umbrello/*
%_kde_iconsdir/*/*/*/umbrello*

%doc %_kde_docdir/HTML/en/umbrello/*.png
%doc %_kde_docdir/HTML/en/umbrello/*.bz2
%doc %_kde_docdir/HTML/en/umbrello/*.docbook

#---------------------------------------------------------------

%package cervisia
Summary: CVS client part
Group: Graphical desktop/KDE
Provides: cervisia4 = %epoch:%version-%release
Requires: %lib_name-cervisia = %epoch:%version-%release
Requires: cvs

%description cervisia
CVS client part.

%files cervisia
%defattr(-,root,root,-)
%_kde_datadir/applications/kde4/cervisia.desktop
%_kde_appsdir/cervisia/cervisia.notifyrc
%_kde_appsdir/cervisia/cervisiashellui.rc
%_kde_appsdir/cervisiapart/cervisiaui.rc
%_kde_appsdir/kconf_update/cervisia-change_repos_list.pl
%_kde_appsdir/kconf_update/cervisia-normalize_cvsroot.pl
%_kde_appsdir/kconf_update/cervisia.upd
%_kde_appsdir/kconf_update/change_colors.pl
%_kde_datadir/config.kcfg/cervisiapart.kcfg
%_kde_datadir/icons/*/*/actions/vcs_add.*
%_kde_datadir/icons/*/*/actions/vcs_commit.*
%_kde_datadir/icons/*/*/actions/vcs_diff.*
%_kde_datadir/icons/*/*/actions/vcs_remove.*
%_kde_datadir/icons/*/*/actions/vcs_status.*
%_kde_datadir/icons/*/*/actions/vcs_update.*
%_kde_datadir/icons/*/*/apps/cervisia.*
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsjob.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsloginjob.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsservice.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.repository.xml
%_kde_prefix/man/man1/cervisia.*

%doc %_kde_docdir/HTML/en/cervisia/*.bz2
%doc %_kde_docdir/HTML/en/cervisia/*.docbook
%doc %_kde_docdir/HTML/en/cervisia/*.png

#---------------------------------------------------------------

%package kompare
Summary: kompare is a KDE diff graphic tool
Group: Graphical desktop/KDE
Provides: kompare4 = %epoch:%version-%release

%description kompare
kompare is a KDE diff graphic tool

%files kompare
%defattr(-,root,root,-)
#---------------------------------------------------------------

%package kcachegrind
Summary: KCachegrind
Group: Graphical desktop/KDE
Provides: kcachegrind4 = %epoch:%version-%release
%ifarch %{ix86}
Requires: valgrind
%endif

%description kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by 
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%files kcachegrind
%defattr(-,root,root,-)
%_kde_bindir/kcachegrind
%_kde_iconsdir/*/*/*/kcachegrind*
%dir %_kde_appsdir/kcachegrind/
%_kde_appsdir/kcachegrind/*
%_kde_datadir/applications/kde4/kcachegrind.desktop
%doc %_kde_docdir/HTML/en/kcachegrind/*.bz2
%doc %_kde_docdir/HTML/en/kcachegrind/*.docbook

#---------------------------------------------------------------

%package -n %lib_name-cervisia
Summary: Library for CVS client part
Group: Graphical desktop/KDE
Provides: %lib_name_orig-cervisia = %epoch:%version-%release

%description -n %lib_name-cervisia
Library for CVS client part.

%post -n %lib_name-cervisia -p /sbin/ldconfig
%postun -n %lib_name-cervisia -p /sbin/ldconfig

%files -n %lib_name-cervisia
%defattr(-,root,root,-)
%_kde_libdir/libkdeinit4_cervisia.so
%_kde_libdir/libkdeinit4_cvsaskpass.so
%_kde_libdir/libkdeinit4_cvsservice.so

#---------------------------------------------------------------

%package -n %lib_name-cervisia-devel
Summary: Devel files for CVS client part
Group: Development/KDE and Qt
Requires: %lib_name-cervisia = %epoch:%version-%release
Provides: %{lib_name_orig}-cervisia-devel = %epoch:%version-%release
Provides: %{name}-cervisia-devel = %epoch:%version-%release

%description -n %lib_name-cervisia-devel
Devel files for CVS client part.

%files -n %lib_name-cervisia-devel
%defattr(-,root,root,-)

#---------------------------------------------------------------

%prep
%setup -q -n kdesdk-%version

%build
%cmake_kde4

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot



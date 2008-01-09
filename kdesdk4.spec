%define revision 752225

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
Version: 3.97.1
Epoch: 1
License: GPL
URL: ftp://ftp.kde.org/pub/kde/stable/%version/src/
%if %branch
Release: %mkrel 0.%revision.1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%version.%revision.tar.bz2
%else
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%version.tar.bz2
%endif
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-%version-%release-root
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
BuildRequires: binutils-devel
BuildRequires: subversion-devel
BuildRequires:	libxslt-devel
BuildRequires:	mesaglut-devel 
BuildRequires: libx11-devel 
BuildRequires:	libltdl-devel

%description
Software Development Kit for the K Desktop Environment.


#--------------------------------------------------------------------
%package core
Summary: Common files needed for kdesdk
Group: Graphical desktop/KDE
Conflicts: %name < %epoch:3.97.1-0.746591.1
Obsoletes: %{_lib}kdesdk41 <= %epoch:3.96.1-0.740308.1

%description core
Common files needed for kdesdk

%files core
%defattr(-,root,root)
%{_kde_bindir}/cvsaskpass
%{_kde_bindir}/cvsservice
%{_kde_bindir}/kio_svn_helper
%{_kde_bindir}/kstartperf
%{_kde_libdir}/kde4/kabcformat_kdeaccounts.so
%{_kde_appsdir}/kabc/formats/kdeaccountsplugin.desktop

#---------------------------------------------------------------------

%package  -n kde4-kapptemplate
Summary:   Template for KDE Application Development
Group:     Graphical desktop/KDE
Provides:  kapptemplate4
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires:  %name-core = %epoch:%version-%release

%description   -n kde4-kapptemplate
KAppTemplate is a set of modular shell scripts that will create a 
framework for any number of KDE application types. At it's base 
level, it handles creation of things like the automake/autoconf 
framework, lsm files, RPM spec files, and po files. Then, there 
are individual modules that allow you to create a skeleton KDE 
application, a KPart application, a KPart plugin, or even convert 
existing source code to the KDE framework.

%files   -n kde4-kapptemplate
%defattr(-,root,root)
%{_kde_bindir}/kapptemplate
%{_kde_datadir}/applications/kde4/kapptemplate.desktop
%dir %{_kde_appsdir}/kapptemplate
%dir %{_kde_appsdir}/kapptemplate/appframework
%{_kde_appsdir}/kapptemplate/appframework/AUTHORS
%{_kde_appsdir}/kapptemplate/appframework/COPYING
%{_kde_appsdir}/kapptemplate/appframework/ChangeLog
%{_kde_appsdir}/kapptemplate/appframework/INSTALL
%{_kde_appsdir}/kapptemplate/appframework/NEWS
%{_kde_appsdir}/kapptemplate/appframework/README
%{_kde_appsdir}/kapptemplate/appframework/VERSION
%{_kde_appsdir}/kapptemplate/appframework/app.lsm
%{_kde_appsdir}/kapptemplate/appframework/app.spec
%{_kde_appsdir}/kapptemplate/appframework/base-Makefile.am
%{_kde_appsdir}/kapptemplate/appframework/base-Makefile.cvs
%{_kde_appsdir}/kapptemplate/appframework/configure.in.in.in
%{_kde_appsdir}/kapptemplate/appframework/no-exe/COPYING
%{_kde_appsdir}/kapptemplate/appframework/no-exe/INSTALL
%{_kde_appsdir}/kapptemplate/appframework/po-Makefile.am
%dir %{_kde_appsdir}/kapptemplate/bin
%{_kde_appsdir}/kapptemplate/bin/mkinstalldirs
%dir %{_kde_appsdir}/kapptemplate/existing
%{_kde_appsdir}/kapptemplate/existing/app-Makefile.am
%{_kde_appsdir}/kapptemplate/existing/app-desktop
%dir %{_kde_appsdir}/kapptemplate/include
%{_kde_appsdir}/kapptemplate/include/existing.module
%{_kde_appsdir}/kapptemplate/include/kapp4template.module
%{_kde_appsdir}/kapptemplate/include/kapptemplate.common
%{_kde_appsdir}/kapptemplate/include/kapptemplate.module
%{_kde_appsdir}/kapptemplate/include/kpartapp.module
%{_kde_appsdir}/kapptemplate/include/kpartplugin.module
%dir %{_kde_appsdir}/kapptemplate/kapp
%{_kde_appsdir}/kapptemplate/kapp/app-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kapp/app-desktop
%{_kde_appsdir}/kapptemplate/kapp/app.cpp
%{_kde_appsdir}/kapptemplate/kapp/app.h
%{_kde_appsdir}/kapptemplate/kapp/app.kcfg
%{_kde_appsdir}/kapptemplate/kapp/apppref.cpp
%{_kde_appsdir}/kapptemplate/kapp/apppref.h
%{_kde_appsdir}/kapptemplate/kapp/appui.rc
%{_kde_appsdir}/kapptemplate/kapp/appview.cpp
%{_kde_appsdir}/kapptemplate/kapp/appview.h
%{_kde_appsdir}/kapptemplate/kapp/doc-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kapp/hi16-app-app.png
%{_kde_appsdir}/kapptemplate/kapp/hi32-app-app.png
%{_kde_appsdir}/kapptemplate/kapp/hi48-app-app.png
%{_kde_appsdir}/kapptemplate/kapp/icons-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kapp/index.docbook
%{_kde_appsdir}/kapptemplate/kapp/main.cpp
%{_kde_appsdir}/kapptemplate/kapp/no-exe/hi16-app-app.png
%{_kde_appsdir}/kapptemplate/kapp/no-exe/hi32-app-app.png
%{_kde_appsdir}/kapptemplate/kapp/no-exe/hi48-app-app.png
%{_kde_appsdir}/kapptemplate/kapp/org.kde.app.App.xml
%{_kde_appsdir}/kapptemplate/kapp/settings.kcfgc
%{_kde_appsdir}/kapptemplate/kapp/src-CMakeLists.txt
%dir %{_kde_appsdir}/kapptemplate/kapp4
%{_kde_appsdir}/kapptemplate/kapp4/kapp4-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kapp4/kapp4-desktop
%{_kde_appsdir}/kapptemplate/kapp4/kapp4.cpp
%{_kde_appsdir}/kapptemplate/kapp4/kapp4.h
%{_kde_appsdir}/kapptemplate/kapp4/kapp4.kcfg
%{_kde_appsdir}/kapptemplate/kapp4/kapp4ui.rc
%{_kde_appsdir}/kapptemplate/kapp4/kapp4view.cpp
%{_kde_appsdir}/kapptemplate/kapp4/kapp4view.h
%{_kde_appsdir}/kapptemplate/kapp4/kapp4view_base.ui
%{_kde_appsdir}/kapptemplate/kapp4/main.cpp
%{_kde_appsdir}/kapptemplate/kapp4/prefs_base.ui
%{_kde_appsdir}/kapptemplate/kapp4/settings.kcfgc
%dir %{_kde_appsdir}/kapptemplate/kpartapp
%{_kde_appsdir}/kapptemplate/kpartapp/app-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kpartapp/app-desktop
%{_kde_appsdir}/kapptemplate/kpartapp/app-main-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kpartapp/app.cpp
%{_kde_appsdir}/kapptemplate/kpartapp/app.h
%{_kde_appsdir}/kapptemplate/kpartapp/app_part-desktop
%{_kde_appsdir}/kapptemplate/kpartapp/app_part.cpp
%{_kde_appsdir}/kapptemplate/kpartapp/app_part.h
%{_kde_appsdir}/kapptemplate/kpartapp/app_part.rc
%{_kde_appsdir}/kapptemplate/kpartapp/app_shell.rc
%{_kde_appsdir}/kapptemplate/kpartapp/doc-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kpartapp/hi16-app-app.png
%{_kde_appsdir}/kapptemplate/kpartapp/hi32-app-app.png
%{_kde_appsdir}/kapptemplate/kpartapp/hi48-app-app.png
%{_kde_appsdir}/kapptemplate/kpartapp/index.docbook
%{_kde_appsdir}/kapptemplate/kpartapp/main.cpp
%dir %{_kde_appsdir}/kapptemplate/kpartapp/no-exe
%{_kde_appsdir}/kapptemplate/kpartapp/no-exe/hi16-app-app.png
%{_kde_appsdir}/kapptemplate/kpartapp/no-exe/hi32-app-app.png
%{_kde_appsdir}/kapptemplate/kpartapp/no-exe/hi48-app-app.png
%dir %{_kde_appsdir}/kapptemplate/kpartplugin
%{_kde_appsdir}/kapptemplate/kpartplugin/hi16-action-plugin.png
%{_kde_appsdir}/kapptemplate/kpartplugin/hi22-action-plugin.png
%{_kde_appsdir}/kapptemplate/kpartplugin/no-exe/hi16-action-plugin.png
%{_kde_appsdir}/kapptemplate/kpartplugin/no-exe/hi22-action-plugin.png
%{_kde_appsdir}/kapptemplate/kpartplugin/plugin-CMakeLists.txt
%{_kde_appsdir}/kapptemplate/kpartplugin/plugin_app.cpp
%{_kde_appsdir}/kapptemplate/kpartplugin/plugin_app.h
%{_kde_appsdir}/kapptemplate/kpartplugin/plugin_app.rc

%dir %_kde_docdir/HTML/en/kapptemplate
%doc %_kde_docdir/HTML/en/kapptemplate/*.bz2
%doc %_kde_docdir/HTML/en/kapptemplate/*.docbook
%doc %_kde_docdir/HTML/en/kapptemplate/*.png

#---------------------------------------------------------------------

%package  -n kde4-kuiviewer
Summary:   UI Files Viewer
Group:     Graphical desktop/KDE
Provides:  kuiviewer4
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires:  %name-core = %epoch:%version-%release

%description -n kde4-kuiviewer
Displays Qt Designer UI files

%files -n kde4-kuiviewer
%defattr(-,root,root)
%{_kde_bindir}/kuiviewer
%{_kde_libdir}/kde4/libkuiviewerpart.so
%{_kde_libdir}/kde4/quithumbnail.so
%{_kde_datadir}/applications/kde4/kuiviewer.desktop
%{_kde_appsdir}/kuiviewer/kuiviewerui.rc
%{_kde_appsdir}/kuiviewerpart/kuiviewer_part.rc
%{_kde_iconsdir}/hicolor/*/apps/kuiviewer.png
%{_kde_datadir}/kde4/services/kuiviewer_part.desktop
%{_kde_datadir}/kde4/services/designerthumbnail.desktop

#---------------------------------------------------------------------

%package -n kde4-scripts
Summary:    Script From kdesdk
Group:      Graphical desktop/KDE
Conflicts:  kdesdk4 < %epoch:3.97.1-0.746591.1
Requires:   %name-core = %epoch:%version-%release

%description -n kde4-scripts
This package contains the scripts for KDE development which are
contained in the kdesdk module.

%files -n kde4-scripts
%defattr(-,root,root)
%{_kde_bindir}/adddebug
%{_kde_bindir}/build-progress.sh
%{_kde_bindir}/cheatmake
%{_kde_bindir}/colorsvn
%{_kde_bindir}/create_cvsignore
%{_kde_bindir}/create_makefile
%{_kde_bindir}/create_makefiles
%{_kde_bindir}/create_svnignore
%{_kde_bindir}/cvs-clean
%{_kde_bindir}/cvs2dist
%{_kde_bindir}/cvsaddcurrentdir
%{_kde_bindir}/cvsbackport
%{_kde_bindir}/cvsblame
%{_kde_bindir}/cvscheck
%{_kde_bindir}/cvsforwardport
%{_kde_bindir}/cvslastchange
%{_kde_bindir}/cvslastlog
%{_kde_bindir}/cvsrevertlast
%{_kde_bindir}/cvsversion
%{_kde_bindir}/cxxmetric
%{_kde_bindir}/extend_dmalloc
%{_kde_bindir}/extractattr
%{_kde_bindir}/extractrc
%{_kde_bindir}/findmissingcrystal
%{_kde_bindir}/fix-include.sh
%{_kde_bindir}/fixkdeincludes
%{_kde_bindir}/fixuifiles
%{_kde_bindir}/includemocs
%{_kde_bindir}/kde_generate_export_header
%{_kde_bindir}/kdedoc
%{_kde_bindir}/kdekillall
%{_kde_bindir}/kdelnk2desktop.py
%{_kde_bindir}/kdemangen.pl
%{_kde_bindir}/kdesvn-build
%{_kde_bindir}/makeobj
%{_kde_bindir}/noncvslist
%{_kde_bindir}/nonsvnlist
%{_kde_bindir}/package_crystalsvg
%{_kde_bindir}/png2mng.pl
%{_kde_bindir}/pruneemptydirs
%{_kde_bindir}/qtdoc
%{_kde_bindir}/svn-clean
%{_kde_bindir}/svn2dist
%{_kde_bindir}/svnbackport
%{_kde_bindir}/svnchangesince
%{_kde_bindir}/svngettags
%{_kde_bindir}/svnintegrate
%{_kde_bindir}/svnlastchange
%{_kde_bindir}/svnlastlog
%{_kde_bindir}/svnrevertlast
%{_kde_bindir}/svnversions
%{_kde_bindir}/zonetab2pot.py

%dir %doc %_kde_docdir/HTML/en/kdesvn-build
%doc %_kde_docdir/HTML/en/kdesvn-build/*.docbook
%doc %_kde_docdir/HTML/en/kdesvn-build/index.cache.bz2

#---------------------------------------------------------------------

%package -n kde4-kbugbuster
Summary:   kbugbuster
Group:     Graphical desktop/KDE
Provides:  kbugbuster4
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires:  %name-core = %epoch:%version-%release

%description -n kde4-kbugbuster
Kbugbuster

%files -n kde4-kbugbuster
%defattr(-,root,root)
%_kde_bindir/kbugbuster
%_kde_datadir/applications/kde4/kbugbuster.desktop
%dir %_kde_appsdir/kbugbuster
%_kde_appsdir/kbugbuster/*
%_kde_iconsdir/*/*/*/kbugbuster*

%_kde_libdir/kde4/kcal_bugzilla.so
%_kde_datadir/kde4/services/kresources/kcal/bugzilla.desktop

%dir %doc %_kde_docdir/HTML/en/kbugbuster
%doc %_kde_docdir/HTML/en/kbugbuster/*.bz2
%doc %_kde_docdir/HTML/en/kbugbuster/*.docbook

#---------------------------------------------------------------------

%package strigi-analyzer
Summary: Strigi Analyzer
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version-%release

%description strigi-analyzer
Strigi analyzer

%files strigi-analyzer
%defattr(-,root,root)
%_kde_libdir/strigi/strigi*

#---------------------------------------------------------------

%package po2xml
Summary: An xml2po and vice versa converters
Group: Graphical desktop/KDE
Conflicts: kdesdk4-core < 1:3.97.1-0.752225.2
Conflicts: kde4-scripts < 1:3.97.1-0.752225.2

%description po2xml
An xml2po and vice versa converters.

%files po2xml
%defattr(-,root,root,-)
%{_kde_bindir}/po2xml
%{_kde_bindir}/split2po
%{_kde_bindir}/swappo
%{_kde_bindir}/xml2pot

#---------------------------------------------------------------------

%package -n kde4-kate
Summary:   Kate
Group:     Graphical desktop/KDE
Provides:  kate4
Obsoletes: kdebase4-kate < 1:3.97.1
Provides:  kdebase4-kate > 1:3.97.1
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Obsoletes: %lib_name-kate <= 1:3.96.1-0.740308.1
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: %name-core = %epoch:%version-%release

%description -n kde4-kate
A fast and advanced text editor with nice plugins

%files -n kde4-kate
%defattr(-,root,root)
%_kde_bindir/kate
%_kde_datadir/applications/kde4/kate.desktop
%dir %_kde_appsdir/kate
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
%_kde_libdir/libkdeinit4_kate.so
%_kde_libdir/kde4/kateexternaltoolsplugin.so
%_kde_libdir/kde4/katefilebrowserplugin.so
%_kde_libdir/kde4/katefiletemplates.so
%_kde_libdir/kde4/katefindinfilesplugin.so
%_kde_libdir/kde4/katekonsoleplugin.so
%_kde_libdir/kde4/katemailfilesplugin.so
%_kde_libdir/kde4/kateopenheaderplugin.so
%_kde_libdir/kde4/katequickdocumentswitcherplugin.so
%_kde_libdir/kde4/katesymbolviewerplugin.so
%_kde_libdir/kde4/katetabbarextensionplugin.so
%_kde_libdir/kde4/katetextfilterplugin.so
%_kde_libdir/kde4/kickermenu_kate.so
%dir %_kde_appsdir/katepart
%dir %_kde_appsdir/katepart/syntax   
%_kde_appsdir/katepart/syntax/katetemplate.xml
%_kde_appsdir/katepart/syntax/kdesvn-buildrc.xml
%_kde_datadir/kde4/services/kateexternaltoolsplugin.desktop
%_kde_datadir/kde4/services/katefilebrowserplugin.desktop
%_kde_datadir/kde4/services/katefiletemplates.desktop
%_kde_datadir/kde4/services/katefindinfilesplugin.desktop
%_kde_datadir/kde4/services/katekonsoleplugin.desktop
%_kde_datadir/kde4/services/katemailfilesplugin.desktop
%_kde_datadir/kde4/services/kateopenheader.desktop
%_kde_datadir/kde4/services/katequickdocumentswitcher.desktop
%_kde_datadir/kde4/services/katesymbolviewer.desktop
%_kde_datadir/kde4/services/katetabbarextension.desktop
%_kde_datadir/kde4/services/katetextfilter.desktop
%_kde_datadir/kde4/servicetypes/kateplugin.desktop
   
%doc %_kde_docdir/HTML/en/kate-plugins/*.png
%doc %_kde_docdir/HTML/en/kate-plugins/*.bz2
%doc %_kde_docdir/HTML/en/kate-plugins/*.docbook
%doc %_kde_docdir/HTML/en/kate/*.png
%doc %_kde_docdir/HTML/en/kate/*.bz2
%doc %_kde_docdir/HTML/en/kate/*.docbook

#---------------------------------------------------------------------

%package    devel
Summary:    Header files for kdesdk
Group:      Development/KDE and Qt
Provides:   kdesdk4-devel =  %epoch:%version-%release
Obsoletes:  %lib_name_orig-devel < 1:3.97.1
Obsoletes:  %{_lib}kdesdk41-kate-devel <= %epoch:3.96.1-0.740308.1
Obsoletes:  %{_lib}kdesdk41-devel <= %epoch:3.96.1-0.740308.1
Obsoletes:  %{_lib}kdesdk41-cervisia-devel <= %epoch:3.96.1-0.740308.1

%description  devel	
This package includes the header files you will need to compile
applications for kdesdk.

%files devel
%defattr(-,root,root,-)
%_kde_includedir/kprofilemethod.h
%_kde_includedir/ktrace.h
%_kde_includedir/kate_export.h
%dir %_kde_includedir/kate
%_kde_includedir/kate/*.h
%_kde_libdir/libantlr.so
%_kde_libdir/libktrace.so
%_kde_libdir/libkstartperf.so
%_kde_libdir/libkateinterfaces.so
%_kde_libdir/libkompareinterface.so
#---------------------------------------------------------------

%package -n kde4-umbrello
Summary:    UML Modeller
Group:      Graphical desktop/KDE
Provides:   umbrello4
Conflicts:  kdesdk4 < %epoch:3.97.1
Requires:   %name-core = %epoch:%version-%release
Obsoletes:  %name-umbrello < %epoch:3.97.1 

%description -n kde4-umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files -n kde4-umbrello
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

%package -n kde4-cervisia
Summary:    CVS client part
Group:      Graphical desktop/KDE
Provides:   cervisia4 = %epoch:%version-%release
Requires:   cvs
Conflicts:  kdesdk4 < %epoch:3.97.1-0.746591.1
Requires:   %name-core = %epoch:%version-%release
Obsoletes:  %name-cervisia < %epoch:3.97.1 
Obsoletes:  %lib_name-cervisia <= %epoch:3.96.1-0.740308.1

%description -n kde4-cervisia
CVS client part.

%files -n kde4-cervisia
%defattr(-,root,root,-)
%{_kde_bindir}/cervisia
%_kde_iconsdir/*/*/actions/svn_add.*
%_kde_iconsdir/*/*/actions/svn_branch.*
%_kde_iconsdir/*/*/actions/svn_merge.*
%_kde_iconsdir/*/*/actions/svn_remove.*
%_kde_iconsdir/*/*/actions/svn_status.*
%_kde_iconsdir/*/*/actions/svn_switch.*
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
%_kde_datadir/man/man1/cervisia.1
%_kde_libdir/libkdeinit4_cervisia.so
%_kde_libdir/libkdeinit4_cvsaskpass.so
%_kde_libdir/libkdeinit4_cvsservice.so
%{_kde_libdir}/kde4/kded_ksvnd.so
%{_kde_libdir}/kde4/kio_svn.so
%{_kde_libdir}/kde4/libcervisiapart.so
%{_kde_datadir}/kde4/services/ServiceMenus/subversion.desktop
%{_kde_datadir}/kde4/services/ServiceMenus/subversion_toplevel.desktop
%{_kde_datadir}/kde4/services/cvsservice.desktop
%{_kde_datadir}/kde4/services/kded/ksvnd.desktop
%{_kde_datadir}/kde4/services/svn+file.protocol
%{_kde_datadir}/kde4/services/svn+http.protocol
%{_kde_datadir}/kde4/services/svn+https.protocol
%{_kde_datadir}/kde4/services/svn+ssh.protocol
%{_kde_datadir}/kde4/services/svn.protocol
%{_datadir}/dbus-1/interfaces/org.kde.ksvnd.xml

%doc %_kde_docdir/HTML/en/cervisia/*.bz2
%doc %_kde_docdir/HTML/en/cervisia/*.docbook
%doc %_kde_docdir/HTML/en/cervisia/*.png

#---------------------------------------------------------------

%package -n kde4-kompare
Summary: kompare is a KDE diff graphic tool
Group: Graphical desktop/KDE
Provides: kompare4 = %epoch:%version-%release
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Obsoletes: %name-kompare < %epoch:3.97.1-0.746591.1
Requires: %name-core = %epoch:%version-%release

%description -n kde4-kompare
kompare is a KDE diff graphic tool

%files -n kde4-kompare
%defattr(-,root,root,-)
%_kde_bindir/kompare
%_kde_libdir/kde4/libkomparenavtreepart.so
%_kde_libdir/kde4/libkomparepart.so
%_kde_libdir/libkomparedialogpages.so
%_kde_libdir/libkomparediff2.so
%_kde_datadir/applications/kde4/kompare.desktop
%_kde_datadir/apps/kompare/komparepartui.rc
%_kde_datadir/apps/kompare/kompareui.rc
%_kde_datadir/doc/HTML/en/kompare/index.cache.bz2
%_kde_datadir/doc/HTML/en/kompare/index.docbook
%_kde_datadir/doc/HTML/en/kompare/settings-diff1.png
%_kde_datadir/doc/HTML/en/kompare/settings-diff2.png
%_kde_datadir/doc/HTML/en/kompare/settings-diff3.png
%_kde_datadir/doc/HTML/en/kompare/settings-diff4.png
%_kde_datadir/doc/HTML/en/kompare/settings-view1.png
%_kde_datadir/doc/HTML/en/kompare/settings-view2.png
%_kde_datadir/icons/hicolor/128x128/apps/kompare.png
%_kde_datadir/icons/hicolor/16x16/apps/kompare.png
%_kde_datadir/icons/hicolor/22x22/apps/kompare.png
%_kde_datadir/icons/hicolor/32x32/apps/kompare.png
%_kde_datadir/icons/hicolor/48x48/apps/kompare.png
%_kde_datadir/icons/hicolor/scalable/apps/kompare.svgz
%_kde_datadir/kde4/services/komparenavtreepart.desktop
%_kde_datadir/kde4/services/komparepart.desktop
%_kde_datadir/kde4/servicetypes/komparenavigationpart.desktop
%_kde_datadir/kde4/servicetypes/kompareviewpart.desktop

#---------------------------------------------------------------

%define  libkompareinterface %mklibname kompareinterface 4

%package -n %libkompareinterface
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkompareinterface
KDE 4 core library.

%post -n   %libkompareinterface -p /sbin/ldconfig
%postun -n %libkompareinterface -p /sbin/ldconfig

%files -n %libkompareinterface
%defattr(-,root,root)
%_kde_libdir/libkompareinterface.so.*


#---------------------------------------------------------------

%package -n kde4-kmtrace
Summary: Memory Allocation Debugging Tool
Group: Graphical desktop/KDE
Provides: kmtrace4 = %epoch:%version-%release
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires: %name-core = %epoch:%version-%release

%description -n kde4-kmtrace
Memory Allocation Debugging Tool

%files -n kde4-kmtrace
%defattr(-,root,root,-)
%{_kde_bindir}/kmtrace
%{_kde_bindir}/demangle
%{_kde_bindir}/kminspector
%{_kde_bindir}/kmmatch
%{_kde_appsdir}/kmtrace/kde.excludes

#---------------------------------------------------------------

%package -n kde4-kcachegrind
Summary: KCachegrind
Group: Graphical desktop/KDE
Provides: kcachegrind4 = %epoch:%version-%release
Obsoletes: %name-kcachegrind < %epoch:3.97.1
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires: %name-core = %epoch:%version-%release
%ifarch %{ix86}
Requires: valgrind
%endif

%description -n kde4-kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by 
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%files -n kde4-kcachegrind
%defattr(-,root,root,-)
%_kde_bindir/kcachegrind
%{_kde_bindir}/dprof2calltree
%{_kde_bindir}/hotshot2calltree
%{_kde_bindir}/memprof2calltree
%{_kde_bindir}/op2calltree
%{_kde_bindir}/pprof2calltree
%_kde_iconsdir/*/*/*/kcachegrind*
%dir %_kde_appsdir/kcachegrind/
%_kde_appsdir/kcachegrind/*
%_kde_datadir/applications/kde4/kcachegrind.desktop
%doc %_kde_docdir/HTML/en/kcachegrind/*.bz2
%doc %_kde_docdir/HTML/en/kcachegrind/*.docbook

#---------------------------------------------------------------
%define  libantlr %mklibname antlr 4

%package -n %libantlr
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libantlr
KDE 4 core library.

%post -n %libantlr -p /sbin/ldconfig
%postun -n %libantlr -p /sbin/ldconfig

%files -n %libantlr
%defattr(-,root,root)
%_kde_libdir/libantlr.so.*

#---------------------------------------------------------------
%define  libkateinterfaces %mklibname kateinterfaces 4

%package -n %libkateinterfaces
Summary:    KDE 4 core library
Group:      System/Libraries
Conflicts:  %lib_name-kate <= 1:3.96.1-0.740308.1

%description -n %libkateinterfaces
KDE 4 core library.

%post -n   %libkateinterfaces -p /sbin/ldconfig
%postun -n %libkateinterfaces -p /sbin/ldconfig

%files -n %libkateinterfaces
%defattr(-,root,root)
%_kde_libdir/libkateinterfaces.so.*

#-----------------------------------------------------------------------------
%define  libkstartperf %mklibname kstartperf 4

%package -n %libkstartperf
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkstartperf
KDE 4 core library.

%post -n %libkstartperf -p /sbin/ldconfig
%postun -n %libkstartperf -p /sbin/ldconfig

%files -n %libkstartperf
%defattr(-,root,root)
%_kde_libdir/libkstartperf.so.*

#-----------------------------------------------------------------------------
%define  libktrace %mklibname ktrace 4

%package -n %libktrace
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libktrace
KDE 4 core library.

%post -n %libktrace -p /sbin/ldconfig
%postun -n %libktrace -p /sbin/ldconfig

%files -n %libktrace
%defattr(-,root,root)
%_kde_libdir/libktrace.so.*

#-----------------------------------------------------------------------------

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



Name:          kdesdk4
Summary:       K Desktop Environment - Software Development Kit
Version: 4.0.80
Epoch:         1
License:       GPL
URL:           ftp://ftp.kde.org/pub/kde/stable/%version/src/
Release: %mkrel 2
Source:        ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%version.tar.bz2
BuildRoot:     %_tmppath/%name-%version-%release-root
Group:         Graphical desktop/KDE
BuildRequires: db4-devel 
BuildRequires: freetype2-devel
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: kdepim4-devel
BuildRequires: bzip2-devel 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel 
BuildRequires: png-devel 
BuildRequires: zlib-devel
BuildRequires: flex
BuildRequires: binutils-devel
BuildRequires: subversion-devel
BuildRequires: libxslt-devel
BuildRequires: mesaglut-devel 
BuildRequires: X11-devel 
BuildRequires: libltdl-devel
BuildRequires: boost-devel
Requires:      kapptemplate
Requires:      kuiviewer
Requires:      kdesdk4-scripts
Requires:      kbugbuster
Requires:      %name-strigi-analyzer
Requires:      %name-po2xml
Requires:      kate
Requires:      umbrello 
Requires:      cervisia
Requires:      kompare 
Requires:      kmtrace
Requires:      kcachegrind

%description
Software Development Kit for the K Desktop Environment.

%files
%defattr(-,root,root)

#--------------------------------------------------------------------

%package core
Summary: Common files needed for kdesdk
Group: Graphical desktop/KDE
Conflicts: %name < %epoch:3.97.1-0.746591.1
Obsoletes: %{_lib}kdesdk41 < %epoch:3.96.1-0.740308.2
Obsoletes: %name < %epoch:4.0.2-3

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

%package  -n kapptemplate
Summary:   Template for KDE Application Development
Group:     Graphical desktop/KDE
Provides:  kapptemplate4
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Conflicts: kdevelop4 < 3:4.0.80-1
Requires:  %name-core = %epoch:%version-%release
Obsoletes: kde4-kapptemplate < 1:4.0.68
Provides: kde4-kapptemplate = %epoch:%version

%description   -n kapptemplate
KAppTemplate is a set of modular shell scripts that will create a 
framework for any number of KDE application types. At it's base 
level, it handles creation of things like the automake/autoconf 
framework, lsm files, RPM spec files, and po files. Then, there 
are individual modules that allow you to create a skeleton KDE 
application, a KPart application, a KPart plugin, or even convert 
existing source code to the KDE framework.

%files   -n kapptemplate
%defattr(-,root,root)
%{_kde_bindir}/kapptemplate
%{_kde_datadir}/applications/kde4/kapptemplate.desktop
%{_kde_appsdir}/kapptemplate
%{_kde_datadir}/config.kcfg/kapptemplate.kcfg
%{_kde_appsdir}/kdevappwizard
%_kde_docdir/*/*/kapptemplate

#---------------------------------------------------------------------

%package  -n kuiviewer
Summary:   UI Files Viewer
Group:     Graphical desktop/KDE
Provides:  kuiviewer4
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires:  %name-core = %epoch:%version-%release
Obsoletes: kde4-kuiviewer < 1:4.0.68
Provides: kde4-kuiviewer = %epoch:%version

%description -n kuiviewer
Displays Qt Designer UI files

%files -n kuiviewer
%defattr(-,root,root)
%{_kde_bindir}/kuiviewer
%{_kde_libdir}/kde4/libkuiviewerpart.so
%{_kde_libdir}/kde4/quithumbnail.so
%{_kde_datadir}/applications/kde4/kuiviewer.desktop
%{_kde_appsdir}/kuiviewer
%{_kde_appsdir}/kuiviewerpart
%{_kde_iconsdir}/hicolor/*/apps/kuiviewer.png
%{_kde_datadir}/kde4/services/kuiviewer_part.desktop
%{_kde_datadir}/kde4/services/designerthumbnail.desktop

#---------------------------------------------------------------------

%package -n kdesdk4-scripts
Summary:    Script From kdesdk
Group:      Graphical desktop/KDE
Conflicts:  kdesdk4 < %epoch:3.97.1-0.746591.1
Obsoletes:  kde4-scripts
Requires:   %name-core = %epoch:%version-%release
Requires:   colorsvn

%description -n kdesdk4-scripts
This package contains the scripts for KDE development which are
contained in the kdesdk module.

%files -n kdesdk4-scripts
%defattr(-,root,root)
%{_kde_bindir}/adddebug
%{_kde_bindir}/build-progress.sh
%{_kde_bindir}/cheatmake
# (nl) Prefer the file from colorsvn as it is more up to date 
# and this removing fix a conflict between kdesdk4-scripts and colorsvn
%exclude %{_kde_bindir}/colorsvn
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
%{_kde_bindir}/optimizegraphics
%{_kde_bindir}/wcgrep
%_kde_docdir/HTML/en/kdesvn-build

#---------------------------------------------------------------------

%package -n kbugbuster
Summary:   kbugbuster
Group:     Graphical desktop/KDE
Provides:  kbugbuster4
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires:  %name-core = %epoch:%version-%release
Obsoletes: kde4-kbugbuster < 1:4.0.68
Provides: kde4-kbugbuster = %epoch:%version

%description -n kbugbuster
Kbugbuster

%files -n kbugbuster
%defattr(-,root,root)
%_kde_bindir/kbugbuster
%_kde_datadir/applications/kde4/kbugbuster.desktop
%dir %_kde_appsdir/kbugbuster
%_kde_appsdir/kbugbuster/*
%_kde_iconsdir/*/*/*/kbugbuster*
%_kde_libdir/kde4/kcal_bugzilla.so
%_kde_datadir/kde4/services/kresources/kcal/bugzilla.desktop
%_kde_docdir/*/*/kbugbuster

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
Summary: Xml2po and vice versa converters
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

%package -n kate
Summary:   Kate
Group:     Graphical desktop/KDE
Provides:  kate4
Obsoletes: kdebase4-kate < 1:3.97.1
Provides:  kdebase4-kate > 1:3.97.1
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: %name-core = %epoch:%version-%release
Obsoletes: kde4-kate < 1:4.0.68
Provides: kde4-kate = %epoch:%version

%description -n kate
A fast and advanced text editor with nice plugins

%files -n kate
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
%_kde_libdir/kde4/plasma_applet_katesession.so
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
%_kde_datadir/kde4/services/plasma-applet-katesession.desktop
%_kde_docdir/*/*/kate-plugins 
%_kde_docdir/*/*/kate

#---------------------------------------------------------------------

%package    devel
Summary:    Header files for kdesdk
Group:      Development/KDE and Qt
Provides:   kdesdk4-devel =  %epoch:%version-%release
Obsoletes:  %{_lib}kdesdk41-kate-devel < %epoch:3.96.1-0.740308.2
Obsoletes:  %{_lib}kdesdk41-devel < %epoch:3.96.1-0.740308.2
Obsoletes:  %{_lib}kdesdk41-cervisia-devel < %epoch:3.96.1-0.740308.2

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

%package -n umbrello
Summary:    UML Modeller
Group:      Graphical desktop/KDE
Provides:   umbrello4
Conflicts:  kdesdk4 < %epoch:3.97.1
Conflicts:  kdesdk-umbrello < 1:3.5.9-5
Requires:   %name-core = %epoch:%version-%release
Obsoletes:  %name-umbrello < %epoch:3.97.1 
Obsoletes:  kde4-umbrello < 1:4.0.68
Provides:   kde4-umbrello = %epoch:%version

%description -n umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files -n umbrello
%defattr(-,root,root,-)
%_kde_bindir/umbrello
%_kde_datadir/applications/kde4/umbrello.desktop
%dir %_kde_appsdir/umbrello/
%_kde_appsdir/umbrello/*
%_kde_iconsdir/*/*/*/umbrello*
%_kde_docdir/*/*/umbrello

#---------------------------------------------------------------

%package -n localize
Summary:   TODO 
Group:      Graphical desktop/KDE
Provides:   localize4
Requires:   %name-core = %epoch:%version-%release

%description -n localize
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files -n localize
%defattr(-,root,root,-)
%_kde_bindir/lokalize
%_kde_datadir/applications/kde4/lokalize.desktop                                     
%_kde_appsdir/lokalize
%_kde_datadir/config.kcfg/lokalize.kcfg  
%_kde_datadir/strigi/fieldproperties/strigi_translation.fieldproperties                                            
%_kde_iconsdir/*/*/actions/approved.*
%_kde_iconsdir/*/*/actions/insert_arg.png
%_kde_iconsdir/*/*/actions/insert_tag.png                             
%_kde_iconsdir/*/*/actions/msgid2msgstr.png                           
%_kde_iconsdir/*/*/actions/nexterror.png                              
%_kde_iconsdir/*/*/actions/nextfuzzy.png                              
%_kde_iconsdir/*/*/actions/nextfuzzyuntrans.png                       
%_kde_iconsdir/*/*/actions/nextuntranslated.png                       
%_kde_iconsdir/*/*/actions/preverror.png                              
%_kde_iconsdir/*/*/actions/prevfuzzy.png                              
%_kde_iconsdir/*/*/actions/prevfuzzyuntrans.png                       
%_kde_iconsdir/*/*/actions/prevuntranslated.png                       
%_kde_iconsdir/*/*/actions/search2msgstr.png
%_kde_iconsdir/*/*/actions/transsearch.png                            
%_kde_iconsdir/*/*/actions/catalogmanager.png
%_kde_iconsdir/*/*/actions/autodiff.png
%_kde_iconsdir/*/*/actions/diff.png
%_kde_iconsdir/*/*/apps/lokalize.*
%_kde_docdir/*/*/lokalize

#---------------------------------------------------------------

%package -n cervisia
Summary:    CVS client part
Group:      Graphical desktop/KDE
Provides:   cervisia4 = %epoch:%version-%release
Requires:   cvs
Conflicts:  kdesdk4 < %epoch:3.97.1-0.746591.1
Conflicts:  kdesdk-cervisia < 1:3.5.9-5mdv
Requires:   %name-core = %epoch:%version-%release
Obsoletes:  %name-cervisia < %epoch:3.97.1 
Obsoletes:  kde4-cervisia < 1:4.0.68
Provides:   kde4-cervisia = %epoch:%version

%description -n cervisia
CVS client part.

%files -n cervisia
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
%_kde_docdir/*/*/cervisia
%{_kde_mandir}/man1/cervisia.1.*

#---------------------------------------------------------------

%package -n kompare
Summary: KDE diff graphic tool
Group: Graphical desktop/KDE
Provides: kompare4 = %epoch:%version-%release
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Conflicts: kdesdk-kompare < 1:3.5.9-5
Obsoletes: %name-kompare < %epoch:3.97.1-0.746591.1
Requires: %name-core = %epoch:%version-%release
Obsoletes: kde4-kompare < 1:4.0.68
Provides: kde4-kompare = %epoch:%version

%description -n kompare
kompare is a KDE diff graphic tool

%files -n kompare
%defattr(-,root,root,-)
%_kde_bindir/kompare
%_kde_libdir/kde4/libkomparenavtreepart.so
%_kde_libdir/kde4/libkomparepart.so
%_kde_libdir/libkomparedialogpages.so
%_kde_libdir/libkomparediff2.so
%_kde_datadir/applications/kde4/kompare.desktop
%_kde_appsdir/kompare
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
%_kde_docdir/*/*/kompare

#---------------------------------------------------------------

%define  komparediff2_major 4
%define  libkomparediff2 %mklibname komparediff2 %komparediff2_major

%package -n %libkomparediff2
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkomparediff2
KDE 4 core library.

%if %mdkversion < 200900
%post -n   %libkomparediff2 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkomparediff2 -p /sbin/ldconfig
%endif

%files -n %libkomparediff2
%defattr(-,root,root)
%_kde_libdir/libkomparediff2.so.%{komparediff2_major}*

#---------------------------------------------------------------

%define  komparedialogpages_major 4
%define  libkomparedialogpages %mklibname komparedialogpages %komparedialogpages_major

%package -n %libkomparedialogpages
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkomparedialogpages
KDE 4 core library.

%if %mdkversion < 200900
%post -n   %libkomparedialogpages -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkomparedialogpages -p /sbin/ldconfig
%endif

%files -n %libkomparedialogpages
%defattr(-,root,root)
%_kde_libdir/libkomparedialogpages.so.%{komparedialogpages_major}*

#---------------------------------------------------------------


%define  kompareinterface_major 4
%define  libkompareinterface %mklibname kompareinterface %kompareinterface_major

%package -n %libkompareinterface
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkompareinterface
KDE 4 core library.

%if %mdkversion < 200900
%post -n   %libkompareinterface -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkompareinterface -p /sbin/ldconfig
%endif

%files -n %libkompareinterface
%defattr(-,root,root)
%_kde_libdir/libkompareinterface.so.%{kompareinterface_major}*

#---------------------------------------------------------------

%package -n kmtrace
Summary: Memory Allocation Debugging Tool
Group: Graphical desktop/KDE
Provides: kmtrace4 = %epoch:%version-%release
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Requires: %name-core = %epoch:%version-%release
Obsoletes: kde4-kmtrace < 1:4.0.68
Provides: kde4-kmtrace = %epoch:%version

%description -n kmtrace
Memory Allocation Debugging Tool

%files -n kmtrace
%defattr(-,root,root,-)
%{_kde_bindir}/kmtrace
%{_kde_bindir}/demangle
%{_kde_bindir}/kminspector
%{_kde_bindir}/kmmatch
%{_kde_appsdir}/kmtrace

#---------------------------------------------------------------

%package -n kcachegrind
Summary: KCachegrind
Group: Graphical desktop/KDE
Provides: kcachegrind4 = %epoch:%version-%release
Obsoletes: %name-kcachegrind < %epoch:3.97.1
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Conflicts: kdesdk-kcachegrind < 1:3.5.9-5
Requires: %name-core = %epoch:%version-%release
Obsoletes: kde4-kcachegrind < 1:4.0.68
Provides: kde4-kcachegrind = %epoch:%version
%ifarch %{ix86}
Requires: valgrind
%endif

%description -n kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by 
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%files -n kcachegrind
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
%_kde_docdir/*/*/kcachegrind

#---------------------------------------------------------------

%define  antlr_major 4
%define  libantlr %mklibname antlr %antlr_major

%package -n %libantlr
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libantlr
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libantlr -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libantlr -p /sbin/ldconfig
%endif

%files -n %libantlr
%defattr(-,root,root)
%_kde_libdir/libantlr.so.%{antlr_major}*

#---------------------------------------------------------------

%define  kateinterfaces_major 4
%define  libkateinterfaces %mklibname kateinterfaces %kateinterfaces_major

%package -n %libkateinterfaces
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkateinterfaces
KDE 4 core library.

%if %mdkversion < 200900
%post -n   %libkateinterfaces -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkateinterfaces -p /sbin/ldconfig
%endif

%files -n %libkateinterfaces
%defattr(-,root,root)
%_kde_libdir/libkateinterfaces.so.%{kateinterfaces_major}*

#-----------------------------------------------------------------------------

%define  kstartperf_major 4
%define  libkstartperf %mklibname kstartperf %kstartperf_major

%package -n %libkstartperf
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkstartperf
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libkstartperf -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkstartperf -p /sbin/ldconfig
%endif

%files -n %libkstartperf
%defattr(-,root,root)
%_kde_libdir/libkstartperf.so.%{kstartperf_major}*

#-----------------------------------------------------------------------------

%define  ktrace_major 4
%define  libktrace %mklibname ktrace %ktrace_major

%package -n %libktrace
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libktrace
KDE 4 core library.

%if %mdkversion < 200900
%post -n %libktrace -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libktrace -p /sbin/ldconfig
%endif

%files -n %libktrace
%defattr(-,root,root)
%_kde_libdir/libktrace.so.%{ktrace_major}*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdesdk-%version

%build

%cmake_kde4

%make

%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%clean
rm -fr %buildroot



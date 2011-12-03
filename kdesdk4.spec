Name: kdesdk4
Summary: K Desktop Environment - Software Development Kit
Version: 4.7.80
Release: 1
Epoch: 1
License: GPL
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%{version}.tar.bz2
Group: Graphical desktop/KDE
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdepimlibs4-devel
BuildRequires: kdebase4-devel
BuildRequires: subversion-devel
BuildRequires: libxslt-devel
BuildRequires: binutils-devel
BuildRequires: boost-devel
BuildRequires: hunspell-devel
BuildRequires: libltdl-devel
BuildRequires: antlr
BuildRequires: antlr-native
Suggests: kapptemplate
Suggests: kuiviewer
Suggests: kdesdk4-scripts
Suggests: %name-strigi-analyzer
Suggests: %name-po2xml
Suggests: umbrello 
Suggests: cervisia
Suggests: kompare 
Suggests: kmtrace
Suggests: kcachegrind
Suggests: lokalize
Suggests: okteta

%description
Software Development Kit for the K Desktop Environment.

%files


#--------------------------------------------------------------------

%package core
Summary: Common files needed for kdesdk
Group: Graphical desktop/KDE
Requires:  kdebase4-runtime

%description core
Common files needed for kdesdk

%files core

%{_kde_bindir}/krazy-licensecheck
%{_kde_bindir}/cvsaskpass
%{_kde_bindir}/cvsservice
%{_kde_bindir}/kio_svn_helper
%{_kde_bindir}/kstartperf
%{_kde_bindir}/kpartloader
%{_kde_libdir}/kde4/kabcformat_kdeaccounts.so
%{_kde_libdir}/libkdeinit4_cvsaskpass.so
%{_kde_libdir}/libkdeinit4_cvsservice.so
%{_kde_libdir}/kde4/fileviewgitplugin.so
%{_kde_libdir}/kde4/fileviewsvnplugin.so
%{_kde_appsdir}/kabc/formats/kdeaccountsplugin.desktop
%{_kde_appsdir}/kio_perldoc
%{_kde_appsdir}/kpartloader
%{_kde_libdir}/kde4/kio_perldoc.so
%{_kde_services}/perldoc.protocol
%{_kde_services}/fileviewgitplugin.desktop
%{_kde_services}/fileviewsvnplugin.desktop
%{_kde_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_kde_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg

#---------------------------------------------------------------------

%package  -n kapptemplate
Summary:   Template for KDE Application Development
Group:     Graphical desktop/KDE
Provides:  kapptemplate4
Requires:  %name-core = %epoch:%version-%release
Requires:  kdelibs4-devel

%description   -n kapptemplate
KAppTemplate is a set of modular shell scripts that will create a 
framework for any number of KDE application types. At it's base 
level, it handles creation of things like the automake/autoconf 
framework, lsm files, RPM spec files, and po files. Then, there 
are individual modules that allow you to create a skeleton KDE 
application, a KPart application, a KPart plugin, or even convert 
existing source code to the KDE framework.

%files   -n kapptemplate

%{_kde_bindir}/kapptemplate
%{_kde_datadir}/applications/kde4/kapptemplate.desktop
%{_kde_datadir}/config.kcfg/kapptemplate.kcfg
%{_kde_appsdir}/kdevappwizard
%_kde_docdir/*/*/kapptemplate
%_kde_iconsdir/hicolor/*/apps/kapptemplate.png
%_kde_appsdir/kdesdk/scripts

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

%{_kde_bindir}/kuiviewer
%_kde_libdir/kde4/quithumbnail.so
%_kde_libdir/kde4/kuiviewerpart.so
%{_kde_datadir}/applications/kde4/kuiviewer.desktop
%{_kde_appsdir}/kuiviewer
%{_kde_appsdir}/kuiviewerpart
%{_kde_iconsdir}/hicolor/*/apps/kuiviewer.png
%_kde_services/kuiviewer_part.desktop
%_kde_services/designerthumbnail.desktop

#---------------------------------------------------------------------

%package -n kdesdk4-scripts
Summary:    Script From kdesdk
Group:      Graphical desktop/KDE
Obsoletes:  kde4-scripts
Requires:   %name-core = %epoch:%version-%release
Requires:   colorsvn

%description -n kdesdk4-scripts
This package contains the scripts for KDE development which are
contained in the kdesdk module.

%files -n kdesdk4-scripts

%{_kde_bindir}/adddebug
%{_kde_bindir}/build-progress.sh
%{_kde_bindir}/cheatmake
%{_kde_bindir}/create_cvsignore
%{_kde_bindir}/create_makefile
%{_kde_bindir}/create_makefiles
%{_kde_bindir}/create_svnignore
%{_kde_bindir}/cvs-clean
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
%{_kde_bindir}/makeobj
%{_kde_bindir}/noncvslist
%{_kde_bindir}/nonsvnlist
%{_kde_bindir}/package_crystalsvg
%{_kde_bindir}/png2mng.pl
%{_kde_bindir}/pruneemptydirs
%{_kde_bindir}/qtdoc
%{_kde_bindir}/svn-clean
%{_kde_bindir}/svnbackport
%{_kde_bindir}/svnchangesince
%{_kde_bindir}/svngettags
%{_kde_bindir}/svnintegrate
%{_kde_bindir}/svnforwardport
%{_kde_bindir}/svnlastchange
%{_kde_bindir}/svnlastlog
%{_kde_bindir}/svnrevertlast
%{_kde_bindir}/svnversions
%{_kde_bindir}/zonetab2pot.py
%{_kde_bindir}/optimizegraphics
%{_kde_bindir}/wcgrep
%{_kde_bindir}/extractqml
%{_kde_bindir}/kde-systemsettings-tree.py
%{_kde_libdir}/kde4/kstartperf.so
%_kde_mandir/man1/adddebug.1.*
%_kde_mandir/man1/cheatmake.1.*
%_kde_mandir/man1/create_cvsignore.1.*
%_kde_mandir/man1/create_makefile.1.*
%_kde_mandir/man1/create_makefiles.1.*
%_kde_mandir/man1/cvscheck.1.*
%_kde_mandir/man1/cvslastchange.1.*
%_kde_mandir/man1/cvslastlog.1.*
%_kde_mandir/man1/cvsrevertlast.1.*
%_kde_mandir/man1/cxxmetric.1.*
%_kde_mandir/man1/demangle.1.*
%_kde_mandir/man1/extend_dmalloc.1.*
%_kde_mandir/man1/extractrc.1.*
%_kde_mandir/man1/fixincludes.1.*
%_kde_mandir/man1/pruneemptydirs.1.*
%_kde_mandir/man1/qtdoc.1.*
%_kde_mandir/man1/reportview.1.*
%_kde_mandir/man1/transxx.1.*
%_kde_mandir/man1/xml2pot.1.*
%_kde_mandir/man1/zonetab2pot.py.1.*

#---------------------------------------------------------------------

%package strigi-analyzer
Summary: Strigi Analyzer
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version-%release

%description strigi-analyzer
Strigi analyzer

%files strigi-analyzer

%_kde_libdir/strigi/strigi*

#---------------------------------------------------------------

%package po2xml
Summary: Xml2po and vice versa converters
Group: Graphical desktop/KDE
Suggests: md5deep

%description po2xml
An xml2po and vice versa converters.

%files po2xml
%defattr(-,root,root,-)
%{_kde_bindir}/split2po
%{_kde_bindir}/xml2pot
%{_kde_bindir}/po2xml
%{_kde_bindir}/swappo
%{_kde_mandir}/man1/po2xml.1.*
%{_kde_mandir}/man1/split2po.1.*
%{_kde_mandir}/man1/swappo.1.*
%{_kde_mandir}/man1/xml2pot.1.*

#---------------------------------------------------------------

%package -n umbrello
Summary:    UML Modeller
Group:      Graphical desktop/KDE
Provides:   umbrello4
Requires:   %name-core = %epoch:%version-%release

%description -n umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files -n umbrello
%defattr(-,root,root,-)
%_kde_bindir/umbrello
%_kde_datadir/applications/kde4/umbrello.desktop
%dir %_kde_appsdir/umbrello/
%_kde_appsdir/umbrello/*
%_kde_iconsdir/*/*/*/umbrello*
%_kde_iconsdir/*/*/mimetypes/application-x-uml.png
%_kde_docdir/*/*/umbrello

#---------------------------------------------------------------

%package -n lokalize
Summary:    Computer-Aided Translation Tool
Group:      Graphical desktop/KDE
Provides:   lokalize4
Requires:   %name-core = %epoch:%version-%release
Requires:   kdesdk4-strigi-analyzer
Requires:   qt4-database-plugin-sqlite
Suggests:   python-translate

%description -n lokalize
Lokalize is a computer-aided translation system that focuses on 
productivity and performance. Translator does only creative work 
(of delivering message in his/her mother language in laconic and 
easy to understand form). Lokalize implies paragraph-by-paragraph 
translation approach (when translating documentation) and 
message-by-message approach (when translating GUI).

%files -n lokalize
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
%_kde_iconsdir/*/*/actions/diff.png
%_kde_iconsdir/*/*/actions/nextpo.png
%_kde_iconsdir/*/*/actions/nexttemplate.png
%_kde_iconsdir/*/*/actions/prevpo.png
%_kde_iconsdir/*/*/actions/prevtemplate.png

%_kde_iconsdir/*/*/apps/lokalize.*
%_kde_docdir/*/*/lokalize

#---------------------------------------------------------------

%package -n cervisia
Summary:    CVS client part
Group:      Graphical desktop/KDE
Requires:   cvs
Requires:   %name-core = %epoch:%version-%release

%description -n cervisia
CVS client part.

%files -n cervisia
%defattr(-,root,root,-)
%{_kde_bindir}/cervisia
%_kde_datadir/applications/kde4/cervisia.desktop
%_kde_appsdir/cervisia/cervisia.notifyrc
%_kde_appsdir/cervisia/cervisiashellui.rc
%_kde_appsdir/cervisiapart/cervisiaui.rc
%_kde_appsdir/kconf_update/cervisia-change_repos_list.pl
%_kde_appsdir/kconf_update/cervisia-normalize_cvsroot.pl
%_kde_appsdir/kconf_update/cervisia.upd
%_kde_appsdir/kconf_update/change_colors.pl
%_kde_datadir/config.kcfg/cervisiapart.kcfg
%_kde_iconsdir/*/*/apps/cervisia.*
%_kde_libdir/libkdeinit4_cervisia.so
%_kde_libdir/kde4/kded_ksvnd.so
%_kde_libdir/kde4/kio_svn.so
%_kde_libdir/kde4/cervisiapart.so
%_kde_services/ServiceMenus/subversion.desktop
%_kde_services/ServiceMenus/subversion_toplevel.desktop
%_kde_services/cervisiapart.desktop
%_kde_services/cvsservice.desktop
%_kde_services/kded/ksvnd.desktop
%_kde_services/svn+file.protocol
%_kde_services/svn+http.protocol
%_kde_services/svn+https.protocol
%_kde_services/svn+ssh.protocol
%_kde_services/svn.protocol
%_kde_docdir/*/*/cervisia
%{_kde_mandir}/man1/cervisia.1.*

#---------------------------------------------------------------

%package -n okteta
Summary: Edit raw file data as Hex values
Group: Graphical desktop/KDE

%description -n okteta
Okteta is a simple editor for the raw data of files. This type of
program is also called hex editor or binary editor.

%files -n okteta

%_kde_bindir/okteta
%_kde_libdir/kde4/libkbytearrayedit.so
%_kde_libdir/kde4/oktetapart.so
%_kde_applicationsdir/okteta.desktop
%_kde_appsdir/okteta
%_kde_appsdir/oktetapart
%_kde_datadir/config.kcfg/structviewpreferences.kcfg
%_kde_configdir/okteta-structures.knsrc
%_kde_iconsdir/*/*/apps/okteta.png
%_kde_services/kbytearrayedit.desktop
%_kde_services/oktetapart.desktop
%_kde_datadir/mime/packages/okteta.xml
%doc %_kde_docdir/HTML/en/okteta

#---------------------------------------------------------------

%define liboktetagui_major 4
%define liboktetagui %mklibname oktetagui %{liboktetagui_major}

%package -n %liboktetagui
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetagui
KDE 4 library

%files -n %liboktetagui

%_kde_libdir/liboktetagui.so.%{liboktetagui_major}*

#---------------------------------------------------------------

%define liboktetakastencore_major 4
%define liboktetakastencore %mklibname oktetakastencore %{liboktetakastencore_major}

%package -n %liboktetakastencore
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetakastencore
KDE 4 library

%files -n %liboktetakastencore

%_kde_libdir/liboktetakastencore.so.%{liboktetakastencore_major}*

#---------------------------------------------------------------

%define liboktetakastencontrollers_major 4
%define liboktetakastencontrollers %mklibname oktetakastencontrollers %{liboktetakastencontrollers_major}

%package -n %liboktetakastencontrollers
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetakastencontrollers
KDE 4 library

%files -n %liboktetakastencontrollers

%_kde_libdir/liboktetakastencontrollers.so.%{liboktetakastencontrollers_major}*

#---------------------------------------------------------------

%define libkastengui_major 4
%define libkastengui %mklibname kastengui %{libkastengui_major}

%package -n %libkastengui
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkastengui
KDE 4 library

%files -n %libkastengui

%_kde_libdir/libkastengui.so.%{libkastengui_major}*

#---------------------------------------------------------------

%define libkastencore_major 4
%define libkastencore %mklibname kastencore %{libkastencore_major}

%package -n %libkastencore
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkastencore
KDE 4 library

%files -n %libkastencore

%_kde_libdir/libkastencore.so.%{libkastencore_major}*

#---------------------------------------------------------------

%define libkastencontrollers_major 4
%define libkastencontrollers %mklibname kastencontrollers %{libkastencontrollers_major}

%package -n %libkastencontrollers
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkastencontrollers
KDE 4 library

%files -n %libkastencontrollers

%_kde_libdir/libkastencontrollers.so.%{libkastencontrollers_major}*

#---------------------------------------------------------------

%package -n kompare
Summary: KDE diff graphic tool
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version-%release

%description -n kompare
kompare is a KDE diff graphic tool

%files -n kompare
%defattr(-,root,root,-)
%_kde_bindir/kompare
%_kde_libdir/kde4/libkomparenavtreepart.so
%_kde_libdir/kde4/libkomparepart.so
%_kde_datadir/applications/kde4/kompare.desktop
%_kde_appsdir/kompare
%_kde_iconsdir/hicolor/128x128/apps/kompare.png
%_kde_iconsdir/hicolor/16x16/apps/kompare.png
%_kde_iconsdir/hicolor/22x22/apps/kompare.png
%_kde_iconsdir/hicolor/32x32/apps/kompare.png
%_kde_iconsdir/hicolor/48x48/apps/kompare.png
%_kde_iconsdir/hicolor/scalable/apps/kompare.svgz
%_kde_services/komparenavtreepart.desktop
%_kde_services/komparepart.desktop
%_kde_servicetypes/komparenavigationpart.desktop
%_kde_servicetypes/kompareviewpart.desktop
%_kde_docdir/*/*/kompare

#---------------------------------------------------------------

%define  komparediff2_major 4
%define  libkomparediff2 %mklibname komparediff2_ %komparediff2_major

%package -n %libkomparediff2
Summary:    KDE 4 core library
Group:      System/Libraries
Obsoletes:  %{_lib}komparediff24

%description -n %libkomparediff2
KDE 4 core library.

%files -n %libkomparediff2

%_kde_libdir/libkomparediff2.so.%{komparediff2_major}*

#---------------------------------------------------------------

%define  komparedialogpages_major 4
%define  libkomparedialogpages %mklibname komparedialogpages %komparedialogpages_major

%package -n %libkomparedialogpages
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkomparedialogpages
KDE 4 core library.

%files -n %libkomparedialogpages

%_kde_libdir/libkomparedialogpages.so.%{komparedialogpages_major}*

#---------------------------------------------------------------


%define  kompareinterface_major 4
%define  libkompareinterface %mklibname kompareinterface %kompareinterface_major

%package -n %libkompareinterface
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkompareinterface
KDE 4 core library.

%files -n %libkompareinterface

%_kde_libdir/libkompareinterface.so.%{kompareinterface_major}*

#---------------------------------------------------------------

%package -n kmtrace
Summary: Memory Allocation Debugging Tool
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version-%release

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
Requires: %name-core = %epoch:%version-%release
Requires: valgrind

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

%define  kateinterfaces_major 4
%define  libkateinterfaces %mklibname kateinterfaces %kateinterfaces_major

%package -n %libkateinterfaces
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkateinterfaces
KDE 4 core library.

%files -n %libkateinterfaces

%_kde_libdir/libkateinterfaces.so.%{kateinterfaces_major}*

#-----------------------------------------------------------------------------

%define  ktrace_major 4
%define  libktrace %mklibname ktrace %ktrace_major

%package -n %libktrace
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libktrace
KDE 4 core library.

%files -n %libktrace

%_kde_libdir/libktrace.so.%{ktrace_major}*

#-----------------------------------------------------------------------------

%define  ktexteditor_codesnippets_core_major 0
%define  libktexteditor_codesnippets_core %mklibname ktexteditor_codesnippets_core %ktexteditor_codesnippets_core_major

%package -n %libktexteditor_codesnippets_core
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libktexteditor_codesnippets_core
KDE 4 core library.

%files -n %libktexteditor_codesnippets_core

%_kde_libdir/libktexteditor_codesnippets_core.so.%{ktexteditor_codesnippets_core_major}*

#---------------------------------------------------------------------

%package    devel
Summary:    Header files for kdesdk
Group:      Development/KDE and Qt
Requires: %libkomparediff2 = %epoch:%version
Requires: %libkomparedialogpages = %epoch:%version
Requires: %libkompareinterface = %epoch:%version
Requires: %libkateinterfaces = %epoch:%version
Requires: %libktrace = %epoch:%version
Requires: %libktexteditor_codesnippets_core = %epoch:%version
Requires: %liboktetagui = %epoch:%version
Requires: %liboktetakastencore = %epoch:%version
Requires: %liboktetakastencontrollers = %epoch:%version
Requires: %libkastengui = %epoch:%version
Requires: %libkastencore = %epoch:%version
Requires: %libkastencontrollers = %epoch:%version

%description  devel
This package includes the header files you will need to compile
applications for kdesdk.

%files devel
%defattr(-,root,root,-)
%_kde_includedir/*
%_kde_libdir/libktrace.so
%_kde_libdir/libkateinterfaces.so
%_kde_libdir/libkompareinterface.so
%_kde_libdir/libkomparediff2.so
%_kde_libdir/libkomparedialogpages.so
%_kde_libdir/libktexteditor_codesnippets_core.so
%_kde_libdir/libkastencontrollers.so
%_kde_libdir/libkastencore.so
%_kde_libdir/libkastengui.so
%_kde_libdir/liboktetagui.so
%_kde_libdir/liboktetakastencontrollers.so
%_kde_libdir/liboktetakastencore.so
%_kde_libdir/kde4/plugins/designer/oktetadesignerplugin.so
%_kde_datadir/dbus-1/interfaces/*

#---------------------------------------------------------------

%prep
%setup -q -n kdesdk-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# Copy all scripts 
mkdir -p %buildroot/%_kde_appsdir/kdesdk/
cp -a scripts %buildroot/%_kde_appsdir/kdesdk/
rm -f %buildroot/%_kde_appsdir/kdesdk/CMake*

# (nl) Prefer the file from colorsvn as it is more up to date
# and this fix a conflict between kdesdk4-scripts and colorsvn
rm -f %buildroot%{_kde_bindir}/colorsvn


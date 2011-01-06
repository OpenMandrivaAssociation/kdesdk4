%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1198704
%endif

Name: kdesdk4
Summary: K Desktop Environment - Software Development Kit
Version: 4.5.95
%if %branch
Release: %mkrel -c %kde_snapshot 1
%else
Release: %mkrel 1
%endif
Epoch: 1
License: GPL
%if %branch
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdesdk-%{version}%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%{version}.tar.bz2
%endif
BuildRoot: %_tmppath/%name-%version-%release-root
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
Suggests: kate
Suggests: umbrello 
Suggests: cervisia
Suggests: kompare 
Suggests: kmtrace
Suggests: kcachegrind
Suggests: lokalize
Suggests: okteta
Obsoletes: kbugbuster < 1:4.5.76

%description
Software Development Kit for the K Desktop Environment.

%files
%defattr(-,root,root)

#--------------------------------------------------------------------

%package core
Summary: Common files needed for kdesdk
Group: Graphical desktop/KDE
Conflicts: %name < %epoch:3.97.1-0.746591.1
Conflicts: cervisia < 1:4.2.85-2
Obsoletes: %{_lib}kdesdk41 < %epoch:3.96.1-0.740308.2
Obsoletes: %name < %epoch:4.0.2-3
Requires:  kdebase4-runtime

%description core
Common files needed for kdesdk

%files core
%defattr(-,root,root)
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
%{_kde_iconsdir}/oxygen/16x16/actions/repoadd.png
%{_kde_iconsdir}/oxygen/16x16/actions/repomanage.png
%{_kde_iconsdir}/oxygen/16x16/actions/snippetadd.png
%{_kde_iconsdir}/oxygen/16x16/actions/snippetedit.png

#---------------------------------------------------------------------

%package  -n kapptemplate
Summary:   Template for KDE Application Development
Group:     Graphical desktop/KDE
Provides:  kapptemplate4
Conflicts: kdesdk4 < %epoch:3.97.1-0.746591.1
Conflicts: kdevelop4 < 3:4.0.80-1
Requires:  %name-core = %epoch:%version-%release
Requires:  kdelibs4-devel
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
%defattr(-,root,root)
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
%{_kde_bindir}/kdesrc-build
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
%{_kde_applicationsdir}/kdesrc-build.desktop
%doc %_kde_docdir/HTML/en/kdesrc-build
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
%defattr(-,root,root)
%_kde_libdir/strigi/strigi*

#---------------------------------------------------------------

%package po2xml
Summary: Xml2po and vice versa converters
Group: Graphical desktop/KDE
Conflicts: kdesdk4-core < 1:3.97.1-0.752225.2
Conflicts: kde4-scripts < 1:3.97.1-0.752225.2
Conflicts: kdesdk4-scripts < 1:4.5.85-3
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
Requires: konsole
%if %mdkversion >= 200100
Obsoletes:     kdebase-kate < 1:3.5.10-24
Obsoletes:     kdebase3-kate < 1:3.5.10-24
%endif

%description -n kate
A fast and advanced text editor with nice plugins

%files -n kate
%defattr(-,root,root)
%_kde_bindir/kate
%_kde_bindir/ktesnippets_editor
%_kde_datadir/config/ktexteditor_codesnippets_core.knsrc
%_kde_appsdir/ktexteditor_snippets
%_kde_datadir/applications/kde4/kate.desktop
%_kde_iconsdir/hicolor/*/apps/kate.*
%_kde_iconsdir/*/*/actions/debug.png
%_kde_iconsdir/*/*/actions/interrupt.png
%_kde_iconsdir/*/*/actions/kill.png
%_kde_appsdir/kate
%_kde_appsdir/kconf_update/kate-2.4.upd
%_kde_datadir/config/katerc
%_kde_datadir/config/katefiletemplates.knsrc
%_kde_libdir/libkdeinit4_kate.so
%_kde_libdir/kde4/katebacktracebrowserplugin.so
%_kde_libdir/kde4/kateexternaltoolsplugin.so
%_kde_libdir/kde4/katefilebrowserplugin.so
%_kde_libdir/kde4/katefiletemplates.so
%_kde_libdir/kde4/katefindinfilesplugin.so
%_kde_libdir/kde4/kategdbplugin.so
%_kde_libdir/kde4/katekonsoleplugin.so
%_kde_libdir/kde4/katemailfilesplugin.so
%_kde_libdir/kde4/kateopenheaderplugin.so
%_kde_libdir/kde4/katequickdocumentswitcherplugin.so
%_kde_libdir/kde4/katesymbolviewerplugin.so
%_kde_libdir/kde4/katetabbarextensionplugin.so
%_kde_libdir/kde4/katetextfilterplugin.so
%_kde_libdir/kde4/plasma_applet_katesession.so
%_kde_libdir/kde4/katebuildplugin.so
%_kde_libdir/kde4/katectagsplugin.so
%_kde_libdir/kde4/kate_kttsd.so
%_kde_libdir/kde4/katexmlcheckplugin.so
%_kde_libdir/kde4/katesnippets_tngplugin.so
%_kde_libdir/kde4/katetabifyplugin.so
%_kde_libdir/kde4/katexmltoolsplugin.so
%_kde_libdir/kde4/katefiletreeplugin.so
%_kde_libdir/kde4/katesqlplugin.so
%_kde_appsdir/katepart
%_kde_services/katebacktracebrowserplugin.desktop
%_kde_services/kateexternaltoolsplugin.desktop
%_kde_services/katefilebrowserplugin.desktop
%_kde_services/katefiletemplates.desktop
%_kde_services/katefindinfilesplugin.desktop
%_kde_services/kategdbplugin.desktop
%_kde_services/katekonsoleplugin.desktop
%_kde_services/katemailfilesplugin.desktop
%_kde_services/kateopenheader.desktop
%_kde_services/katequickdocumentswitcher.desktop
%_kde_services/katesymbolviewer.desktop
%_kde_services/katetabbarextension.desktop
%_kde_services/katetextfilter.desktop
%_kde_servicetypes/kateplugin.desktop
%_kde_services/plasma-applet-katesession.desktop
%_kde_services/katebuildplugin.desktop
%_kde_services/katectagsplugin.desktop
%_kde_services/kate_kttsd.desktop
%_kde_services/katexmlcheck.desktop
%_kde_services/katesnippets_tngplugin.desktop
%_kde_services/katetabifyplugin.desktop
%_kde_services/katexmltools.desktop
%_kde_services/katesql.desktop
%_kde_services/katefiletreeplugin.desktop
%_kde_datadir/applications/kde4/ktesnippets_editor.desktop
%_kde_appsdir/katexmltools
%_kde_mandir/man1/kate.1.*
%_kde_datadir/mime/packages/ktesnippets.xml
%_kde_docdir/*/*/kate

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
%_kde_iconsdir/*/*/mimetypes/application-x-uml.png
%_kde_docdir/*/*/umbrello

#---------------------------------------------------------------

%package -n lokalize
Summary:    Computer-Aided Translation Tool
Group:      Graphical desktop/KDE
Provides:   lokalize4
Obsoletes:  localise < 1:4.0.83-4
Obsoletes:  localise4 < 1:4.0.83-4
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
%_kde_iconsdir/*/*/actions/vcs_add.*
%_kde_iconsdir/*/*/actions/vcs_commit.*
%_kde_iconsdir/*/*/actions/vcs_diff.*
%_kde_iconsdir/*/*/actions/vcs_remove.*
%_kde_iconsdir/*/*/actions/vcs_status.*
%_kde_iconsdir/*/*/actions/vcs_update.*
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
%if %mdkversion >= 201000
Obsoletes: kdeutils-khexedit < 3.5.10-3
%endif

%description -n okteta
Okteta is a simple editor for the raw data of files. This type of
program is also called hex editor or binary editor.

%files -n okteta
%defattr(-,root,root)
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
 
%define liboktetacore_major 4
%define liboktetacore %mklibname oktetacore %{liboktetacore_major}

%package -n %liboktetacore
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetacore
KDE 4 library

%files -n %liboktetacore
%defattr(-,root,root)
%_kde_libdir/liboktetacore.so.%{liboktetacore_major}*

#---------------------------------------------------------------

%define liboktetakastengui_major 4
%define liboktetakastengui %mklibname oktetakastengui %{liboktetakastengui_major}

%package -n %liboktetakastengui
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetakastengui
KDE 4 library

%files -n %liboktetakastengui
%defattr(-,root,root)
%_kde_libdir/liboktetakastengui.so.%{liboktetakastengui_major}*

#---------------------------------------------------------------

%define liboktetagui_major 4
%define liboktetagui %mklibname oktetagui %{liboktetagui_major}

%package -n %liboktetagui
Summary: KDE 4 library
Group: System/Libraries

%description -n %liboktetagui
KDE 4 library

%files -n %liboktetagui
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
%_kde_libdir/libkastencontrollers.so.%{libkastencontrollers_major}*

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

%define  kateinterfaces_major 4
%define  libkateinterfaces %mklibname kateinterfaces %kateinterfaces_major

%package -n %libkateinterfaces
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libkateinterfaces
KDE 4 core library.

%files -n %libkateinterfaces
%defattr(-,root,root)
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
%defattr(-,root,root)
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
%defattr(-,root,root)
%_kde_libdir/libktexteditor_codesnippets_core.so.%{ktexteditor_codesnippets_core_major}*

#---------------------------------------------------------------------

%package    devel
Summary:    Header files for kdesdk
Group:      Development/KDE and Qt
Provides:   kdesdk4-devel = %epoch:%version-%release
Conflicts:  kompare < 1:4.2.0-3
Obsoletes:  %{_lib}kdesdk41-kate-devel < %epoch:3.96.1-0.740308.2
Obsoletes:  %{_lib}kdesdk41-devel < %epoch:3.96.1-0.740308.2
Obsoletes:  %{_lib}kdesdk41-cervisia-devel < %epoch:3.96.1-0.740308.2
Requires: %libkomparediff2 = %epoch:%version
Requires: %libkomparedialogpages = %epoch:%version
Requires: %libkompareinterface = %epoch:%version
Requires: %libkateinterfaces = %epoch:%version
Requires: %libktrace = %epoch:%version
Requires: %libktexteditor_codesnippets_core = %epoch:%version
Requires: %liboktetacore = %epoch:%version
Requires: %liboktetakastengui = %epoch:%version
Requires: %liboktetagui = %epoch:%version
Requires: %liboktetakastencore = %epoch:%version
Requires: %liboktetakastencontrollers = %epoch:%version
Requires: %libkastengui = %epoch:%version
Requires: %libkastencore = %epoch:%version
Requires: %libkastencontrollers = %epoch:%version
Conflicts: kdeutils4-devel < 4.5.71
Conflicts: kremotecontrol < 4.5.71

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
%_kde_libdir/liboktetacore.so
%_kde_libdir/liboktetagui.so
%_kde_libdir/liboktetakastencontrollers.so
%_kde_libdir/liboktetakastencore.so
%_kde_libdir/liboktetakastengui.so
%_kde_libdir/kde4/plugins/designer/oktetadesignerplugin.so
%_kde_datadir/dbus-1/interfaces/*

#---------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdesdk-%{version}%kde_snapshot
%else
%setup -q -n kdesdk-%{version}
%endif

%build
%cmake_kde4
%make

%install
rm -fr %buildroot

%makeinstall_std -C build

# Copy all scripts 
mkdir -p %buildroot/%_kde_appsdir/kdesdk/
cp -a scripts %buildroot/%_kde_appsdir/kdesdk/
rm -f %buildroot/%_kde_appsdir/kdesdk/CMake*

# (nl) Prefer the file from colorsvn as it is more up to date
# and this removing fix a conflict between kdesdk4-scripts and colorsvn
rm -f %buildroot%{_kde_bindir}/colorsvn


%clean
rm -fr %buildroot


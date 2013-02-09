Name:		kdesdk4
Summary:	K Desktop Environment - Software Development Kit
Version:	4.10.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdesdk-%{version}.tar.xz
Source1:	kdesdk4.rpmlintrc
BuildRequires:	kdebase4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	antlr
BuildRequires:	antlr-native
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool-devel
BuildRequires:	subversion-devel
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libxslt)
Suggests:	cervisia
Suggests:	kapptemplate
Suggests:	kcachegrind
Suggests:	kde-thumbnailer-po
Suggests:	kdesdk4-scripts
Suggests:	kdesdk4-strigi-analyzer
Suggests:	kdesdk4-po2xml
Suggests:	kmtrace
Suggests:	kompare
Suggests:	kuiviewer
Suggests:	lokalize
Suggests:	okteta
Suggests:	umbrello

%description
Software Development Kit for the K Desktop Environment.

%files

#--------------------------------------------------------------------

%package core
Summary:	Common files needed for kdesdk
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime

%description core
Common files needed for kdesdk

%files core
%{_kde_bindir}/krazy-licensecheck
%{_kde_bindir}/cvsaskpass
%{_kde_bindir}/cvsservice
%{_kde_bindir}/kio_svn_helper
%{_kde_bindir}/kstartperf
%{_kde_bindir}/kpartloader
%{_kde_bindir}/struct2osd.sh
%{_kde_libdir}/libkdeinit4_cvsaskpass.so
%{_kde_libdir}/libkdeinit4_cvsservice.so
%{_kde_libdir}/kde4/fileviewgitplugin.so
%{_kde_libdir}/kde4/fileviewsvnplugin.so
%{_kde_libdir}/kde4/fileviewbazaarplugin.so
%{_kde_libdir}/kde4/fileviewhgplugin.so
%{_kde_libdir}/kde4/kio_perldoc.so
%{_kde_appsdir}/kio_perldoc
%{_kde_appsdir}/kpartloader
%{_kde_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_kde_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_kde_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_kde_services}/perldoc.protocol
%{_kde_services}/fileviewgitplugin.desktop
%{_kde_services}/fileviewsvnplugin.desktop
%{_kde_services}/fileviewbazaarplugin.desktop
%{_kde_services}/fileviewhgplugin.desktop

#---------------------------------------------------------------------

%package -n kapptemplate
Summary:	Template for KDE Application Development
Group:		Graphical desktop/KDE
Provides:	kapptemplate4
Requires:	%{name}-core = %{epoch}:%{version}-%{release}
Requires:	kdelibs4-devel

%description -n kapptemplate
KAppTemplate is a set of modular shell scripts that will create a 
framework for any number of KDE application types. At it's base 
level, it handles creation of things like the automake/autoconf 
framework, lsm files, RPM spec files, and po files. Then, there 
are individual modules that allow you to create a skeleton KDE 
application, a KPart application, a KPart plugin, or even convert 
existing source code to the KDE framework.

%files -n kapptemplate
%{_kde_bindir}/kapptemplate
%{_kde_applicationsdir}/kapptemplate.desktop
%{_kde_datadir}/config.kcfg/kapptemplate.kcfg
%{_kde_appsdir}/kdevappwizard
%{_kde_docdir}/*/*/kapptemplate
%{_kde_iconsdir}/hicolor/*/apps/kapptemplate.png
%{_kde_appsdir}/kdesdk/scripts

#---------------------------------------------------------------------

%package -n kuiviewer
Summary:	UI Files Viewer
Group:		Graphical desktop/KDE
Provides:	kuiviewer4
Requires:	%{name}-core = %{EVRD}
Provides:	kde4-kuiviewer = %{EVRD}

%description -n kuiviewer
Displays Qt Designer UI files

%files -n kuiviewer
%{_kde_bindir}/kuiviewer
%{_kde_libdir}/kde4/quithumbnail.so
%{_kde_libdir}/kde4/kuiviewerpart.so
%{_kde_applicationsdir}/kuiviewer.desktop
%{_kde_appsdir}/kuiviewer
%{_kde_appsdir}/kuiviewerpart
%{_kde_iconsdir}/hicolor/*/apps/kuiviewer.png
%{_kde_services}/kuiviewer_part.desktop
%{_kde_services}/designerthumbnail.desktop

#---------------------------------------------------------------------

%package -n kdesdk4-scripts
Summary:	Script From kdesdk
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	colorsvn

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
%{_kde_bindir}/kde-systemsettings-tree.py
%{_kde_libdir}/kde4/kstartperf.so
%{_kde_mandir}/man1/adddebug.1.*
%{_kde_mandir}/man1/cheatmake.1.*
%{_kde_mandir}/man1/create_cvsignore.1.*
%{_kde_mandir}/man1/create_makefile.1.*
%{_kde_mandir}/man1/create_makefiles.1.*
%{_kde_mandir}/man1/cvscheck.1.*
%{_kde_mandir}/man1/cvslastchange.1.*
%{_kde_mandir}/man1/cvslastlog.1.*
%{_kde_mandir}/man1/cvsrevertlast.1.*
%{_kde_mandir}/man1/cxxmetric.1.*
%{_kde_mandir}/man1/demangle.1.*
%{_kde_mandir}/man1/extend_dmalloc.1.*
%{_kde_mandir}/man1/extractrc.1.*
%{_kde_mandir}/man1/fixincludes.1.*
%{_kde_mandir}/man1/pruneemptydirs.1.*
%{_kde_mandir}/man1/qtdoc.1.*
%{_kde_mandir}/man1/reportview.1.*
%{_kde_mandir}/man1/transxx.1.*
%{_kde_mandir}/man1/zonetab2pot.py.1.*

#---------------------------------------------------------------------

%package strigi-analyzer
Summary:	Strigi Analyzer
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description strigi-analyzer
Strigi analyzer

%files strigi-analyzer
%{_kde_libdir}/strigi/strigi*

#---------------------------------------------------------------

%package po2xml
Summary:	Xml2po and vice versa converters
Group:		Graphical desktop/KDE
Suggests:	md5deep

%description po2xml
An xml2po and vice versa converters.

%files po2xml
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
Summary:	UML Modeller
Group:		Graphical desktop/KDE
Provides:	umbrello4
Requires:	%{name}-core = %{EVRD}

%description -n umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files -n umbrello
%{_kde_bindir}/umbrello
%{_kde_applicationsdir}/umbrello.desktop
%{_kde_appsdir}/umbrello
%{_kde_iconsdir}/*/*/*/umbrello*
%{_kde_iconsdir}/*/*/mimetypes/application-x-uml.png
%{_kde_docdir}/*/*/umbrello

#---------------------------------------------------------------

%package -n lokalize
Summary:	Computer-Aided Translation Tool
Group:		Graphical desktop/KDE
Provides:	lokalize4
Requires:	%{name}-core = %{EVRD}
Requires:	kdesdk4-strigi-analyzer
Requires:	qt4-database-plugin-sqlite
Suggests:	python-translate

%description -n lokalize
Lokalize is a computer-aided translation system that focuses on 
productivity and performance. Translator does only creative work 
(of delivering message in his/her mother language in laconic and 
easy to understand form). Lokalize implies paragraph-by-paragraph 
translation approach (when translating documentation) and 
message-by-message approach (when translating GUI).

%files -n lokalize
%{_kde_bindir}/lokalize
%{_kde_applicationsdir}/lokalize.desktop
%{_kde_appsdir}/lokalize
%{_kde_datadir}/config.kcfg/lokalize.kcfg
%{_kde_datadir}/strigi/fieldproperties/strigi_translation.fieldproperties
%{_kde_iconsdir}/*/*/actions/approved.*
%{_kde_iconsdir}/*/*/actions/insert_arg.png
%{_kde_iconsdir}/*/*/actions/insert_tag.png
%{_kde_iconsdir}/*/*/actions/msgid2msgstr.png
%{_kde_iconsdir}/*/*/actions/nexterror.png
%{_kde_iconsdir}/*/*/actions/nextfuzzy.png
%{_kde_iconsdir}/*/*/actions/nextfuzzyuntrans.png
%{_kde_iconsdir}/*/*/actions/nextuntranslated.png
%{_kde_iconsdir}/*/*/actions/preverror.png
%{_kde_iconsdir}/*/*/actions/prevfuzzy.png
%{_kde_iconsdir}/*/*/actions/prevfuzzyuntrans.png
%{_kde_iconsdir}/*/*/actions/prevuntranslated.png
%{_kde_iconsdir}/*/*/actions/search2msgstr.png
%{_kde_iconsdir}/*/*/actions/transsearch.png
%{_kde_iconsdir}/*/*/actions/catalogmanager.png
%{_kde_iconsdir}/*/*/actions/diff.png
%{_kde_iconsdir}/*/*/actions/nextpo.png
%{_kde_iconsdir}/*/*/actions/nexttemplate.png
%{_kde_iconsdir}/*/*/actions/prevpo.png
%{_kde_iconsdir}/*/*/actions/prevtemplate.png
%{_kde_iconsdir}/*/*/apps/lokalize.*
%{_kde_docdir}/*/*/lokalize

#---------------------------------------------------------------

%package -n cervisia
Summary:	CVS client part
Group:		Graphical desktop/KDE
Requires:	cvs
Requires:	%{name}-core = %{EVRD}

%description -n cervisia
CVS client part.

%files -n cervisia
%{_kde_bindir}/cervisia
%{_kde_applicationsdir}/cervisia.desktop
%{_kde_appsdir}/cervisia/cervisia.notifyrc
%{_kde_appsdir}/cervisia/cervisiashellui.rc
%{_kde_appsdir}/cervisiapart/cervisiaui.rc
%{_kde_datadir}/config.kcfg/cervisiapart.kcfg
%{_kde_iconsdir}/*/*/*/*cervisia*
%{_kde_iconsdir}/*/*/*/*kiosvn*
%{_kde_libdir}/libkdeinit4_cervisia.so
%{_kde_libdir}/kde4/kded_ksvnd.so
%{_kde_libdir}/kde4/kio_svn.so
%{_kde_libdir}/kde4/cervisiapart.so
%{_kde_services}/ServiceMenus/subversion.desktop
%{_kde_services}/ServiceMenus/subversion_toplevel.desktop
%{_kde_services}/cervisiapart.desktop
%{_kde_services}/cvsservice.desktop
%{_kde_services}/kded/ksvnd.desktop
%{_kde_services}/svn+file.protocol
%{_kde_services}/svn+http.protocol
%{_kde_services}/svn+https.protocol
%{_kde_services}/svn+ssh.protocol
%{_kde_services}/svn.protocol
%{_kde_docdir}/*/*/cervisia
%{_kde_mandir}/man1/cervisia.1.*

#---------------------------------------------------------------

%package -n okteta
Summary:	Edit raw file data as Hex values
Group:		Graphical desktop/KDE

%description -n okteta
Okteta is a simple editor for the raw data of files. This type of
program is also called hex editor or binary editor.

%files -n okteta
%{_kde_bindir}/okteta
%{_kde_libdir}/kde4/libkbytearrayedit.so
%{_kde_libdir}/kde4/oktetapart.so
%{_kde_applicationsdir}/okteta.desktop
%{_kde_appsdir}/okteta
%{_kde_appsdir}/oktetapart
%{_kde_datadir}/config.kcfg/structviewpreferences.kcfg
%{_kde_configdir}/okteta-structures.knsrc
%{_kde_iconsdir}/*/*/apps/okteta.png
%{_kde_services}/kbytearrayedit.desktop
%{_kde_services}/oktetapart.desktop
%{_kde_datadir}/mime/packages/okteta.xml
%doc %{_kde_docdir}/HTML/en/okteta

#---------------------------------------------------------------

%package -n kompare
Summary:	KDE diff graphic tool
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n kompare
kompare is a KDE diff graphic tool

%files -n kompare
%{_kde_bindir}/kompare
%{_kde_libdir}/kde4/komparenavtreepart.so
%{_kde_libdir}/kde4/komparepart.so
%{_kde_applicationsdir}/kompare.desktop
%{_kde_appsdir}/kompare
%{_kde_iconsdir}/hicolor/128x128/apps/kompare.png
%{_kde_iconsdir}/hicolor/16x16/apps/kompare.png
%{_kde_iconsdir}/hicolor/22x22/apps/kompare.png
%{_kde_iconsdir}/hicolor/32x32/apps/kompare.png
%{_kde_iconsdir}/hicolor/48x48/apps/kompare.png
%{_kde_iconsdir}/hicolor/scalable/apps/kompare.svgz
%{_kde_services}/komparenavtreepart.desktop
%{_kde_services}/komparepart.desktop
%{_kde_servicetypes}/kompareviewpart.desktop
%{_kde_servicetypes}/komparenavigationpart.desktop
%{_kde_docdir}/*/*/kompare

#---------------------------------------------------------------

%define  komparediff2_major 4
%define  libkomparediff2 %mklibname komparediff2_ %{komparediff2_major}

%package -n %{libkomparediff2}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkomparediff2}
KDE 4 core library.

%files -n %{libkomparediff2}
%{_kde_libdir}/libkomparediff2.so.%{komparediff2_major}*

#---------------------------------------------------------------

%define  komparedialogpages_major 4
%define  libkomparedialogpages %mklibname komparedialogpages %{komparedialogpages_major}

%package -n %{libkomparedialogpages}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkomparedialogpages}
KDE 4 core library.

%files -n %{libkomparedialogpages}
%{_kde_libdir}/libkomparedialogpages.so.%{komparedialogpages_major}*

#---------------------------------------------------------------

%define kompareinterface_major 4
%define libkompareinterface %mklibname kompareinterface %{kompareinterface_major}

%package -n %{libkompareinterface}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkompareinterface}
KDE 4 core library.

%files -n %{libkompareinterface}
%{_kde_libdir}/libkompareinterface.so.%{kompareinterface_major}*

#---------------------------------------------------------------

%package -n kmtrace
Summary:	Memory Allocation Debugging Tool
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}

%description -n kmtrace
Memory Allocation Debugging Tool

%files -n kmtrace
%{_kde_bindir}/kmtrace
%{_kde_bindir}/demangle
%{_kde_bindir}/kminspector
%{_kde_bindir}/kmmatch
%{_kde_appsdir}/kmtrace

#---------------------------------------------------------------

%package -n kcachegrind
Summary:	KCachegrind
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	valgrind

%description -n kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by 
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%files -n kcachegrind
%{_kde_bindir}/kcachegrind
%{_kde_bindir}/dprof2calltree
%{_kde_bindir}/hotshot2calltree
%{_kde_bindir}/memprof2calltree
%{_kde_bindir}/op2calltree
%{_kde_bindir}/pprof2calltree
%{_kde_iconsdir}/*/*/*/kcachegrind*
%{_kde_appsdir}/kcachegrind
%{_kde_datadir}/applications/kde4/kcachegrind.desktop
%{_kde_docdir}/*/*/kcachegrind

#---------------------------------------------------------------

%package -n kde-thumbnailer-po
Summary:	KDE4 preview image generator plugin for gettext translations and templates
Group:		Graphical desktop/KDE
Requires:	%{name}-core = %{EVRD}
Requires:	gettext

%description -n kde-thumbnailer-po
KDE-thumbnailer-po is a preview image generator plugin for gettext
translations and templates.

%files -n kde-thumbnailer-po
%{_kde_libdir}/kde4/pothumbnail.so
%{_kde_datadir}/config.kcfg/pocreatorsettings.kcfg
%{_kde_services}/pothumbnail.desktop

#---------------------------------------------------------------

%define ktrace_major 4
%define libktrace %mklibname ktrace %{ktrace_major}

%package -n %{libktrace}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libktrace}
KDE 4 core library.

%files -n %{libktrace}
%{_kde_libdir}/libktrace.so.%{ktrace_major}*

#---------------------------------------------------------------

%define kasten2controllers_major 2
%define libkasten2controllers %mklibname kasten2controllers %{kasten2controllers_major}

%package -n %{libkasten2controllers}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1controllers 0} < %{EVRD}

%description -n %{libkasten2controllers}
KDE 4 core library.

%files -n %{libkasten2controllers}
%{_kde_libdir}/libkasten2controllers.so.%{kasten2controllers_major}
%{_kde_libdir}/libkasten2controllers.so.0.*

#---------------------------------------------------------------

%define kasten2core_major 2
%define libkasten2core %mklibname kasten2core %{kasten2core_major}

%package -n %{libkasten2core}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1core 0} < %{EVRD}

%description -n %{libkasten2core}
KDE 4 core library.

%files -n %{libkasten2core}
%{_kde_libdir}/libkasten2core.so.%{kasten2core_major}
%{_kde_libdir}/libkasten2core.so.0.*

#---------------------------------------------------------------

%define kasten2gui_major 2
%define libkasten2gui %mklibname kasten2gui %{kasten2gui_major}

%package -n %{libkasten2gui}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1gui 0} < %{EVRD}

%description -n %{libkasten2gui}
KDE 4 core library.

%files -n %{libkasten2gui}
%{_kde_libdir}/libkasten2gui.so.%{kasten2gui_major}
%{_kde_libdir}/libkasten2gui.so.0.*

#---------------------------------------------------------------

%define kasten2okteta1controllers_major 1
%define libkasten2okteta1controllers %mklibname kasten2okteta1controllers %{kasten2okteta1controllers_major}

%package -n %{libkasten2okteta1controllers}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1controllers 0} < %{EVRD}

%description -n %{libkasten2okteta1controllers}
KDE 4 core library.

%files -n %{libkasten2okteta1controllers}
%{_kde_libdir}/libkasten2okteta1controllers.so.%{kasten2okteta1controllers_major}
%{_kde_libdir}/libkasten2okteta1controllers.so.0.*

#---------------------------------------------------------------

%define kasten2okteta1core_major 1
%define libkasten2okteta1core %mklibname kasten2okteta1core %{kasten2okteta1core_major}

%package -n %{libkasten2okteta1core}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1core 0} < %{EVRD}

%description -n %{libkasten2okteta1core}
KDE 4 core library.

%files -n %{libkasten2okteta1core}
%{_kde_libdir}/libkasten2okteta1core.so.%{kasten2okteta1core_major}
%{_kde_libdir}/libkasten2okteta1core.so.0.*

#---------------------------------------------------------------

%define kasten2okteta1gui_major 1
%define libkasten2okteta1gui %mklibname kasten2okteta1gui %{kasten2okteta1gui_major}

%package -n %{libkasten2okteta1gui}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1gui 0} < %{EVRD}

%description -n %{libkasten2okteta1gui}
KDE 4 core library.

%files -n %{libkasten2okteta1gui}
%{_kde_libdir}/libkasten2okteta1gui.so.%{kasten2okteta1gui_major}
%{_kde_libdir}/libkasten2okteta1gui.so.0.*

#---------------------------------------------------------------

%define okteta1core_major 1
%define libokteta1core %mklibname okteta1core %{okteta1core_major}

%package -n %{libokteta1core}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1core 0} < %{EVRD}

%description -n %{libokteta1core}
KDE 4 core library.

%files -n %{libokteta1core}
%{_kde_libdir}/libokteta1core.so.%{okteta1core_major}
%{_kde_libdir}/libokteta1core.so.0.*

#---------------------------------------------------------------

%define okteta1gui_major 1
%define libokteta1gui %mklibname okteta1gui %{okteta1gui_major}

%package -n %{libokteta1gui}
Summary:	KDE 4 core library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1gui 0} < %{EVRD}

%description -n %{libokteta1gui}
KDE 4 core library.

%files -n %{libokteta1gui}
%{_kde_libdir}/libokteta1gui.so.%{okteta1gui_major}
%{_kde_libdir}/libokteta1gui.so.0.*

#-----------------------------------------------------------------------------

%package devel
Summary:	Header files for kdesdk
Group:		Development/KDE and Qt
Requires:	%{libkomparediff2} = %{EVRD}
Requires:	%{libkomparedialogpages} = %{EVRD}
Requires:	%{libkompareinterface} = %{EVRD}
Requires:	%{libktrace} = %{EVRD}
Requires:	%{libkasten2controllers} = %{EVRD}
Requires:	%{libkasten2core} = %{EVRD}
Requires:	%{libkasten2gui} = %{EVRD}
Requires:	%{libkasten2okteta1controllers} = %{EVRD}
Requires:	%{libkasten2okteta1core} = %{EVRD}
Requires:	%{libkasten2okteta1gui} = %{EVRD}
Requires:	%{libokteta1core} = %{EVRD}
Requires:	%{libokteta1gui} = %{EVRD}

%description devel
This package includes the header files you will need to compile
applications for kdesdk.

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/libktrace.so
%{_kde_libdir}/libkompareinterface.so
%{_kde_libdir}/libkomparediff2.so
%{_kde_libdir}/libkomparedialogpages.so
%{_kde_libdir}/libkasten2controllers.so
%{_kde_libdir}/libkasten2core.so
%{_kde_libdir}/libkasten2gui.so
%{_kde_libdir}/libkasten2okteta1controllers.so
%{_kde_libdir}/libkasten2okteta1core.so
%{_kde_libdir}/libkasten2okteta1gui.so
%{_kde_libdir}/libokteta1core.so
%{_kde_libdir}/libokteta1gui.so
%{_kde_libdir}/kde4/plugins/designer/oktetadesignerplugin.so
%{_datadir}/dbus-1/interfaces/*

#---------------------------------------------------------------

%prep
%setup -q -n kdesdk-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

# Copy all scripts
mkdir -p %{buildroot}%{_kde_appsdir}/kdesdk/
cp -a scripts %{buildroot}%{_kde_appsdir}/kdesdk/
rm -f %{buildroot}%{_kde_appsdir}/kdesdk/CMake*

# (nl) Prefer the file from colorsvn as it is more up to date
# and this fix a conflict between kdesdk4-scripts and colorsvn
rm -f %{buildroot}%{_kde_bindir}/colorsvn

%changelog
* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Wed Aug 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0
- Add rpmlintrc file

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97
- Make better usage of KDE path macros

* Fri Jun 29 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95
- Add gettext-devel to BuildRequires
- New subpackage kde-thumbnailer-po
- Update file list
- Fix library majors

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- extractqml is no longer packaged, remove it from the file list
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 762520
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762520
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758109
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 750418
- New version

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 744310
- Fix file list
- New upstream tarball
- Remove dupplicate file
- New version 4.7.80
- Remove kate
- Remove old rpm stuffs
- New version 4.7.41
- Remove branch switch

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-2
+ Revision: 684410
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-2
+ Revision: 674035
- new version 4.6.3

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1:4.6.2-2
+ Revision: 655776
- add upstream patch to detect hunspell 1.3
- rebuild for new hunspell

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650781
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-1
+ Revision: 640733
- New version 4.6.1

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-1
+ Revision: 632970
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629126
- New version KDE 4.6 RC2

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 1:4.5.90-1mdv2011.0
+ Revision: 624709
- update file list
- md5deep is not that requires (there is no runtime hard dependency in source)
- move man pages into correct sub package

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball
    - Add a require for md5deep
      CCBUG: 61903

* Sun Dec 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-2mdv2011.0
+ Revision: 620603
- Fix file list
- Fix file list
- New upstream tarball

* Thu Dec 02 2010 Paulo Andrade <pcpa@mandriva.com.br> 1:4.5.80-2mdv2011.0
+ Revision: 604633
- Rebuild with apr with workaround to gcc strict aliasing issue

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601485
- new version 4.5.80 (aka 4.6 beta1)
- modify libname according to our libname policy

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599133
- new snapshot 4.5.77

* Sun Nov 14 2010 Funda Wang <fwang@mandriva.org> 1:4.5.76-0.svn1196628.1mdv2011.0
+ Revision: 597479
- BR binutils
- new snapshot 4.5.76
- byebye kbugbuster

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 591269
- update file list
- update file list
- new snapshot 4.5.74

* Sun Oct 17 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1183784.2mdv2011.0
+ Revision: 586233
- add antlr as BR

* Fri Oct 08 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1183784.1mdv2011.0
+ Revision: 584250
- kdeworkspace and kdepim have nothing to do with kdesdk
- new snapshot 4.5.71

* Fri Sep 17 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 579174
- new snapshot 4.5.68

* Wed Sep 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:4.5.67-2mdv2011.0
+ Revision: 576825
- rebuild with latest hunspell to fix a buffer overflow

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-1mdv2011.0
+ Revision: 576693
- LOL
- Fix file list
- New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566574
- New upstream tarball
- Update to version 4.5.0

* Thu Jul 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562943
- Add BR
- kde 4.4.95

* Thu May 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-5mdv2010.1
+ Revision: 546332
- Add branch patch to fix kate crash

* Sat May 08 2010 Colin Guthrie <cguthrie@mandriva.org> 1:4.4.3-4mdv2010.1
+ Revision: 543582
- Fix kate crash when closing files

* Sat May 08 2010 Funda Wang <fwang@mandriva.org> 1:4.4.3-3mdv2010.1
+ Revision: 543561
- add missing requires on libfile

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Requires
      CCBUG: 59007

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542108
- Update to version 4.4.3

* Fri Apr 02 2010 Funda Wang <fwang@mandriva.org> 1:4.4.2-1mdv2010.1
+ Revision: 530758
- update filelist

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to version 4.4.2
    - Convert Requires into suggests on the metapackage

* Thu Mar 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-2mdv2010.1
+ Revision: 524906
- Install konsole when using kate for the konsole part

* Thu Mar 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 517963
- Really fix file list
- Fix file list
- Fix release
- Update to version 4.4.1

* Thu Feb 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-3mdv2010.1
+ Revision: 504315
- Fix crash in lokalize with wrong files (Bug #57582)

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-1mdv2010.1
+ Revision: 502617
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498948
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 496466
- Fix version
- Update to version 4.3.95 aka "kde 4.4 RC2"

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488565
- Update to kde 4.4 rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480755
- Update to kde 4.4 beta2

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-1mdv2010.1
+ Revision: 473349
- Update to KDE 4.4 Beta1

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-1mdv2010.1
+ Revision: 470799
- Update to kde 4.3.77

* Thu Nov 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.75-1mdv2010.1
+ Revision: 467385
- Remove typo
- Fix %%libktexteditor_codesnippets_core major
- Fix file list
- Update to kde 4.3.75

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-2mdv2010.1
+ Revision: 465255
- Rebuild against new Qt

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 1:4.3.73-1mdv2010.1
+ Revision: 463283
- add BR

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to kde 4.3.73
      Fix file list
    - Suggests python-translate

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454664
- New upstream release 4.3.2.

* Sun Sep 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 438580
- Obsolete kde3 packages

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423219
- New upstream release 4.3.1.

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-1mdv2010.0
+ Revision: 409513
- New upstream release 4.3.0.
- Update to KDE 4.3 RC3

* Sun Jul 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.96-1mdv2010.0
+ Revision: 394960
- Update to Rc2

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389560
- Update to KDE 4.3 Rc1

* Fri Jun 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 382950
- Update to beta2

* Sat May 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.88-1mdv2010.0
+ Revision: 381535
- Update to kde 4.2.88
- Adapt kdesdk to new layout

* Sat May 23 2009 Funda Wang <fwang@mandriva.org> 1:4.2.87-1mdv2010.0
+ Revision: 378892
- New version 4.2.87

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Requires on the lokalize package

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-2mdv2010.0
+ Revision: 373894
- Move some cervisia files into the core package to avoid some automatic deps

* Sat May 09 2009 Funda Wang <fwang@mandriva.org> 1:4.2.85-1mdv2010.0
+ Revision: 373680
- New version 4.2.85

* Wed May 06 2009 Funda Wang <fwang@mandriva.org> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 372605
- New versino 4.2.71
- use kde macros

* Fri Apr 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-4mdv2009.1
+ Revision: 365553
- Fix requires on kdesdk4-strigi-analyzer

* Thu Apr 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-3mdv2009.1
+ Revision: 365474
- Fix Requires (Bug #49582)

* Fri Mar 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-2mdv2009.1
+ Revision: 361757
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with 4.2.2 try#1 packages

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 346213
- KDE 4.2.1 try#1 upstream release

* Wed Feb 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-3mdv2009.1
+ Revision: 342615
- Fix file list

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-2mdv2009.1
+ Revision: 340891
- Rebuild against qt4.5

* Wed Jan 28 2009 Funda Wang <fwang@mandriva.org> 1:4.2.0-1mdv2009.1
+ Revision: 334913
- fix file list
- New version 4.2.0

* Wed Jan 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-2mdv2009.1
+ Revision: 332331
- Fix file list
- Add an upstream patch to fix the build against the new boost

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-1mdv2009.1
+ Revision: 314062
- Fix File list
- New version KDE 4.2 Beta2

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-1mdv2009.1
+ Revision: 313487
- Update to kde 4.1.82

* Mon Dec 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.81-1mdv2009.1
+ Revision: 308866
- Update to kde 4.1.81

* Wed Nov 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304563
- Update with Beta 1 - 4.1.80

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 303436
- Update to kde 4.1.73

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-1mdv2009.1
+ Revision: 297138
- Fix file list
- Fix file list
- New version 4.1.71
- Fix Requires

  + Funda Wang <fwang@mandriva.org>
    - update file list
    - New version 4.1.70

* Sat Sep 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288846
- KDE 4.1.2 arriving.

* Sun Aug 31 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-1mdv2009.0
+ Revision: 277828
- Upgrade to forthcoming 4.1.1 packages

* Tue Jul 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 252439
- Update with Release Candidate 1 - 4.1.0
- Update with Release Candidate 1 - 4.0.98

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232548
- New version kde 4.0.85
- Use default kate behaviour

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.84-1mdv2009.0
+ Revision: 229406
- Update with new snapshot tarballs 4.0.84

* Tue Jun 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.83-4mdv2009.0
+ Revision: 228498
- [BUGFIX] Fix name of lokalize package ( it was wrongly called localize ) (Bug #41637) ( thanks to JLP )
  Fix Description and summary too ( thanks to JLP )
- Rebuild against fixed rpm

* Sun Jun 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.83-2mdv2009.0
+ Revision: 227845
- [BUGFIX] Fix use of multiple instances in kate (Bug #41365)

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-1mdv2009.0
+ Revision: 226103
- Update with new snapshot tarballs 4.0.83

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-2mdv2009.0
+ Revision: 218302
- Update with new snapshot tarballs 4.0.82
- Update with new snapshot tarballs 4.0.81

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-2mdv2009.0
+ Revision: 211536
- Conflicts against old kdevelop4

* Mon May 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-1mdv2009.0
+ Revision: 211453
- Fix file list
- Own %%{_kde_appsdir}/kmtrace
- Own %%{_kde_appsdir}/kompare
- Own %%{_kde_appsdir}/kuiviewer
- Own %%{_kde_appsdir}/lokalize

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 beta1

* Sun May 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-2mdv2009.0
+ Revision: 208768
- [BUGFIX] Fix conflicts with colorsvn (Bug #40909)

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1:4.0.74-1mdv2009.0
+ Revision: 208076
- New version 4.0.74

* Sun May 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-5mdv2009.0
+ Revision: 205937
- Bump release
- Fix more conflicts
- Fix conflicts
- Rebuild because of BS failure
- Update to kde 4.0.73

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-1mdv2009.0
+ Revision: 202804
- Add boost-devel as BuildRequires
- Remove patch not needed
- Update to kde 4.0.72
- Fix Requires
- Fix Require and lib name
- Add new package Localize , libkomparediff2 and libkomparedialogpages
- New snapshot 4.0.70

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1

* Sun Mar 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 191157
- Fix release

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update for last stable release 4.0.3

* Tue Mar 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-3mdv2008.1
+ Revision: 190096
- Fix obsoletes

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 182265
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177448
- New upstream bugfix release 4.0.2

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1:4.0.1-2mdv2008.1
+ Revision: 170921
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix BuildRequires

* Tue Feb 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 166287
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE team

* Sun Feb 03 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-3mdv2008.1
+ Revision: 161802
- Fix name of the kdesdk4-scripts package

* Sat Jan 12 2008 Anssi Hannula <anssi@mandriva.org> 1:4.0.0-2mdv2008.1
+ Revision: 149660
- fix versioning of obsoletes
- ensure major correctness

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 147321
- Update for final stable 4.0.0

  + Funda Wang <fwang@mandriva.org>
    - single out po2xml and related progs

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.752225.1mdv2008.1
+ Revision: 137578
- New snapshot
  Kompare is back for christmas
  libkompareinterface is now on the package too

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.746591.1mdv2008.1
+ Revision: 117709
- New snapshot
  Big clean up
        - Creation of core package
        - Creation of Kbugbuster package
        - Creation of scripts package
        - Creation of kuiviewer package
        - Creation of kmtrace package
        - Creation of kcachegrind package
        - Creation of libantlr libkateinterfaces  libkstartperf and libktrace4
        - Removal of libkdesdk41-kate and libkdesdk41-cervisia
        - All Devel files have been merged in kdesdk4-devel

* Fri Nov 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740308.1mdv2008.1
+ Revision: 111565
- New snapshot

* Sat Nov 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.0-0.737044.1mdv2008.1
+ Revision: 109672
- KDE4 RC1
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.730863.1mdv2008.1
+ Revision: 103698
- New snashot

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.729243.1mdv2008.1
+ Revision: 102093
- New snapshot
- New snapshot

* Sat Oct 20 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.727179.1mdv2008.1
+ Revision: 100590
- Kde 4 Beta 3

* Wed Sep 26 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.93.0-0.714320.1mdv2008.0
+ Revision: 93009
- new snapshot from KDE svn
- spec cleanup

  + Laurent Montel <lmontel@mandriva.org>
    - it compiles with enable final
    - new snapshot
    - new snapshot


* Fri Mar 02 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070228.6mdv2007.0
+ Revision: 130938
- s/kdebase/kdebase4

* Thu Mar 01 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.3-0.20070228.5mdv2007.1
+ Revision: 130474
- Fix obsolete provides
- new snapshot
- 3.80.3
- new snapshot
- Fix spec file
- new snapshot
- new snapshot

* Thu Jan 18 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070117.4mdv2007.1
+ Revision: 110423
- updtae

* Sat Jan 13 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.4mdv2007.1
+ Revision: 108183
- Fix buildrequires (need to compile kcal plugins)

* Wed Jan 10 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.3mdv2007.1
+ Revision: 107029
- a
- Update

* Thu Jan 04 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.2mdv2007.1
+ Revision: 104043
- Update

* Fri Dec 29 2006 Laurent Montel <lmontel@mandriva.com> 1:3.80-2mdv2007.1
+ Revision: 102535
- Fix buildrequires
- Import kdesdk4

* Wed Dec 27 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-5mdv2007.0
- kde 4.0


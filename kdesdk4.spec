%define branch_date 20070418

%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname kdesdk4 %lib_major
# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/
%define _mandir %_prefix/man/

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


Name: 		kdesdk4
Summary: 	K Desktop Environment - Software Development Kit
Version: 	3.80.3
Release: 	%mkrel 0.%branch_date.6
Epoch: 1
License:	GPL
URL: 		ftp://ftp.kde.org/pub/kde/stable/%version/src/
%if %branch
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%version-%branch_date.tar.bz2
%else
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdesdk-%version.tar.bz2
%endif
Group: 		Graphical desktop/KDE
Packager:	Mandriva Linux KDE Team <kde@mandriva.com>
BuildRoot: 	%_tmppath/%name-%version-%release-root
Requires: cvs
BuildRequires: db4-devel 
BuildRequires: freetype2-devel
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires: kdepimlibs4-devel >= %version-%mini_release
BuildRequires: kdepim4-devel 
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
%_bindir/*
%_iconsdir/*/*/*/kuiviewer*
%_iconsdir/*/*/*/kbugbuster*
%_datadir/apps/katepart/syntax/kdesvn-buildrc.xml
%_libdir/kde4/*
%_datadir/applications/kde4/kbugbuster.desktop
%_datadir/applications/kde4/kuiviewer.desktop
%dir %_datadir/apps/kbugbuster
%_datadir/apps/kbugbuster/*
%dir %_datadir/apps/kapptemplate/
%_datadir/apps/kapptemplate/*
%dir %_datadir/apps/kuiviewer/
%_datadir/apps/kuiviewer/*
%dir %_datadir/apps/kuiviewerpart/
%_datadir/apps/kuiviewerpart/*
%_datadir/servicetypes/*
%_datadir/apps/kmtrace/kde.excludes
%_datadir/apps/kabc/*
%_datadir/services/*
%exclude %_bindir/kbabel
%exclude %_bindir/kbabeldict
%exclude %_bindir/catalogmanager
%exclude %_bindir/kcachegrind
%exclude %_libdir/kde4/kbabel*
%exclude %_libdir/kde4/kfile_po*
%exclude %_libdir/kde4/pothumbnail*
%exclude %_bindir/umbrello
%exclude %_datadir/services/kbabel_*.desktop
%exclude %_datadir/services/po*.desktop
%exclude %_datadir/services/dbsea*.desktop
%exclude %_datadir/services/kfile_po.desktop
%exclude %_datadir/services/tmx*.desktop
%exclude %_datadir/servicetypes/kbabel*.desktop
%_iconsdir/crystalsvg/16x16/actions/svn_add.png
%_iconsdir/crystalsvg/16x16/actions/svn_branch.png
%_iconsdir/crystalsvg/16x16/actions/svn_merge.png
%_iconsdir/crystalsvg/16x16/actions/svn_remove.png
%_iconsdir/crystalsvg/16x16/actions/svn_status.png
%_iconsdir/crystalsvg/16x16/actions/svn_switch.png
%_iconsdir/crystalsvg/22x22/actions/svn_add.png
%_iconsdir/crystalsvg/22x22/actions/svn_branch.png
%_iconsdir/crystalsvg/22x22/actions/svn_merge.png
%_iconsdir/crystalsvg/22x22/actions/svn_remove.png
%_iconsdir/crystalsvg/22x22/actions/svn_status.png
%_iconsdir/crystalsvg/22x22/actions/svn_switch.png
%_iconsdir/crystalsvg/32x32/actions/svn_add.png
%_iconsdir/crystalsvg/32x32/actions/svn_branch.png
%_iconsdir/crystalsvg/32x32/actions/svn_merge.png
%_iconsdir/crystalsvg/32x32/actions/svn_remove.png
%_iconsdir/crystalsvg/32x32/actions/svn_status.png
%_iconsdir/crystalsvg/32x32/actions/svn_switch.png
%_iconsdir/crystalsvg/48x48/actions/svn_add.png
%_iconsdir/crystalsvg/48x48/actions/svn_branch.png
%_iconsdir/crystalsvg/48x48/actions/svn_merge.png
%_iconsdir/crystalsvg/48x48/actions/svn_remove.png
%_iconsdir/crystalsvg/48x48/actions/svn_status.png
%_iconsdir/crystalsvg/48x48/actions/svn_switch.png
%_iconsdir/crystalsvg/64x64/actions/svn_add.png
%_iconsdir/crystalsvg/64x64/actions/svn_branch.png
%_iconsdir/crystalsvg/64x64/actions/svn_merge.png
%_iconsdir/crystalsvg/64x64/actions/svn_remove.png
%_iconsdir/crystalsvg/64x64/actions/svn_status.png
%_iconsdir/crystalsvg/64x64/actions/svn_switch.png
%_iconsdir/crystalsvg/scalable/actions/svn_add.svgz
%_iconsdir/crystalsvg/scalable/actions/svn_branch.svgz
%_iconsdir/crystalsvg/scalable/actions/svn_merge.svgz
%_iconsdir/crystalsvg/scalable/actions/svn_remove.svgz
%_iconsdir/crystalsvg/scalable/actions/svn_status.svgz
%_iconsdir/crystalsvg/scalable/actions/svn_switch.svgz
%_datadir/apps/konqueror/servicemenus/subversion.desktop
%_datadir/apps/konqueror/servicemenus/subversion_toplevel.desktop
%_datadir/icons/crystalsvg/128x128/actions/svn_add.png
%_datadir/icons/crystalsvg/128x128/actions/svn_branch.png
%_datadir/icons/crystalsvg/128x128/actions/svn_merge.png
%_datadir/icons/crystalsvg/128x128/actions/svn_remove.png
%_datadir/icons/crystalsvg/128x128/actions/svn_status.png
%_datadir/icons/crystalsvg/128x128/actions/svn_switch.png

%doc %_docdir/HTML/en/kdesvn-build/*.docbook
%doc %_docdir/HTML/en/kdesvn-build/index.cache.bz2

%doc %_docdir/HTML/en/kbugbuster/*.bz2
%doc %_docdir/HTML/en/kbugbuster/*.docbook


%package kate
Summary:        Kate
Group:          Graphical desktop/KDE
Requires:       %lib_name-kate = %epoch:%version-%release
Provides:       kate4
Obsoletes:	kdebase4-kate <= 1:3.80.2
Provides:	kdebase4-kate > 1:3.80.2
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kate
A fast and advanced text editor with nice plugins

%post kate
%update_menus
%if %mdkversion > 200600
%{update_desktop_database}
%update_icon_cache crystalsvg
%endif

%postun kate
%clean_menus
%if %mdkversion > 200600
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%endif

%files kate
%defattr(-,root,root)
%_datadir/applications/kde4/kate.desktop
%_datadir/apps/kate/externaltools
%_datadir/apps/kate/icons/crystalsvg/16x16/actions/curfiledir.png
%_datadir/apps/kate/icons/crystalsvg/16x16/actions/highlighting.png
%_datadir/apps/kate/icons/crystalsvg/16x16/actions/modified.png
%_datadir/apps/kate/icons/crystalsvg/16x16/actions/modmod.png
%_datadir/apps/kate/icons/crystalsvg/16x16/actions/modonhd.png
%_datadir/apps/kate/icons/crystalsvg/16x16/actions/null.png
%_datadir/apps/kate/icons/crystalsvg/32x32/actions/highlighting.png
%_datadir/apps/kate/icons/locolor/16x16/actions/curfiledir.png
%_datadir/apps/kate/icons/locolor/16x16/actions/indent.png
%_datadir/apps/kate/icons/locolor/16x16/actions/modified.png
%_datadir/apps/kate/icons/locolor/16x16/actions/modmod.png
%_datadir/apps/kate/icons/locolor/16x16/actions/modonhd.png
%_datadir/apps/kate/icons/locolor/16x16/actions/null.png
%_datadir/apps/kate/icons/locolor/16x16/actions/unindent.png
%_datadir/apps/kate/icons/locolor/22x22/actions/indent.png
%_datadir/apps/kate/icons/locolor/22x22/actions/unindent.png
%_datadir/apps/kate/kateui.rc
%_datadir/apps/kate/pics/sessionchooser.png
%_datadir/apps/kate/plugins/kateexternaltools/ui.rc
%_datadir/apps/kate/plugins/katekonsole/ui.rc
%_datadir/apps/kate/plugins/katemailfiles/ui.rc
%_datadir/apps/kate/plugins/katesymbolviewer/ui.rc
%_datadir/apps/kate/plugins/katetabbarextension/ui.rc
%_datadir/apps/kate/tips
%_datadir/apps/kconf_update/kate-2.4.upd
%_datadir/config/katerc
%doc %_docdir/HTML/en/kate-plugins/*.png
%doc %_docdir/HTML/en/kate-plugins/*.bz2
%doc %_docdir/HTML/en/kate-plugins/*.docbook
%doc %_docdir/HTML/en/kate/*.png
%doc %_docdir/HTML/en/kate/*.bz2
%doc %_docdir/HTML/en/kate/*.docbook
%_datadir/icons/hicolor/128x128/apps/kate.png
%_datadir/icons/hicolor/128x128/apps/kwrite.png
%_datadir/icons/hicolor/16x16/apps/kate.png
%_datadir/icons/hicolor/16x16/apps/kwrite.png
%_datadir/icons/hicolor/22x22/apps/kate.png
%_datadir/icons/hicolor/22x22/apps/kwrite.png
%_datadir/icons/hicolor/32x32/apps/kate.png
%_datadir/icons/hicolor/32x32/apps/kwrite.png
%_datadir/icons/hicolor/48x48/apps/kate.png
%_datadir/icons/hicolor/48x48/apps/kwrite.png
%_datadir/icons/hicolor/64x64/apps/kate.png
%_datadir/icons/hicolor/64x64/apps/kwrite.png
%_datadir/icons/hicolor/scalable/apps/kate2.svgz
%_datadir/icons/hicolor/scalable/apps/kwrite2.svgz


%package -n %lib_name-kate
Summary:        Libraries for Kate
Group:          Graphical desktop/KDE
%define kdebase_lib_name %mklibname kdebase4 6
Obsoletes:      %kdebase_lib_name-kate <= 1:3.80.2
Provides:       %kdebase_lib_name-kate > 1:3.80.2


%description -n %lib_name-kate
Libraries for kate program

%post -n %lib_name-kate -p /sbin/ldconfig
%postun -n %lib_name-kate -p /sbin/ldconfig

%files -n %lib_name-kate
%defattr(-,root,root)
%_libdir/libkateinterfaces.so.*
%_libdir/libkdeinit_kate.so

%package -n %lib_name-kate-devel
Summary:        Development file for Kate
Group:          Development/KDE and Qt
Requires:       %lib_name-kate = %epoch:%version-%release
%define kdebase_lib_name %mklibname kdebase4 6
Obsoletes:      %kdebase_lib_name-kate-devel <= 1:3.80.2
Provides:       %kdebase_lib_name-kate-devel > 1:3.80.2


%description -n %lib_name-kate-devel
Development file for kate program

%files -n %lib_name-kate-devel
%defattr(-,root,root)
%_libdir/libkateinterfaces.so

#---------------------------------------------------------------

%package -n %lib_name-devel
Summary:        Header files for kdesdk
Group:		Development/KDE and Qt
Requires:	%lib_name = %epoch:%version-%release
Provides:	kdesdk4-devel =  %epoch:%version-%release
Provides:   %lib_name_orig-devel = %epoch:%version-%release


%description -n %lib_name-devel	
This package includes the header files you will need to compile
applications for kdesdk.

%files -n %lib_name-devel
%defattr(-,root,root,-)
%_includedir/kprofilemethod.h
%_includedir/ktrace.h
%_datadir/dbus-1/interfaces/org.kde.kbabel.kbabel.xml
%_datadir/dbus-1/interfaces/org.kde.kbabel.kbabeldict.xml
%_datadir/dbus-1/interfaces/org.kde.kbabel.catalogmanager.xml
%_libdir/libktrace.so
%_libdir/libkstartperf.so

#---------------------------------------------------------------

%package -n %lib_name
Summary:        Lib files for kdesdk
Group:		Graphical desktop/KDE
Conflicts:      %lib_name-kbabel <= 3.3.2-1mdk
 
%description -n %lib_name
Lib files for kdesdk

%post -n %lib_name -p /sbin/ldconfig
%postun -n %lib_name -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root,-)
%_libdir/libktrace.so.*
%_libdir/libkstartperf.so.*
#---------------------------------------------------------------

%package umbrello
Summary:    UML Modeller
Group:      Graphical desktop/KDE
Provides:	umbrello4

%description umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%files umbrello
%defattr(-,root,root,-)
%_bindir/umbrello
%_datadir/applications/kde4/umbrello.desktop
%dir %_datadir/apps/umbrello/
%_datadir/apps/umbrello/*
%_iconsdir/*/*/*/umbrello*
%_datadir/mimelnk/application/x-umbrello.desktop

%doc %_docdir/HTML/en/umbrello/*.png
%doc %_docdir/HTML/en/umbrello/*.bz2
%doc %_docdir/HTML/en/umbrello/*.docbook

#---------------------------------------------------------------

%package cervisia
Summary:    CVS client part
Group:      Graphical desktop/KDE
Provides:	cervisia4 = %epoch:%version-%release
Requires:	%lib_name-cervisia = %epoch:%version-%release
Requires:	cvs

%description cervisia
CVS client part.

%files cervisia
%defattr(-,root,root,-)
%_datadir/applications/kde4/cervisia.desktop
%_datadir/apps/cervisia/cervisia.notifyrc
%_datadir/apps/cervisia/cervisiashellui.rc
%_datadir/apps/cervisiapart/cervisiaui.rc
%_datadir/apps/kconf_update/cervisia-change_repos_list.pl
%_datadir/apps/kconf_update/cervisia-normalize_cvsroot.pl
%_datadir/apps/kconf_update/cervisia.upd
%_datadir/apps/kconf_update/change_colors.pl
%_datadir/config.kcfg/cervisiapart.kcfg
%_datadir/icons/crystalsvg/16x16/actions/vcs_add.png
%_datadir/icons/crystalsvg/16x16/actions/vcs_commit.png
%_datadir/icons/crystalsvg/16x16/actions/vcs_diff.png
%_datadir/icons/crystalsvg/16x16/actions/vcs_remove.png
%_datadir/icons/crystalsvg/16x16/actions/vcs_status.png
%_datadir/icons/crystalsvg/16x16/actions/vcs_update.png
%_datadir/icons/crystalsvg/22x22/actions/vcs_add.png
%_datadir/icons/crystalsvg/22x22/actions/vcs_commit.png
%_datadir/icons/crystalsvg/22x22/actions/vcs_diff.png
%_datadir/icons/crystalsvg/22x22/actions/vcs_remove.png
%_datadir/icons/crystalsvg/22x22/actions/vcs_status.png
%_datadir/icons/crystalsvg/22x22/actions/vcs_update.png
%_datadir/icons/crystalsvg/32x32/actions/vcs_add.png
%_datadir/icons/crystalsvg/32x32/actions/vcs_commit.png
%_datadir/icons/crystalsvg/32x32/actions/vcs_diff.png
%_datadir/icons/crystalsvg/32x32/actions/vcs_remove.png
%_datadir/icons/crystalsvg/32x32/actions/vcs_status.png
%_datadir/icons/crystalsvg/32x32/actions/vcs_update.png
%_datadir/icons/crystalsvg/48x48/actions/vcs_add.png
%_datadir/icons/crystalsvg/48x48/actions/vcs_commit.png
%_datadir/icons/crystalsvg/48x48/actions/vcs_diff.png
%_datadir/icons/crystalsvg/48x48/actions/vcs_remove.png
%_datadir/icons/crystalsvg/48x48/actions/vcs_status.png
%_datadir/icons/crystalsvg/48x48/actions/vcs_update.png
%_datadir/icons/crystalsvg/scalable/actions/vcs_add.svgz
%_datadir/icons/crystalsvg/scalable/actions/vcs_commit.svgz
%_datadir/icons/crystalsvg/scalable/actions/vcs_diff.svgz
%_datadir/icons/crystalsvg/scalable/actions/vcs_remove.svgz
%_datadir/icons/crystalsvg/scalable/actions/vcs_status.svgz
%_datadir/icons/crystalsvg/scalable/actions/vcs_update.svgz
%_datadir/icons/hicolor/16x16/apps/cervisia.png
%_datadir/icons/hicolor/22x22/apps/cervisia.png
%_datadir/icons/hicolor/32x32/apps/cervisia.png
%_datadir/icons/hicolor/48x48/apps/cervisia.png

%doc %_docdir/HTML/en/cervisia/*.bz2
%doc %_docdir/HTML/en/cervisia/*.docbook
%doc %_docdir/HTML/en/cervisia/*.png
%_mandir/man1/cervisia.1

#---------------------------------------------------------------

%package kompare
Summary: kompare is a KDE diff graphic tool
Group:  Graphical desktop/KDE
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
Requires: valgrind-plugins
%endif

%description kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by 
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%files kcachegrind
%defattr(-,root,root,-)
%_bindir/kcachegrind
%_iconsdir/*/*/*/kcachegrind*
%dir %_datadir/apps/kcachegrind/
%_datadir/apps/kcachegrind/*
%_datadir/mimelnk/application/x-kcachegrind.desktop
%_datadir/applications/kde4/kcachegrind.desktop
%doc %_docdir/HTML/en/kcachegrind/*.bz2
%doc %_docdir/HTML/en/kcachegrind/*.docbook


#---------------------------------------------------------------

%package kbabel
Summary:    KBabel is a set of tools for editing and managing gettext PO files.
Group:      Graphical desktop/KDE
Provides:	kbabel4 = %epoch:%version-%release
Requires:	%lib_name-kbabel = %epoch:%version-%release
Requires:	gettext

%description kbabel
KBabel is a set of tools for editing and managing gettext PO files. 
Main part is a powerful and comfortable PO file editor which features 
full navigation capabilities, full editing functionality, possibility 
to search for translations in different dictionaries, spell and 
syntax checking, showing diffs and many more. Also included is a 
"Catalog Manager", a file manager view which helps keeping an overview 
of PO files. Last but not least it includes a standalone 
dictionary application as an additional possibility to access KBabel's 
powerful dictionaries. 
KBabel will help you to translate fast and also keep consistent translations.

%files kbabel
%defattr(-,root,root,-)
%_bindir/kbabel
%_bindir/kbabeldict
%_bindir/catalogmanager
%_datadir/applications/kde4/kbabel.desktop
%_datadir/applications/kde4/kbabeldict.desktop
%_datadir/applications/kde4/catalogmanager.desktop
%_iconsdir/*/*/*/catalogmanager*
%_iconsdir/*/*/*/kbabel*
%dir %_datadir/apps/kbabel
%_datadir/apps/kbabel/*
%_datadir/apps/kconf_update/kbabel-difftoproject.upd
%_datadir/apps/kconf_update/kbabel-project.upd
%_datadir/apps/kconf_update/kbabel-projectrename.upd
%_datadir/config.kcfg/kbabel.kcfg
%_datadir/config.kcfg/kbprojectsettings.kcfg
%dir %_datadir/apps/catalogmanager
%_datadir/apps/catalogmanager/*
%_datadir/services/kbabel_*.desktop
%_datadir/services/po*.desktop
%_datadir/services/dbsea*.desktop
%_datadir/services/kfile_po.desktop
%_datadir/services/tmx*.desktop
%_datadir/servicetypes/kbabel*.desktop

%doc %_docdir/HTML/en/kbabel/*.png
%doc %_docdir/HTML/en/kbabel/*.docbook
%doc %_docdir/HTML/en/kbabel/*.bz2

#---------------------------------------------------------------

%package -n %lib_name-kbabel-devel
Summary:    Devel files for KBabel.
Group:      Development/KDE and Qt
Requires:	%lib_name-kbabel = %epoch:%version-%release

%description -n %lib_name-kbabel-devel
Devel files for KBabel.

%files -n %lib_name-kbabel-devel
%defattr(-,root,root,-)
%_libdir/libkbabelcommon.so
%_libdir/libkbabeldictplugin.so
%_libdir/libkbabelcommonui.so
%_includedir/*.h
%_includedir/kbabel/*.h
#---------------------------------------------------------------

%package -n %lib_name-kbabel
Summary:    Library files for KBabel.
Group:      Graphical desktop/KDE

%description -n %lib_name-kbabel
Library files for KBabel.

%files -n %lib_name-kbabel
%defattr(-,root,root,-)
%_libdir/libkbabelcommon.so.*
%_libdir/libkbabeldictplugin.so.*
%_libdir/kde4/kbabel*.so
%_libdir/kde4/kfile_po.so
%_libdir/kde4/pothumbnail.so

%post  -n %lib_name-kbabel -p /sbin/ldconfig

%postun -n %lib_name-kbabel -p /sbin/ldconfig


#---------------------------------------------------------------

%package -n %lib_name-cervisia
Summary:    Library for CVS client part
Group:      Graphical desktop/KDE
Provides:   %lib_name_orig-cervisia = %epoch:%version-%release

%description -n %lib_name-cervisia
Library for CVS client part.

%post -n %lib_name-cervisia -p /sbin/ldconfig
%postun -n %lib_name-cervisia -p /sbin/ldconfig

%files -n %lib_name-cervisia
%defattr(-,root,root,-)
%_libdir/libkdeinit_cervisia.so
%_libdir/libkdeinit_cvsaskpass.so
%_libdir/libkdeinit_cvsservice.so

#---------------------------------------------------------------

%package -n %lib_name-cervisia-devel
Summary:    Devel files for CVS client part
Group:      Development/KDE and Qt
Requires:	%lib_name-cervisia = %epoch:%version-%release
Provides:      %{lib_name_orig}-cervisia-devel = %epoch:%version-%release
Provides:      %{name}-cervisia-devel = %epoch:%version-%release

%description -n %lib_name-cervisia-devel
Devel files for CVS client part.

%files -n %lib_name-cervisia-devel
%defattr(-,root,root,-)
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsjob.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsloginjob.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.cvsservice.xml
%_datadir/dbus-1/interfaces/org.kde.cervisia.repository.xml

#---------------------------------------------------------------

%prep
%setup -q -nkdesdk-%version-%branch_date

%build
cd $RPM_BUILD_DIR/kdesdk-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make



%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdesdk-%version-%branch_date
cd build

make DESTDIR=%buildroot install



# Create LMDK menu structure
install -d %buildroot/%_menudir/
# %%_datadir/applnk/Development/
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbabel.desktop "More Applications/Development/Tools" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbabeldict.desktop "More Applications/Development/Tools" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/catalogmanager.desktop "More Applications/Development/Tools" 
#mandriva-add-xdg-categories.pl kdesdk-cervisia "More Applications/Development/Tools" %buildroot/%_datadir/applications/kde/cervisia.desktop %buildroot/%_menudir/kdesdk-cervisia
#mandriva-add-xdg-categories.pl kdesdk "More Applications/Development/Tools" %buildroot/%_datadir/applications/kde/kompare.desktop %buildroot/%_menudir/kdesdk-kompare

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kbugbuster.desktop "More Applications/Development/Tools" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcachegrind.desktop "More Applications/Development/Tools" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/umbrello.desktop "More Applications/Development/Tools" 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kuiviewer.desktop "More Applications/Development/Tools" 

%clean
rm -fr %buildroot



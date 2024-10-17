Summary:	K Desktop Environment - Software Development Kit
Name:		kdesdk4
Version:	4.14.3
Release:	3
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Suggests:	cervisia
Suggests:	dolphin-plugins
Suggests:	lokalize
Suggests:	kapptemplate
Suggests:	kcachegrind
Suggests:	kde-dev-scripts
Suggests:	kde-dev-utils
Suggests:	kdesdk-kioslaves
Suggests:	kdesdk-strigi-analyzers
Suggests:	kdesdk-thumbnailers
Suggests:	kompare
Suggests:	okteta
Suggests:	poxml
Suggests:	umbrello
Obsoletes:	kdesdk4-core < 1:4.11.0
Obsoletes:	kdesdk4-devel < 1:4.11.0
BuildArch:	noarch

%description
Metapackage for Software Development Kit for the K Desktop Environment.

%files

#---------------------------------------------------------------

%prep

%build

%install

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0
- Just a metapackage from now on

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1
- Fix files

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


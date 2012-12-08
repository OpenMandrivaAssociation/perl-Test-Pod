%define upstream_name       Test-Pod
%define upstream_version 1.45

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary: 	Check for POD errors in files
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Pod::Simple) >= 3.07
BuildRequires:	perl(Test::Builder::Tester)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description 
Check POD files for errors or warnings in a test file, using Pod::Simple to do
the heavy lifting.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.450.0-5mdv2012.0
+ Revision: 765736
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.450.0-3
+ Revision: 763105
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.450.0-2
+ Revision: 667350
- mass rebuild

* Sun Mar 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.450.0-1
+ Revision: 644342
- update to new version 1.45

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.440.0-2mdv2011.0
+ Revision: 564756
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.440.0-1mdv2011.0
+ Revision: 552638
- update to 1.44

* Thu Apr 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.430.0-1mdv2010.1
+ Revision: 537883
- update to 1.43

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.420.0-1mdv2010.1
+ Revision: 518085
- update to 1.42

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.410.0-1mdv2010.1
+ Revision: 491634
- update to 1.41

* Thu Jul 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.400.0-1mdv2010.0
+ Revision: 396671
- use %%perl_version macro
- update to new version 1.40

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.26-4mdv2009.0
+ Revision: 224138
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.26-3mdv2008.1
+ Revision: 180598
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-2mdv2008.0
+ Revision: 67069
- rebuild


* Sun Jul 23 2006 Emmanuel Andry <eandry@mandriva.org> 1.26-1mdv2007.0
- 1.26

* Thu Feb 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.24-1mdk
- 1.24

* Fri Oct 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.22-1mdk
- 1.22

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.20-4mdk
- fix deps

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-3mdk 
- spec cleanup
- better url
- rpmbuildupdate aware
- don't ship useless empty dirs
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.20-2mdk
- fix buildrequires in a backward compatible way

* Tue Jun 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.20-1mdk
- 1.20

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.16-1mdk
- 1.16
- cosmetics

* Mon Mar 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.12-1mdk
- first mdk release


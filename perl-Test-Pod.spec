%define modname	Test-Pod
%define modver 1.51

# Avoid nasty circular dependency
%define dont_gprintify 1

Summary:	Check for POD errors in files

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Pod::Simple) >= 3.07
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(JSON::PP)

%description 
Check POD files for errors or warnings in a test file, using Pod::Simple to do
the heavy lifting.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL installdirs=vendor
%make_build

%check
%make test

%install
%make_install
find %{buildroot} -name .packlist -o -name perllocal.pod |xargs rm -f

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/man3/*

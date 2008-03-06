%define	module	Test-Pod
%define	name	perl-%{module}
%define version 1.26
%define release %mkrel 3

Summary: 	Check for POD errors in files
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0: 	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-Pod-Simple
BuildRequires:	perl-Test-Builder-Tester
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description 
Check POD files for errors or warnings in a test file, using Pod::Simple to do
the heavy lifting.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*


%define upstream_name       Test-Pod
%define upstream_version 1.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	Check for POD errors in files
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Pod-Simple >= 3.07
BuildRequires:	perl-Test-Builder-Tester

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

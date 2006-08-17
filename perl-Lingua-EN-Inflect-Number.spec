#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Inflect-Number
Summary:	Lingua::EN::Inflect::Number - Force number of words to singular or plural
#Summary(pl):	
Name:		perl-Lingua-EN-Inflect-Number
Version:	1.1
Release:	1
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SI/SIMON/Lingua-EN-Inflect-Number-1.1.tar.gz
# Source0-md5:	bcee940ef603da93e7da11d8eecad409
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Lingua-EN-Inflect
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module extends the functionality of Lingua::EN::Inflect with three
new functions available for export:

This takes a word, and determines its number. It returns s for singular,
p for plural, and ambig for words that can be either singular or plural.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Lingua/EN/Inflect/*.pm
%{_mandir}/man3/*

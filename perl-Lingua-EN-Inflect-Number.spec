#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Inflect-Number
Summary:	Lingua::EN::Inflect::Number - Force number of words to singular or plural
Summary(pl.UTF-8):   Lingua::EN::Inflect::Number - wymuszanie liczby słów na pojedynczą lub mnogą
Name:		perl-Lingua-EN-Inflect-Number
Version:	1.1
Release:	1
License:	Unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SI/SIMON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bcee940ef603da93e7da11d8eecad409
URL:		http://search.cpan.org/dist/Lingua-EN-Inflect-Number/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Lingua-EN-Inflect
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module extends the functionality of Lingua::EN::Inflect with
three new functions available for export.

"number" takes a word, and determines its number. It returns s for
singular, p for plural, and ambig for words that can be either
singular or plural.

"to_S" and "to_PL" take a word and convert it forcefully either to
singular or to plural. Lingua::EN::Inflect does funny things if you
try to pluralise an already-plural word, but this module does the
right thing.

%description -l pl.UTF-8
Ten moduł rozszerza funkcjonalność Lingua::EN::Inflect o trzy nowe
funkcje dostępne do wyeksportowania.

"number" przyjmuje słowo i określa jego liczbę. Zwraca s dla
pojedynczej, p dla mnogiej i ambig dla słów, które mogą być zarówno w
liczbie pojedynczej, jak i mnogiej.

"to_S" i "to_PL" przyjmują słowo i wymuszają zmianę jego liczby na
pojedynczą lub mnogą. Lingua::EN::Inflect robi dziwne rzeczy jeżeli
próbujemy zmienić na liczbę mnogą słowo, które już jest w liczbie
mnogiej, ale ten moduł zachowuje się poprawnie.

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

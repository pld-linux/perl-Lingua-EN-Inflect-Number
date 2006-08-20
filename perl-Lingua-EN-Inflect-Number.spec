#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Inflect-Number
Summary:	Lingua::EN::Inflect::Number - Force number of words to singular or plural
Summary(pl):	Lingua::EN::Inflect::Number - wymuszanie liczby s³ów na pojedyncz± lub mnog±
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

%description -l pl
Ten modu³ rozszerza funkcjonalno¶æ Lingua::EN::Inflect o trzy nowe
funkcje dostêpne do wyeksportowania.

"number" przyjmuje s³owo i okre¶la jego liczbê. Zwraca s dla
pojedynczej, p dla mnogiej i ambig dla s³ów, które mog± byæ zarówno w
liczbie pojedynczej, jak i mnogiej.

"to_S" i "to_PL" przyjmuj± s³owo i wymuszaj± zmianê jego liczby na
pojedyncz± lub mnog±. Lingua::EN::Inflect robi dziwne rzeczy je¿eli
próbujemy zmieniæ na liczbê mnog± s³owo, które ju¿ jest w liczbie
mnogiej, ale ten modu³ zachowuje siê poprawnie.

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

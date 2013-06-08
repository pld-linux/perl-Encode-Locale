#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Encode
%define		pnam	Locale
%include	/usr/lib/rpm/macros.perl
Summary:	Encode::Locale - Determine the locale encoding
Summary(pl.UTF-8):	Encode::Locale - określenie kodowania lokalizacji
Name:		perl-Encode-Locale
Version:	1.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de8422d068634e7c1068dab4e18b452f
URL:		http://search.cpan.org/dist/Encode-Locale/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Encode >= 2
%endif
Requires:	perl-Encode >= 2.44-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Encode::Locale module looks up the charset and encoding (called a
CODESET in the locale jargon) and arrange for the Encode module to
know this encoding under the name "locale". It means bytes obtained
from the environment can be converted to Unicode strings by calling
Encode::encode(locale => $bytes) and converted back again with
Encode::decode(locale => $string).

%description -l pl.UTF-8
Moduł Encode::Locale sprawdza zestaw znaków i kodowanie (nazywane
CODESET) i przygotowuje je dla modułu Encode pod nazwą "locale".
To oznacza, że tekst zakodowany bajtowo może być przekonwertowany do
Unikodu przez wywołanie Encode::encode(locale => $bytes) i z powrotem
przez Encode::decode(locale => $string).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Encode/Locale.pm
%{_mandir}/man3/Encode::Locale.3pm*

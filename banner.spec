Summary:	Print short string in large letters
Summary(pl.UTF-8):	Wypisywanie krótkiego tekstu wielkimi literami
Name:		banner
Version:	1.3.4
Release:	1
License:	GPL v2
Group:		Applications/Games
Source0:	http://cedar-solutions.com/ftp/software/%{name}-%{version}.tar.gz
# Source0-md5:	cfd45b431a5356c086657365b23ab0c4
URL:		http://www.cedar-solutions.com/software.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nearly all UN*X systems seem to provide a "banner" program that prints
some short string in large letters. Except, apparently, Linux. This
program fills that hole. It prints a "banner" on the screen that
corresponds to the first 10 characters of a string entered on the
command line, in a way similar to what you might see when using
Solaris or AIX.

%description -l pl.UTF-8
Prawie wszystkie systemy UN*Xowe udostępniają program "banner"
wypisujący jakiś krótki tekst wielkimi literami. Za wyjątkiem Linuksa.
Ten program uzupełnia tę lukę. Wypisuje "banner" na ekranie za pomocą
wielkich liter z 10 pierwszych znaków wpisanego w linii poleceń
tekstu, podobnie jak można to zobaczyć korzystając z Solarisa lub
AIX-a.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/banner
%{_mandir}/man1/banner.1*

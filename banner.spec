Summary:	Print short string in large letters
Summary(pl.UTF-8):   Wypisywanie krótkiego tekstu wielkimi literami
Name:		banner
Version:	1.3.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://cedar-solutions.com/ftp/software/%{name}-%{version}.tar.gz
# Source0-md5:	61d675c768483e8a3c7228cd54decab3
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
wielkich liter z 10 pierwszych znaków wpisanego w linii poleceń tekstu,
podobnie jak można to zobaczyć korzystając z Solarisa lub AIX-a.

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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*

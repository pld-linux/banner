Summary:	Print short string in large letters
Summary(pl):	Wypisywanie krótkiego tekstu wielkimi literami
Name:		banner
Version:	1.3.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://cedar-solutions.com/ftp/software/%{name}-%{version}.tar.gz
# Source0-md5:	7474553ea3ac8e330901525c6d03eae1
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

%description -l pl
Prawie wszystkie systemy UN*Xowe udostêpniaj± program "banner"
wypisuj±cy jaki¶ krótki tekst wielkimi literami. Za wyj±tkiem Linuksa.
Ten program uzupe³nia tê lukê. Wypisuje "banner" na ekranie za pomoc±
wielkich liter z 10 pierwszych znaków wpisanego w lini poleceñ tekstu,
podobnie jak mo¿na to zobaczyæ korzystaj±c z Solarisa lub AIX-a.

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

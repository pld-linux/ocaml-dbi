%define		_vendor_name	ocamldbi
Summary:	Database independent layer
Summary(pl):	Niezale¿ne od bazy danych API dla ocamla
Name:		ocaml-dbi
Version:	0.9.10
Release:	3
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/modcaml/%{_vendor_name}-%{version}.tar.gz
# Source0-md5:	d23495a0a6dee8c0d636d29df844e981
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-postgres-devel
BuildRequires:	ocaml-mysql-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ocamldbi is a database independent layer for Objective CAML (OCaml)
patterned upon Perl DBI.

Currently there are drivers for PostgreSQL and MySQL, and you can use
Perl DBD (database drivers) if you have Perl4Caml installed.

%description -l pl
ocamldbi to niezale¿na od bazy danych warstwa dla Objective CAML-a
(OCamla) wzorowana na perlowym DBI.

Aktualnie dostêpne s± sterowniki dla PostgreSQL-a i MySQL-a oraz mo¿na
u¿ywaæ perlowych sterowników DBD, je¶li zainstalowany jest Perl4Caml.

%package devel
Summary:	Database independent layer - development part
Summary(pl):	Niezale¿ne od bazy danych API dla ocamla - czê¶æ programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
ocamldbi is a database independent layer for Objective CAML (OCaml)
patterned upon Perl DBI. Currently there are drivers for PostgreSQL
and MySQL, and you can use Perl DBD (database drivers) if you have
Perl4Caml installed.

This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl
ocamldbi to niezale¿na od bazy danych warstwa dla Objective CAML-a
(OCamla) wzorowana na perlowym DBI. Aktualnie dostêpne s± sterowniki
dla PostgreSQL-a i MySQL-a oraz mo¿na u¿ywaæ perlowych sterowników
DBD, je¶li zainstalowany jest Perl4Caml.

Ten pakiet zawiera pliki potrzebne do tworzenia programów w OCamlu z
u¿yciem tej biblioteki.

%package postgres-driver
Summary:	Database independent layer - PostgreSQL driver
Summary(pl):	Warstwa niezale¿na od bazy danych - sterownik do PostgreSQL-a
Group:		Development/Libraries
Requires:       ocaml-dbi-devel >= 0.9.10-2
%requires_eq	ocaml

%description postgres-driver
ocamldbi is a database independent layer for Objective CAML (OCaml)
patterned upon Perl DBI. This subpackage containes driver for
PostgreSQL.

%description postgres-driver -l pl
ocamldbi to niezale¿na od bazy danych warstwa dla Objective CAML-a
(OCamla) wzorowana na perlowym DBI. Ten pakiet zawiera sterownik dla
PostgreSQL-a.

%package mysql-driver
Summary:	Database independent layer - MySQL driver
Summary(pl):	Warstwa niezale¿na od bazy danych - sterownik do MySQL-a
Group:		Development/Libraries
Requires:       ocaml-dbi-devel >= 0.9.10-2
%requires_eq	ocaml

%description mysql-driver
ocamldbi is a database independent layer for Objective CAML (OCaml)
patterned upon Perl DBI. This subpackage containes driver for MySQL.

%description mysql-driver -l pl
ocamldbi to niezale¿na od bazy danych warstwa dla Objective CAML-a
(OCamla) wzorowana na perlowym DBI. Ten pakiet zawiera sterownik dla
MySQL-a.

%prep
%setup -q -n %{_vendor_name}-%{version}

%build
%{__make} all opt \
	CC="%{__cc} %{rpmcflags} -fPIC" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/dbi
install *.cm[ixao]* *.a $RPM_BUILD_ROOT%{_libdir}/ocaml/dbi

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/dbi
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/dbi/META <<EOF
requires = ""
version = "%{version}"
directory = "+dbi"
archive(byte) = "dbi.cma"
archive(native) = "dbi.cmxa"
linkopts = ""
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING.LIB *.mli html
%dir %{_libdir}/ocaml/dbi
%{_libdir}/ocaml/dbi/*.cm[ixa]*
%{_libdir}/ocaml/dbi/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/dbi

%files postgres-driver
%defattr(644,root,root,755)
%{_libdir}/ocaml/dbi/dbi_postgres.cmo

%files mysql-driver
%defattr(644,root,root,755)
%{_libdir}/ocaml/dbi/dbi_mysql.cmo

%define		_vendor_name	ocamldbi
Summary:	Database independent layer
Summary(pl):	Niezalezne od bazy danych API dla ocamla
Name:		ocaml-dbi
Version:	0.9.10
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/modcaml/%{_vendor_name}-%{version}.tar.gz
# Source0-md5:	d23495a0a6dee8c0d636d29df844e981
BuildRequires:	ocaml >= 3.04-7
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ocamldbi is a database independent layer for Objective CAML (OCaml)
patterned upon Perl DBI.

Currently there are drivers for PostgreSQL and MySQL, and you can use
Perl DBD (database drivers) if you have Perl4Caml installed.

%package devel
Summary:	TEMPLATE binding for OCaml - development part
Summary(pl):	Wi±zania TEMPLATE dla OCamla - czê¶æ programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
ocamldbi is a database independent layer for Objective CAML (OCaml)
patterned upon Perl DBI.

Currently there are drivers for PostgreSQL and MySQL, and you can use
Perl DBD (database drivers) if you have Perl4Caml installed. This
package contains files needed to develop OCaml programs using this
library.

%prep
%setup -q -n %{_vendor_name}-%{version}

%build
%{__make} CC="%{__cc} %{rpmcflags} -fPIC" all opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/dbi
install *.cm[ixa]* *.a $RPM_BUILD_ROOT%{_libdir}/ocaml/dbi

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
%doc COPYING.LIB *.mli
%dir %{_libdir}/ocaml/dbi
%{_libdir}/ocaml/dbi/*.cm[ixa]*
%{_libdir}/ocaml/dbi/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/dbi

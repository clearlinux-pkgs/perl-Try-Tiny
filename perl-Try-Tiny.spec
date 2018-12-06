#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Try-Tiny
Version  : 0.30
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Try-Tiny-0.30.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Try-Tiny-0.30.tar.gz
Summary  : 'Minimal try/catch with proper preservation of $@'
Group    : Development/Tools
License  : MIT
Requires: perl-Try-Tiny-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Try-Tiny,
version 0.30:
Minimal try/catch with proper preservation of $@

%package dev
Summary: dev components for the perl-Try-Tiny package.
Group: Development
Provides: perl-Try-Tiny-devel = %{version}-%{release}

%description dev
dev components for the perl-Try-Tiny package.


%package license
Summary: license components for the perl-Try-Tiny package.
Group: Default

%description license
license components for the perl-Try-Tiny package.


%prep
%setup -q -n Try-Tiny-0.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Try-Tiny
cp LICENCE %{buildroot}/usr/share/package-licenses/perl-Try-Tiny/LICENCE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Try/Tiny.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Try::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Try-Tiny/LICENCE

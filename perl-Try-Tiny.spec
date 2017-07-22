#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Try-Tiny
Version  : 0.22
Release  : 14
URL      : http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Try-Tiny-0.22.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Try-Tiny-0.22.tar.gz
Summary  : 'minimal try/catch with proper preservation of $@'
Group    : Development/Tools
License  : MIT
Requires: perl-Try-Tiny-doc

%description
This archive contains the distribution Try-Tiny,
version 0.22:
minimal try/catch with proper preservation of $@

%package doc
Summary: doc components for the perl-Try-Tiny package.
Group: Documentation

%description doc
doc components for the perl-Try-Tiny package.


%prep
%setup -q -n Try-Tiny-0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/Try/Tiny.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

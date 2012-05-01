Name: hyphen-sa
Summary: Sanskrit hyphenation rules
%define upstreamid 20090412
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/hyph-sa.tex
Group: Applications/Text
URL: http://tug.org/tex-hyphen
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-sa-cleantex.patch

%description
Sanskrit hyphenation rules (also suitable for Bengali).

%prep
%setup -T -q -c -n hyphen-sa
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-sa.tex hyph_sa_IN.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-sa.tex hyph_sa_IN.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 15 hyph-sa.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sa_IN.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/hyph_sa_IN.dic

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090412-3.1
- Rebuilt for RHEL 6

* Wed Aug 19 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090412-3
- Related: rhbz#517821 drop hyphen-bn alias

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090412-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090412-1
- latest version

* Mon Apr 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081010-1
- initial version

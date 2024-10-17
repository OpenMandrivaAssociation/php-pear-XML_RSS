%define		_class		XML
%define		_subclass	RSS
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.2
Release:	4
Summary:	RSS parser
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/XML_RSS/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Parser for Resource Description Framework (RDF) Site Summary (RSS)
documents.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2012.0
+ Revision: 742309
- fix major breakage by careless packager

* Mon May 09 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1
+ Revision: 672716
- 1.0.2

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 594505
- update to new version 1.0.1

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 508993
- update to new version 1.0.0

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.10-5mdv2010.1
+ Revision: 464961
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.10-4mdv2010.0
+ Revision: 441763
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-3mdv2009.1
+ Revision: 322928
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-2mdv2009.0
+ Revision: 237168
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.10-1mdv2008.0
+ Revision: 15504
- 0.9.10


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-1mdv2007.0
+ Revision: 82904
- Import php-pear-XML_RSS

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-1mdk
- 0.9.9
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-1mdk
- initial Mandriva package (PLD import)


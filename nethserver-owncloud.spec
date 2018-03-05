Summary: NethServer Owncloud configuration
Name: nethserver-owncloud
Version: 2.0.3
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

AutoReq: no
Requires: owncloud = 7.0.13
Requires: php-ldap, php-gd, php-pdo, php-mysql, php-pear, php-pear-MDB2, php-pear-MDB2-Driver-mysqli, php-pear-Net-Curl
Requires: nethserver-httpd, nethserver-mysql

%description
NethServer Owncloud configuration

%prep
%setup

%post

%preun

%build
perl createlinks

%install
rm -rf %{buildroot}

(cd root   ; find . -depth -print | cpio -dump %{buildroot})

%{genfilelist} \
	--dir /var/www/html/owncloud 'attr(750, root, apache)' \
	--dir /var/www/html/owncloud/apps 'attr(770, apache, apache)' \
	--dir /var/www/html/owncloud/apps/user_ldap 'attr(750, root, apache)' \
	--dir /var/www/html/owncloud/apps/user_ldap/command 'attr(750, root, apache)' \
    %{buildroot} > e-smith-%{version}-filelist
echo "%doc COPYING"          >> e-smith-%{version}-filelist

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Mon Mar 05 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.3-1
- Fix dirty exit status

* Fri Sep 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.2-1
- Fix db migration - NehServer/nethserver-owncloud#4

* Wed May 10 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.1-1
- Upgrade from NS 6 via backup and restore - NethServer/dev#5234

* Thu Apr 20 2017 Davide Principi <davide.principi@nethesis.it> - 2.0.0-1
- Build for ns7, to help upgrades from ns6
- Upgrade from NS 6 via backup and restore - NethServer/dev#5234

* Tue Mar 29 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.8-1
- Update to owncloud 7.0.13 - Enhancement #3366

* Tue Nov 10 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.7-1
- Update to owncloud 7.0.11 - Enhancement #3307 [NethServer]

* Tue Sep 22 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.6-1
- Update to owncloud 7.0.10 - Enhancement #3261 [NethServer]

* Wed Sep 09 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.5-1
- Update to owncloud 7.0.8 - Enhancement #3252 [NethServer]

* Tue Jun 30 2015 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.1.4-1
- Wrong email field on LDAP configuration - Bug #3205 [NethServer]
- Update ownCloud to 7.0.6 version - Feature #3191 [NethServer]
- OwnCloud trusted domains - Enhancement #3022 [NethServer]
- OwnCloud update event dirties configuration file - Bug #3021 [NethServer]

* Thu Apr 09 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Update ownCloud to 7.0.5 version - Feature #3109 [NethServer]

* Mon Apr 7 2015 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.1.3-1.ns6
- Update ownCloud to 7.0.5 version - Feature #3109 [NethServer]

* Thu Jan 22 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1.ns6
- Update ownCloud to 7.0.4 version - Feature #2986 [NethServer]

* Tue Dec 16 2014 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.1.1-1.ns6
- Adapt all mysql commands to use "--defaults-file=/root/.my.cnf" option - Bug #2971 [NethServer]
- OwnCloud installation from NethServer web interface fails - Bug #2983 [NethServer]

* Tue Dec 02 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1.ns6
- Upgrade to ownCloud 7 - Enhancement #2669 [NethServer]

* Mon Mar 10 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.2-1.ns6
- Can't find ownCloud LDAP secret password - Bug #2670 [NethServer]

* Mon Dec 16 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- /owncloud path not found - Bug #2342 [NethServer]

* Mon Nov 11 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- First NethServer/ownCloud integration release - Feature #2037 [NethServer]


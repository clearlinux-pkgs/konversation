#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: f4bef72
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : konversation
Version  : 24.02.0
Release  : 8
URL      : https://download.kde.org/stable/release-service/24.02.0/src/konversation-24.02.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.0/src/konversation-24.02.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.0/src/konversation-24.02.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 GPL-3.0 LGPL-2.0
Requires: konversation-bin = %{version}-%{release}
Requires: konversation-data = %{version}-%{release}
Requires: konversation-license = %{version}-%{release}
Requires: konversation-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : kidletime-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : qca-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Konversation website: https://konversation.kde.org/
Konversation wiki: https://userbase.kde.org/Konversation
Bug tracker: https://bugs.kde.org/
IRC channel: #konversation on irc.libera.chat

%package bin
Summary: bin components for the konversation package.
Group: Binaries
Requires: konversation-data = %{version}-%{release}
Requires: konversation-license = %{version}-%{release}

%description bin
bin components for the konversation package.


%package data
Summary: data components for the konversation package.
Group: Data

%description data
data components for the konversation package.


%package doc
Summary: doc components for the konversation package.
Group: Documentation

%description doc
doc components for the konversation package.


%package license
Summary: license components for the konversation package.
Group: Default

%description license
license components for the konversation package.


%package locales
Summary: locales components for the konversation package.
Group: Default

%description locales
locales components for the konversation package.


%prep
%setup -q -n konversation-24.02.0
cd %{_builddir}/konversation-24.02.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710601129
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710601129
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/konversation
cp %{_builddir}/konversation-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/konversation/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/konversation-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/konversation/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/konversation-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/konversation/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/konversation-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/konversation/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/konversation-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/konversation/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/konversation-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/konversation/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/konversation-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/konversation/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/konversation-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/konversation/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/konversation-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/konversation/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang konversation

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/konversation

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.konversation.desktop
/usr/share/dbus-1/services/org.kde.konversation.service
/usr/share/icons/hicolor/128x128/actions/konv_message.png
/usr/share/icons/hicolor/128x128/apps/konversation.png
/usr/share/icons/hicolor/16x16/actions/konv_message.png
/usr/share/icons/hicolor/16x16/apps/konversation.png
/usr/share/icons/hicolor/22x22/actions/konv_message.png
/usr/share/icons/hicolor/22x22/apps/konversation.png
/usr/share/icons/hicolor/32x32/actions/konv_message.png
/usr/share/icons/hicolor/32x32/apps/konversation.png
/usr/share/icons/hicolor/48x48/actions/konv_message.png
/usr/share/icons/hicolor/48x48/apps/konversation.png
/usr/share/icons/hicolor/64x64/actions/konv_message.png
/usr/share/icons/hicolor/64x64/apps/konversation.png
/usr/share/knotifications6/konversation.notifyrc
/usr/share/knsrcfiles/konversation_nicklist_theme.knsrc
/usr/share/konversation/scripting_support/python/konversation/__init__.py
/usr/share/konversation/scripting_support/python/konversation/dbus.py
/usr/share/konversation/scripting_support/python/konversation/i18n.py
/usr/share/konversation/scripts/bug
/usr/share/konversation/scripts/cmd
/usr/share/konversation/scripts/fortune
/usr/share/konversation/scripts/fortunes.dat
/usr/share/konversation/scripts/gauge
/usr/share/konversation/scripts/media
/usr/share/konversation/scripts/sayclip
/usr/share/konversation/scripts/sysinfo
/usr/share/konversation/scripts/tinyurl
/usr/share/konversation/scripts/uptime
/usr/share/konversation/themes/alternative/index.desktop
/usr/share/konversation/themes/alternative/irc_admin.png
/usr/share/konversation/themes/alternative/irc_away.png
/usr/share/konversation/themes/alternative/irc_halfop.png
/usr/share/konversation/themes/alternative/irc_normal.png
/usr/share/konversation/themes/alternative/irc_op.png
/usr/share/konversation/themes/alternative/irc_owner.png
/usr/share/konversation/themes/alternative/irc_voice.png
/usr/share/konversation/themes/christmas/index.desktop
/usr/share/konversation/themes/christmas/irc_admin.png
/usr/share/konversation/themes/christmas/irc_away.png
/usr/share/konversation/themes/christmas/irc_halfop.png
/usr/share/konversation/themes/christmas/irc_normal.png
/usr/share/konversation/themes/christmas/irc_op.png
/usr/share/konversation/themes/christmas/irc_owner.png
/usr/share/konversation/themes/christmas/irc_voice.png
/usr/share/konversation/themes/classic/index.desktop
/usr/share/konversation/themes/classic/irc_admin.png
/usr/share/konversation/themes/classic/irc_away.png
/usr/share/konversation/themes/classic/irc_halfop.png
/usr/share/konversation/themes/classic/irc_normal.png
/usr/share/konversation/themes/classic/irc_op.png
/usr/share/konversation/themes/classic/irc_owner.png
/usr/share/konversation/themes/classic/irc_voice.png
/usr/share/konversation/themes/default-dark/index.desktop
/usr/share/konversation/themes/default-dark/irc_admin.svg
/usr/share/konversation/themes/default-dark/irc_away.svg
/usr/share/konversation/themes/default-dark/irc_away_stacked.svg
/usr/share/konversation/themes/default-dark/irc_halfop.svg
/usr/share/konversation/themes/default-dark/irc_normal.svg
/usr/share/konversation/themes/default-dark/irc_op.svg
/usr/share/konversation/themes/default-dark/irc_owner.svg
/usr/share/konversation/themes/default-dark/irc_voice.svg
/usr/share/konversation/themes/default/index.desktop
/usr/share/konversation/themes/default/irc_admin.svg
/usr/share/konversation/themes/default/irc_away.svg
/usr/share/konversation/themes/default/irc_away_stacked.svg
/usr/share/konversation/themes/default/irc_halfop.svg
/usr/share/konversation/themes/default/irc_normal.svg
/usr/share/konversation/themes/default/irc_op.svg
/usr/share/konversation/themes/default/irc_owner.svg
/usr/share/konversation/themes/default/irc_voice.svg
/usr/share/konversation/themes/oxygen/index.desktop
/usr/share/konversation/themes/oxygen/irc_admin.png
/usr/share/konversation/themes/oxygen/irc_away.png
/usr/share/konversation/themes/oxygen/irc_halfop.png
/usr/share/konversation/themes/oxygen/irc_normal.png
/usr/share/konversation/themes/oxygen/irc_op.png
/usr/share/konversation/themes/oxygen/irc_owner.png
/usr/share/konversation/themes/oxygen/irc_voice.png
/usr/share/konversation/themes/simplistic/index.desktop
/usr/share/konversation/themes/simplistic/irc_admin.png
/usr/share/konversation/themes/simplistic/irc_away.png
/usr/share/konversation/themes/simplistic/irc_halfop.png
/usr/share/konversation/themes/simplistic/irc_normal.png
/usr/share/konversation/themes/simplistic/irc_op.png
/usr/share/konversation/themes/simplistic/irc_owner.png
/usr/share/konversation/themes/simplistic/irc_voice.png
/usr/share/konversation/themes/smiling/index.desktop
/usr/share/konversation/themes/smiling/irc_admin.png
/usr/share/konversation/themes/smiling/irc_away.png
/usr/share/konversation/themes/smiling/irc_halfop.png
/usr/share/konversation/themes/smiling/irc_normal.png
/usr/share/konversation/themes/smiling/irc_op.png
/usr/share/konversation/themes/smiling/irc_owner.png
/usr/share/konversation/themes/smiling/irc_voice.png
/usr/share/konversation/themes/square/index.desktop
/usr/share/konversation/themes/square/irc_admin.png
/usr/share/konversation/themes/square/irc_away.png
/usr/share/konversation/themes/square/irc_halfop.png
/usr/share/konversation/themes/square/irc_normal.png
/usr/share/konversation/themes/square/irc_op.png
/usr/share/konversation/themes/square/irc_owner.png
/usr/share/konversation/themes/square/irc_voice.png
/usr/share/metainfo/org.kde.konversation.appdata.xml
/usr/share/qlogging-categories6/konversation.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/konversation/index.cache.bz2
/usr/share/doc/HTML/ca/konversation/index.docbook
/usr/share/doc/HTML/en/konversation/addchannel.png
/usr/share/doc/HTML/en/konversation/addnetwork_co.png
/usr/share/doc/HTML/en/konversation/addserver_co.png
/usr/share/doc/HTML/en/konversation/bold-text.png
/usr/share/doc/HTML/en/konversation/channel_screen_tour_co.png
/usr/share/doc/HTML/en/konversation/channellist_screen_co.png
/usr/share/doc/HTML/en/konversation/checkidentities.png
/usr/share/doc/HTML/en/konversation/colorchooser_screen.png
/usr/share/doc/HTML/en/konversation/dccstatus_screen_co.png
/usr/share/doc/HTML/en/konversation/first_channel_co.png
/usr/share/doc/HTML/en/konversation/first_serverlist_co.png
/usr/share/doc/HTML/en/konversation/format-text-color.png
/usr/share/doc/HTML/en/konversation/highlighting_screen_co.png
/usr/share/doc/HTML/en/konversation/identities_adv_co.png
/usr/share/doc/HTML/en/konversation/identities_away_co.png
/usr/share/doc/HTML/en/konversation/identities_gen_co.png
/usr/share/doc/HTML/en/konversation/index.cache.bz2
/usr/share/doc/HTML/en/konversation/index.docbook
/usr/share/doc/HTML/en/konversation/irc_admin.png
/usr/share/doc/HTML/en/konversation/irc_away.png
/usr/share/doc/HTML/en/konversation/irc_halfop.png
/usr/share/doc/HTML/en/konversation/irc_normal.png
/usr/share/doc/HTML/en/konversation/irc_op.png
/usr/share/doc/HTML/en/konversation/irc_owner.png
/usr/share/doc/HTML/en/konversation/irc_voice.png
/usr/share/doc/HTML/en/konversation/italic-text.png
/usr/share/doc/HTML/en/konversation/led_blue_on.png
/usr/share/doc/HTML/en/konversation/led_green_on.png
/usr/share/doc/HTML/en/konversation/led_red_on.png
/usr/share/doc/HTML/en/konversation/led_yellow_on.png
/usr/share/doc/HTML/en/konversation/logviewer_co.png
/usr/share/doc/HTML/en/konversation/monospace-text.png
/usr/share/doc/HTML/en/konversation/nicksonline_co.png
/usr/share/doc/HTML/en/konversation/nickthemes_screen_co.png
/usr/share/doc/HTML/en/konversation/notification_screen_co.png
/usr/share/doc/HTML/en/konversation/notifylist_screen_co.png
/usr/share/doc/HTML/en/konversation/osd_demo.png
/usr/share/doc/HTML/en/konversation/osd_screen_co.png
/usr/share/doc/HTML/en/konversation/quickbuttons_screen.png
/usr/share/doc/HTML/en/konversation/quickconnect_screen.png
/usr/share/doc/HTML/en/konversation/serverlist_co.png
/usr/share/doc/HTML/en/konversation/struck-out-text.png
/usr/share/doc/HTML/en/konversation/underline-text.png
/usr/share/doc/HTML/en/konversation/urlcatcher_screen_co.png
/usr/share/doc/HTML/en/konversation/webbrowser_screen_co.png
/usr/share/doc/HTML/es/konversation/index.cache.bz2
/usr/share/doc/HTML/es/konversation/index.docbook
/usr/share/doc/HTML/fr/konversation/index.cache.bz2
/usr/share/doc/HTML/fr/konversation/index.docbook
/usr/share/doc/HTML/it/konversation/addchannel.png
/usr/share/doc/HTML/it/konversation/addnetwork_co.png
/usr/share/doc/HTML/it/konversation/addserver_co.png
/usr/share/doc/HTML/it/konversation/channel_screen_tour_co.png
/usr/share/doc/HTML/it/konversation/channellist_screen_co.png
/usr/share/doc/HTML/it/konversation/checkidentities.png
/usr/share/doc/HTML/it/konversation/colorchooser_screen.png
/usr/share/doc/HTML/it/konversation/dccstatus_screen_co.png
/usr/share/doc/HTML/it/konversation/first_channel_co.png
/usr/share/doc/HTML/it/konversation/first_serverlist_co.png
/usr/share/doc/HTML/it/konversation/highlighting_screen_co.png
/usr/share/doc/HTML/it/konversation/identities_adv_co.png
/usr/share/doc/HTML/it/konversation/identities_away_co.png
/usr/share/doc/HTML/it/konversation/identities_gen_co.png
/usr/share/doc/HTML/it/konversation/index.cache.bz2
/usr/share/doc/HTML/it/konversation/index.docbook
/usr/share/doc/HTML/it/konversation/logviewer_co.png
/usr/share/doc/HTML/it/konversation/nicksonline_co.png
/usr/share/doc/HTML/it/konversation/nickthemes_screen_co.png
/usr/share/doc/HTML/it/konversation/notification_screen_co.png
/usr/share/doc/HTML/it/konversation/notifylist_screen_co.png
/usr/share/doc/HTML/it/konversation/osd_demo.png
/usr/share/doc/HTML/it/konversation/osd_screen_co.png
/usr/share/doc/HTML/it/konversation/quickbuttons_screen.png
/usr/share/doc/HTML/it/konversation/quickconnect_screen.png
/usr/share/doc/HTML/it/konversation/serverlist_co.png
/usr/share/doc/HTML/it/konversation/urlcatcher_screen_co.png
/usr/share/doc/HTML/it/konversation/webbrowser_screen_co.png
/usr/share/doc/HTML/nl/konversation/index.cache.bz2
/usr/share/doc/HTML/nl/konversation/index.docbook
/usr/share/doc/HTML/sv/konversation/addchannel.png
/usr/share/doc/HTML/sv/konversation/addnetwork_co.png
/usr/share/doc/HTML/sv/konversation/addserver_co.png
/usr/share/doc/HTML/sv/konversation/channel_screen_tour_co.png
/usr/share/doc/HTML/sv/konversation/channellist_screen_co.png
/usr/share/doc/HTML/sv/konversation/checkidentities.png
/usr/share/doc/HTML/sv/konversation/colorchooser_screen.png
/usr/share/doc/HTML/sv/konversation/dccstatus_screen_co.png
/usr/share/doc/HTML/sv/konversation/first_channel_co.png
/usr/share/doc/HTML/sv/konversation/first_serverlist_co.png
/usr/share/doc/HTML/sv/konversation/highlighting_screen_co.png
/usr/share/doc/HTML/sv/konversation/identities_adv_co.png
/usr/share/doc/HTML/sv/konversation/identities_away_co.png
/usr/share/doc/HTML/sv/konversation/identities_gen_co.png
/usr/share/doc/HTML/sv/konversation/index.cache.bz2
/usr/share/doc/HTML/sv/konversation/index.docbook
/usr/share/doc/HTML/sv/konversation/kimproxy_create_screen2.png
/usr/share/doc/HTML/sv/konversation/kimproxy_create_screen_co.png
/usr/share/doc/HTML/sv/konversation/logviewer_co.png
/usr/share/doc/HTML/sv/konversation/nicksonline_co.png
/usr/share/doc/HTML/sv/konversation/nickthemes_screen_co.png
/usr/share/doc/HTML/sv/konversation/notification_screen_co.png
/usr/share/doc/HTML/sv/konversation/notifylist_screen_co.png
/usr/share/doc/HTML/sv/konversation/osd_demo.png
/usr/share/doc/HTML/sv/konversation/osd_screen_co.png
/usr/share/doc/HTML/sv/konversation/quickbuttons_screen.png
/usr/share/doc/HTML/sv/konversation/quickconnect_screen.png
/usr/share/doc/HTML/sv/konversation/serverlist_co.png
/usr/share/doc/HTML/sv/konversation/urlcatcher_screen_co.png
/usr/share/doc/HTML/sv/konversation/webbrowser_screen_co.png
/usr/share/doc/HTML/uk/konversation/index.cache.bz2
/usr/share/doc/HTML/uk/konversation/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/konversation/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/konversation/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/konversation/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/konversation/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/konversation/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/konversation/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/konversation/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f konversation.lang
%defattr(-,root,root,-)


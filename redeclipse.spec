Name:		redeclipse
Version:	2.0.0
Release:	1
Summary:	Fast aced first person ego-shooter
Group:		Games/Arcade
License:	zlib/libpng License
URL:		http://www.redeclipse.net/
Source:		https://github.com/redeclipse/base/releases/download/v%{version}/redeclipse_%{version}_nix.tar.bz2
Patch0:     redeclipse-fix-cube2font-install.patch

BuildRequires:	imagemagick
BuildRequires:  ed
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(zlib)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)

Requires:	%{name}-data >= %{version}

%description
The game is a single-player and multi-player first-person ego-shooter,
built as a total conversion of Cube Engine 2, which lends itself toward a
balanced gameplay, completely at the control of map makers, while maintaining
a general theme of agility in a variety of environments.

%package data
Summary:	Data files for RedEclipse game
License:	Creative Commons Attribution-ShareAlike
Requires:	%{name} >= %{version}
BuildArch:	noarch

%description data
The game is a single-player and multi-player first-person ego-shooter,
built as a total conversion of Cube Engine 2, which lends itself toward a
balanced gameplay, completely at the control of map makers, while maintaining
a general theme of agility in a variety of environments.

%package server
Summary:        Server for the Red Eclipse FPS game
# Game engine is zlib
# Trademark info is CC-BY-SA
# Name covered by "trademark guidelines" see trademark.txt
License:        zlib and CC-BY-SA
Requires:       %{name}-data >= %{version}-%{release}

%description server
This package contains the dedicated server for the Red Eclipse FPS game,
it also includes some example scripts for configuring the server.

%package -n cube2font
Summary:        Utility program for creating font bitmaps for Cube Engine games
License:        zlib

%description -n cube2font
cube2font is a utility program designed to create font bitmaps for Cube
Engine games, it works by taking a Truetype font and building it into a
set of coordinates in an image. cube2font is an improved version of the
previous TTF2Font, supporting a much larger range of characters.


%prep
%setup -q
%autopatch -p1

%build
%make_build -C src/ \
    client server cube2font

%install
%make_install -C src prefix=%{_prefix} libexecdir=%{buildroot}%{_libexecdir} system-install system-install-cube2font

# We package this in server docs
rm -rf %{buildroot}%{_docdir}/%{name}/examples


%files
%doc readme.txt doc/announce.txt doc/guidelines.txt
%license doc/license.txt doc/trademark.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/%{name}
%{_mandir}/man6/%{name}.6*


%files data
%license doc/license.txt doc/all-licenses.txt doc/trademark.txt
%{_datadir}/%{name}/
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/config
%{_libexecdir}/%{name}/data
%{_libexecdir}/%{name}/doc

%files server
%doc doc/examples/servinit.cfg
%license doc/license.txt doc/trademark.txt
%{_bindir}/%{name}-server
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/%{name}-server
%{_mandir}/man6/%{name}-server.6*

%files -n cube2font
%{_bindir}/cube2font
%{_mandir}/man1/cube2font.1*

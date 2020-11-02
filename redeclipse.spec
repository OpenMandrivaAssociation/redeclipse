Name:		redeclipse
Version:	2.0.0
Release:	1
Summary:	Fast aced first person ego-shooter
Group:		Games/Arcade
License:	zlib/libpng License
URL:		http://www.redeclipse.net/
Source:		https://github.com/redeclipse/base/releases/download/v%{version}/redeclipse_%{version}_nix.tar.bz2

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

%prep
%setup -q
%autopatch -p1

%build
%make_build -C src/

%install
%make_install -C src prefix=%{_prefix} libexecdir=%{buildroot}%{_libdir} system-install

%files
%doc readme.txt doc/*.txt
%{_bindir}/%{name}-server
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/%{name}-server
%{_libdir}/%{name}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}-server.6.*
%{_mandir}/man6/%{name}.6.*

%files data
%dir %{_datadir}/redeclipse
%{_libdir}/%{name}/data
%{_libdir}/%{name}/game
%{_datadir}/redeclipse/*


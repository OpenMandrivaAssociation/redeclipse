Name:		redeclipse
Version:	1.3.1
Release:	%mkrel 1
Summary:	Fast aced first person ego-shooter
Group:		Games/Arcade
License:	zlib/libpng License
URL:		http://www.redeclipse.net/
Source:		http://sourceforge.net/projects/%{name}/files/%{name}_%{version}/%{name}_%{version}_nix_bsd.tar.bz2
# 128x128 icon is broken in 1.3
Patch0:		redeclipse-1.3.1-128icon.patch
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(gl)
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	zlib-devel
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
%setup -q -n redeclipse
%patch0 -p1 -b .icons

%build
%__sed -i -e 's/^CXXFLAGS= -O3 -fomit-frame-pointer$/CXXFLAGS=%{optflags}/g' src/Makefile
make -C src

%install
%__rm -rf %{buildroot}
%makeinstall_std -C src prefix=%{_prefix} libexecdir=%{buildroot}%{_libdir} system-install
%__sed -i s/ActionGame/ArcadeGame/g %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

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
%{_datadir}/redeclipse/*


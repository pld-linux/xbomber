Name: xbomber
Version: 0.8
Release: 2ark
Summary: A multi-player maze-style game
URL: http://www.newbreedsoftware.com/xbomber/
Source: ftp://ftp.sonic.net/pub/users/nbs/unix/x/xbomber/%name.%version.tar.bz2
License: GPL
Group: Amusements/Games
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: ImageMagick

%description
"X-Bomber" is multi-player maze-style game where players collect and drop
bombs, in an attempt to blow each other up. Last player standing wins!

X-Bomber is vaguely based on "Atomic Bomberman" by InterPlay and "Bomberman"
by Hudsonsof. It is played on a grid, rather than with smooth movement.

%prep
%setup -n %name
for i in bitmaps jungle levels pixmaps sounds; do
	perl -pi -e "s,$i/,%{_datadir}/%{name}/$i/,g" *.c *.h
done

%build
make CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include" XLIB="-L/usr/X11R6/lib -lX11" POSTPROCESS="echo"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/applnk/Games/TacticStrategy $RPM_BUILD_ROOT%{_datadir}/pixmaps $RPM_BUILD_ROOT%{_datadir}/%name
install -m 755 xbomber $RPM_BUILD_ROOT%{_bindir}
cp -aR bitmaps pixmaps jungle levels sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
convert bitmaps/bomb.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xbomber.png
cat >$RPM_BUILD_ROOT%{_datadir}/applnk/Games/TacticStrategy/xbomber.desktop <<EOF
[Desktop Entry]
Name=XBomber
GenericName=Multi-player strategy game
Exec=xbomber
Icon=xbomber
Type=Application
Terminal=0
EOF

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applnk/Games/*/*

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Mon Aug 26 2002 Ark Linux Team <arklinux@arklinux.org> 0.8-2ark
- automated rebuild

* Wed Aug 21 2002 Bernhard Rosenkraenzer <bero@arklinux.org>
- initial RPM

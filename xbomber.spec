Name:		xbomber
Version:	0.8
Release:	2ark
Summary:	A multi-player maze-style game
Group:		Applications/Games
License:	GPL
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/xbomber/%name.%version.tar.gz
URL:		http://www.newbreedsoftware.com/xbomber/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ImageMagick

%description
"X-Bomber" is multi-player maze-style game where players collect and
drop bombs, in an attempt to blow each other up. Last player standing
wins!

X-Bomber is vaguely based on "Atomic Bomberman" by InterPlay and
"Bomberman" by Hudsonsof. It is played on a grid, rather than with
smooth movement.

%prep
%setup -q -n %name
for i in bitmaps jungle levels pixmaps sounds; do
	perl -pi -e "s,$i/,%{_datadir}/%{name}/$i/,g" *.c *.h
done

%build
%{__make} CFLAGS="%{rpmcflags} -I%{_prefix}/X11R6/include" XLIB="-L%{_prefix}/X11R6/lib -lX11" POSTPROCESS="echo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_applnkdir}/Games/TacticStrategy $RPM_BUILD_ROOT%{_datadir}/pixmaps $RPM_BUILD_ROOT%{_datadir}/%name
install -m 755 xbomber $RPM_BUILD_ROOT%{_bindir}
cp -aR bitmaps pixmaps jungle levels sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
convert bitmaps/bomb.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xbomber.png
cat >$RPM_BUILD_ROOT%{_applnkdir}/Games/TacticStrategy/xbomber.desktop <<EOF
[Desktop Entry]
Name=XBomber
GenericName=Multi-player strategy game
Exec=xbomber
Icon=xbomber
Type=Application
Terminal=0
EOF

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_applnkdir}/Games/*/*

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

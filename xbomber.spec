Summary:	A multi-player maze-style game
Summary(pl):	Gra labiryntowa dla wielu graczy
Name:		xbomber
Version:	0.8
Release:	3
Group:		Applications/Games
License:	GPL
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/xbomber/%{name}.%{version}.tar.gz
Source1:	xbomber.desktop
URL:		http://www.newbreedsoftware.com/xbomber/
BuildRequires:	ImageMagick
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"X-Bomber" is multi-player maze-style game where players collect and
drop bombs, in an attempt to blow each other up. Last player standing
wins!

X-Bomber is vaguely based on "Atomic Bomberman" by InterPlay and
"Bomberman" by Hudsonsof. It is played on a grid, rather than with
smooth movement.

%description -l pl
X-Bomber to gra labiryntowa dla wielu graczy, w której gracze zbieraj±
i zrzucaj± bomby, próbuj±c wysadziæ siê nawzajem. Ostatni pozosta³y
przy ¿yciu gracz wygrywa.

X-Bomber niejako bazowany na grach "Atomic Bomberman" firmy InterPlay
oraz "Bomberman" firmy Hudsonsof. Gra toczy siê na siatce, bez
p³ynnych ruchów.

%prep
%setup -q -n %{name}
for i in bitmaps jungle levels pixmaps sounds; do
	perl -pi -e "s,$i/,%{_datadir}/%{name}/$i/,g" *.c *.h
done

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
	XLIB="-L/usr/X11R6/lib -lX11" \
	POSTPROCESS="echo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Games/Strategy,{_pixmapsdir},%{_datadir}/%name}

install xbomber $RPM_BUILD_ROOT%{_bindir}
cp -aR bitmaps pixmaps jungle levels sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
convert bitmaps/bomb.xbm $RPM_BUILD_ROOT%{_pixmapsdir}/xbomber.png

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Strategy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_applnkdir}/Games/Strategy/*

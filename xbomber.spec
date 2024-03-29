Summary:	A multi-player maze-style game
Summary(pl.UTF-8):	Gra labiryntowa dla wielu graczy
Name:		xbomber
Version:	0.8
Release:	3
Group:		X11/Applications/Games
License:	GPL
Source0:	ftp://ftp.sonic.net/pub/users/nbs/unix/x/xbomber/%{name}.%{version}.tar.gz
# Source0-md5:	c17b5dda0241d29ea4644b2906985716
Source1:	xbomber.desktop
URL:		http://www.newbreedsoftware.com/xbomber/
BuildRequires:	ImageMagick
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"X-Bomber" is multi-player maze-style game where players collect and
drop bombs, in an attempt to blow each other up. Last player standing
wins!

X-Bomber is vaguely based on "Atomic Bomberman" by InterPlay and
"Bomberman" by Hudsonsof. It is played on a grid, rather than with
smooth movement.

%description -l pl.UTF-8
X-Bomber to gra labiryntowa dla wielu graczy, w której gracze zbierają
i zrzucają bomby, próbując wysadzić się nawzajem. Ostatni pozostały
przy życiu gracz wygrywa.

X-Bomber niejako bazowany na grach "Atomic Bomberman" firmy InterPlay
oraz "Bomberman" firmy Hudsonsof. Gra toczy się na siatce, bez
płynnych ruchów.

%prep
%setup -q -n %{name}
for i in bitmaps jungle levels pixmaps sounds; do
	%{__perl} -pi -e "s,$i/,%{_datadir}/%{name}/$i/,g" *.c *.h
done

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/X11R6/include" \
	XLIB="-L/usr/X11R6/lib -lX11" \
	POSTPROCESS="echo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name}}

install xbomber $RPM_BUILD_ROOT%{_bindir}
cp -aR bitmaps pixmaps jungle levels sounds $RPM_BUILD_ROOT%{_datadir}/%{name}
convert bitmaps/bomb.xbm $RPM_BUILD_ROOT%{_pixmapsdir}/xbomber.png

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop

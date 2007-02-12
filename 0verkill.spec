Summary:	0verkill - ASCII-art multiplayer game
Summary(pl.UTF-8):   0verkill - gra multiplayer w ASCII
Name:		0verkill
Version:	0.16
Release:	4
License:	GPL
Group:		Applications/Games
Source0:	http://artax.karlin.mff.cuni.cz/~brain/0verkill/release/%{name}-%{version}.tgz
#Source0-md5:	814097fc21a82723a40ec8ae5dd792a7
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://artax.karlin.mff.cuni.cz/~brain/0verkill/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
0verkill is an ASCII-art multiplayer shooting game.

%description -l pl.UTF-8
0verkill jest strzelanką multiplayer z grafiką ASCII.

%package x11
Summary:	X version of 0verkill
Summary(pl.UTF-8):   Wersja 0verkill pod X
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description x11
This package allows you to run an 0verkill client in an X window.

%description x11 -l pl.UTF-8
Ten pakiet pozwala na uruchomienie klienta 0verkill w oknie X.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}
%{__make} x0verkill \
	XLIBS="-L/usr/X11R6/%{_lib} -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{grx,data}}

install 0verkill avi $RPM_BUILD_ROOT%{_bindir}
install x0verkill $RPM_BUILD_ROOT%{_bindir}
install server $RPM_BUILD_ROOT%{_bindir}/0verkill-server
install test_server $RPM_BUILD_ROOT%{_bindir}/0verkill-test_server
install bot $RPM_BUILD_ROOT%{_bindir}/0verkill-bot

for l in data/* ; do
	sed -e 's@grx/@%{_datadir}/0verkill/grx/@' < $l >  $RPM_BUILD_ROOT%{_datadir}/%{name}/$l
done
install grx/* $RPM_BUILD_ROOT%{_datadir}/%{name}/grx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/AUTHORS doc/CHANGELOG doc/*.{txt,html}
%attr(755,root,root) %{_bindir}/0verkill
%attr(755,root,root) %{_bindir}/0verkill-bot
%attr(755,root,root) %{_bindir}/0verkill-server
%attr(755,root,root) %{_bindir}/0verkill-test_server
%attr(755,root,root) %{_bindir}/avi
%{_datadir}/%{name}

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/x0verkill

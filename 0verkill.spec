Summary:	0verkill - ASCII-art multiplayer game
Summary(pl):	0verkill - gra multiplayer w ASCII
Name:		0verkill
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://artax.karlin.mff.cuni.cz/~brain/%{name}/release/%{name}-%{version}.tgz
Patch0:		%{name}-datadir.patch
URL:		http://artax.karlin.mff.cuni.cz/~brain/%{name}/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_x11bindir	%{_prefix}/X11R6/bin

%description
0verkill is an ASCII-art multiplayer shooting game.

%description -l pl
0verkill jest strzelank± multiplayer z grafik± ASCII.

%package x11
Summary:	X version of 0verkill
Summary(pl):	Wersja 0verkill pod X
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description x11
This package allows you to run an 0verkill client in an X window.

%description x11 -l pl
Ten pakiet pozwala na uruchomienie klienta 0verkill w oknie X.

%prep
%setup -q
%patch -p1

%build
aclocal
%{__autoconf}
%configure
%{__make}
%{__make} x0verkill XLIBS="-L/usr/X11R6/lib -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{grx,data},%{_x11bindir}}

install 0verkill avi $RPM_BUILD_ROOT%{_bindir}
install x0verkill $RPM_BUILD_ROOT%{_x11bindir}
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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_x11bindir}/*

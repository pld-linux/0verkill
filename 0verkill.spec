Summary:	0verkill - ASCII-art multiplayer game 
Summary(pl):	0verkill - gra multiplayer w ASCII
Name:		0verkill
Version:	0.15
Release:	2
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	http://artax.karlin.mff.cuni.cz/~brain/%{name}/release/%{name}-%{version}.tgz
Patch0:		%{name}-datadir.patch
URL:		http://artax.karlin.mff.cuni.cz/~brain/%{name}/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-devel

%description
0verkill is an ASCII-art multiplayer shooting game.

%description -l pl
0verkill jest strzelank± multiplayer z grafik± ASCII.

%prep
%setup -q
%patch -p1

%build
aclocal
autoconf
%configure 
%{__make}
%{__make} x0verkill XLIBS="-L%{_prefix}/X11R6/lib -lX11"

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{grx,data}}
%{__install} x0verkill 0verkill avi $RPM_BUILD_ROOT%{_bindir}
%{__install} server $RPM_BUILD_ROOT%{_bindir}/0verkill-server
%{__install} test_server $RPM_BUILD_ROOT%{_bindir}/0verkill-test_server
%{__install} bot $RPM_BUILD_ROOT%{_bindir}/0verkill-bot
for l in data/* ; do 
	sed -e 's@grx/@%{_datadir}/0verkill/grx/@' < $l >  $RPM_BUILD_ROOT%{_datadir}/%{name}/$l
done
%{__install} grx/* $RPM_BUILD_ROOT%{_datadir}/%{name}/grx 

gzip -9nf doc/AUTHORS doc/CHANGELOG doc/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/AUTHORS.gz doc/CHANGELOG.gz doc/*.html doc/*.txt.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

Summary:	0verkill - ASCII-art multiplayer game 
Name:		0verkill
Version:	0.15
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://artax.karlin.mff.cuni.cz/~brain/%{name}/release/%{name}-%{version}.tgz
Patch0:		%{name}-datadir.patch
URL:		http://artax.karlin.mff.cuni.cz/~brain/%{name}/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
0verkill is an ASCII-art multiplayer shooting game

%prep
%setup -q
%patch -p1

%build
%configure 
%{__make}
%{__make} x0verkill XLIBS="-L/usr/X11R6/lib -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{grx,data}}
install x0verkill 0verkill avi $RPM_BUILD_ROOT%{_bindir}
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
%doc doc/AUTHORS doc/CHANGELOG doc/*.html doc/*.txt 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*

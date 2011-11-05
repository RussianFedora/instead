Summary:	Simple text adventures/visual novels engine and game
Name:		instead
Version:	1.5.2
Release:	1%{?dist}.R

URL:		http://instead.googlecode.com
License:	GPLv2
Group:		Amusements/Games
Source0:	http://instead.googlecode.com/files/%{name}_%{version}.tar.gz
Source1:	%{name}.desktop
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	lua-devel

%description 
Simple text adventures/visual novels engine and game
Visual novel/text quest-like game in Russian with engine.

%prep
%setup -q

%build
# Hm, bash configure, great!!!
echo -e "2\n\/usr" | ./configure.sh
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/
strip $RPM_BUILD_ROOT%{_bindir}/sdl-%{name}
rm $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_bindir}/sdl-%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/modules doc/index.html doc/instead.txt doc/manual.pdf doc/writing_games*
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man6/%{name}.6.*

%changelog
* Sun Nov  6 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 1.5.2-1.R
- validate spec and binary packages

* Sun Oct 10 2011 Peter Kosyh <p.kosyh@gmail.com> - 1.5.2-1
- bug fix in release kbd event
- improved motion mode
- align in float gfx mode


Summary:	Simple text adventures/visual novels engine and game
Name:		instead
Version:	2.0.3
Release:	1%{?dist}

URL:		http://instead.syscall.ru/
License:	GPLv2
Group:		Amusements/Games
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_%{version}.tar.gz

BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	compat-lua-devel
BuildRequires:	desktop-file-utils

%description 
Simple text adventures/visual novels engine and game
Visual novel/text quest-like game in Russian with engine.

%prep
%setup -q
echo '#!/bin/bash' > configure
chmod +x configure

%build
#patch lua and install path
sed -e 's/lua5/lua-5/' -e 's/\/local//' -i Rules.make.system
rm Rules.make
ln -s Rules.make.system Rules.make
%configure
make clean
make %{?_smp_mflags} 

%install
%make_install
desktop-file-install                       \
--delete-original                          \
--set-key=Exec --set-value=instead         \
--remove-key=Encoding                      \
--remove-key=Version                       \
--dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/%{name}.desktop

rm %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_bindir}/sdl-%{name} %{buildroot}%{_bindir}/%{name}
rm -rf %{buildroot}%{_docdir}

%files
%doc doc/examples doc/index.html doc/instead*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man6/%{name}.6.*

%changelog
* Wed Mar 26 2014 Ivan Epifanov <isage.dna@gmail.com> - 2.0.3-1.R
- update to 2.0.3

* Sun Nov  6 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 1.5.2-1.R
- validate spec and binary packages

* Mon Oct 10 2011 Peter Kosyh <p.kosyh@gmail.com> - 1.5.2-1
- bug fix in release kbd event
- improved motion mode
- align in float gfx mode


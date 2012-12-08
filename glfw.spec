Summary:	An OpenGL Framework
Name:		glfw
Version:	2.6
Release:	6
URL:		http://glfw.sourceforge.net/
License:	BSD
Source0:	http://ovh.dl.sourceforge.net/sourceforge/glfw/%{name}-%{version}.tar.bz2
Patch0:		glfw-2.6-installdir.patch
Group:		System/Libraries
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(xrandr)

%description
GLFW is a portable framework for OpenGL application development.
It handles operating system specific tasks, such OpenGL window management,
keyboard, mouse and joystick input, reding a high precision timer,
creating threads, and more.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
make x11 CC="gcc %{optflags} %{ldflags}"

%install
make x11-install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}

%files
%doc docs/* license.txt readme.html
%{_libdir}/*.a
%{_includedir}/*
%{_libdir}/pkgconfig/*


%changelog
* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 2.6-5mdv2011.0
+ Revision: 635843
- tighten BR

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6-4mdv2011.0
+ Revision: 618961
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.6-3mdv2010.0
+ Revision: 429210
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.6-2mdv2009.0
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Funda Wang <fwang@mandriva.org> 2.6-2mdv2008.0
+ Revision: 78049
- fix libdir of pkgconfig

* Sun Sep 02 2007 Funda Wang <fwang@mandriva.org> 2.6-1mdv2008.0
+ Revision: 78047
- add install dir patch
- New version 2.6

* Mon Jun 18 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.5.0-4mdv2008.0
+ Revision: 41063
- rebuild
- Import glfw



* Thu Aug 18 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.5.0-3mdk
- fix buildrequires

* Wed Aug 10 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.5.0-2mdk
- fix incredible suckage!!

* Wed Aug 10 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.5.0-1mdk
- Initial build.

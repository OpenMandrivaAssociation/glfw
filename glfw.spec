%define	name	glfw
%define version 2.6
%define release 4

Summary:	An OpenGL Framework
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
URL:		http://glfw.sourceforge.net/
License:	BSD
Source0:	http://ovh.dl.sourceforge.net/sourceforge/glfw/%{name}-%{version}.tar.bz2
Patch0:		glfw-2.6-installdir.patch
Group:		System/Libraries
BuildRequires:	X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GLFW is a portable framework for OpenGL application development.
It handles operating system specific tasks, such OpenGL window management,
keyboard, mouse and joystick input, reding a high precision timer,
creating threads, and more.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
make x11

%install
rm -rf %{buildroot}
make x11-install DESTDIR=%buildroot PREFIX=%_prefix LIBDIR=%_libdir

%clean
rm -rf %{buildroot}

%files
%doc docs/* examples license.txt readme.html
%{_libdir}/*.a
%{_includedir}/*
%{_libdir}/pkgconfig/*

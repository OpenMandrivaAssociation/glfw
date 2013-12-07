%define debug_package %{nil}
%define major	%(echo %{version}|cut -d. -f1,1)
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	An OpenGL Framework
Name:		glfw
Version:	2.7.8
Release:	4
License:	BSD
Group:		System/Libraries
Url:		http://glfw.sourceforge.net/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/glfw/%{name}-%{version}.tar.bz2
Patch0:		glfw-2.6-installdir.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(xrandr)

%description
GLFW is a portable framework for OpenGL application development.
It handles operating system specific tasks, such OpenGL window management,
keyboard, mouse and joystick input, reding a high precision timer,
creating threads, and more.

%package -n %{libname}
Summary:	Main library for gupnp
Group:		System/Libraries
%rename		%{name}

%description -n %{libname}
GLFW is a portable framework for OpenGL application development.
It handles operating system specific tasks, such OpenGL window management,
keyboard, mouse and joystick input, reding a high precision timer,
creating threads, and more.

This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development filescw for %{name}.

%prep
%setup -q
%patch0 -p0

%build
sh ./compile.sh

%make x11 CC=gcc %{ldflags} SOFLAGS="-shared -Wl,-soname,libglfw.so.%{major}"

%install
make x11-install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir}

# this is copied from opensuse
install -D -m0755 lib/x11/libglfw.so %{buildroot}%{_libdir}/libglfw.so.%{version}
ln -s libglfw.so.%{version} %{buildroot}%{_libdir}/libglfw.so.%{major}
ln -s libglfw.so.%{version} %{buildroot}%{_libdir}/libglfw.so

# remove static lib
rm -f %{buildroot}%{_libdir}/libglfw.a

%files -n %{libname}
%{_libdir}/libglfw.so.%{major}*

%files -n %{devname}
%doc docs/* COPYING.txt readme.html
%{_libdir}/libglfw.so
%{_includedir}/*
%{_libdir}/pkgconfig/*


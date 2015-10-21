%define debug_package %{nil}
%define major	%(echo %{version}|cut -d. -f1,1)
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	An OpenGL Framework
Name:		glfw
Version:	3.1.2
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://www.glfw.org/
Source0:	https://github.com/glfw/glfw/releases/download/%{version}/glfw-%{version}.zip
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	cmake

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
%apply_patches

%build
%cmake -DGLFW_BUILD_EXAMPLES:BOOL=OFF \
       -DGLFW_BUILD_TESTS:BOOL=OFF
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libglfw.so.%{major}*

%files -n %{devname}
%doc docs/* COPYING.txt
%{_libdir}/libglfw.so
%{_libdir}/cmake/%{name}
%{_includedir}/*
%{_libdir}/pkgconfig/*


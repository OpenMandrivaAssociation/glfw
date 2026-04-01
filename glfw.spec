%define _empty_manifest_terminate_build 0
%define major	%(echo %{version}|cut -d. -f1,1)
%define	oldlibname	%mklibname %{name} 3
%define	libname	%mklibname %{name}
%define	devname	%mklibname %{name} -d

%ifarch %{x86_64}
%bcond_without compat32
%define lib32name %mklib32name %{name}
%define dev32name %mklib32name %{name} -d
%endif

Summary:	An OpenGL Framework
Name:		glfw
Version:	3.4
Release:	2
License:	BSD
Group:		System/Libraries
Url:		https://www.glfw.org/
Source0:	https://github.com/glfw/glfw/releases/download/%{version}/glfw-%{version}.zip
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	gettext
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  egl-wayland
BuildRequires:  wayland-tools
BuildSystem:	cmake
BuildOption:	-DGLFW_BUILD_EXAMPLES:BOOL=OFF
BuildOption:	-DGLFW_BUILD_TESTS:BOOL=OFF

%description
GLFW is a portable framework for OpenGL application development.
It handles operating system specific tasks, such OpenGL window management,
keyboard, mouse and joystick input, reding a high precision timer,
creating threads, and more.

%package -n %{libname}
Summary:	GLFW OpenGL Framework library
Group:		System/Libraries
%rename		%{name}
# Renamed 2026/04/01 after 6.0
%rename		%{oldlibname}

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
This package contains the development files for %{name}.

%package -n %{lib32name}
Summary:	GLFW OpenGL Framework Library (32-bit)
Group:		System/Libraries
%rename		%{name}
# Renamed 2026/04/01 after 6.0
%rename		%{oldlibname}

%description -n %{lib32name}
GLFW is a portable framework for OpenGL application development.
It handles operating system specific tasks, such OpenGL window management,
keyboard, mouse and joystick input, reding a high precision timer,
creating threads, and more.

This package contains the 32-bit shared library for %{name}.

%package -n %{dev32name}
Summary:	Headers for developing programs that will use %{name} (32-bit)
Group:		Development/C++
Requires:	%{lib32name} = %{version}-%{release}
Provides:	%{devname} = %{version}-%{release}

%description -n %{dev32name}
This package contains the development files for %{name} (32-bit).

%prep
%autosetup -p1

%install -p
# FIXME the CMake files assume BUILDDIR==SOURCEDIR
# and therefore want to copy prebuilt docs from BUILDDIR
# For now, let's just put them where they're expected.
[ -d _OMV_rpm_build32 ] && cp -a docs/html _OMV_rpm_build32/docs/
cp -a docs/html _OMV_rpm_build/docs/

%files -n %{libname}
%{_libdir}/libglfw.so.%{major}*

%files -n %{devname}
%doc %{_docdir}/GLFW
%{_libdir}/libglfw.so
%{_libdir}/cmake/%{name}3
%{_includedir}/*
%{_libdir}/pkgconfig/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libglfw.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libglfw.so
%{_prefix}/lib/cmake/%{name}3
%{_prefix}/lib/pkgconfig/*
%endif

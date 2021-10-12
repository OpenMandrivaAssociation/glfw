%define _empty_manifest_terminate_build 0
%define major	%(echo %{version}|cut -d. -f1,1)
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	An OpenGL Framework
Name:		glfw
Version:	3.3.4
Release:	2
License:	BSD
Group:		System/Libraries
Url:		http://www.glfw.org/
Source0:	https://github.com/glfw/glfw/releases/download/%{version}/glfw-%{version}.zip
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)

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
%autopatch -p1

%build
%cmake -DGLFW_BUILD_EXAMPLES:BOOL=OFF \
       -DGLFW_BUILD_TESTS:BOOL=OFF
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libglfw.so.%{major}*

%files -n %{devname}
%doc docs/*
%{_libdir}/libglfw.so
%{_libdir}/cmake/%{name}3
%{_includedir}/*
%{_libdir}/pkgconfig/*

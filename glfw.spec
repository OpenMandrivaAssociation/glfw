%define	name	glfw
%define version 2.5.0
%define release 3

Summary:	An OpenGL Framework
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
URL:		http://glfw.sourceforge.net/
License:	BSD
Source0:	http://ovh.dl.sourceforge.net/sourceforge/glfw/%{name}-%{version}.tar.bz2
Group:		System/Libraries
BuildRequires:	X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GLFW is a portable framework for OpenGL application development.
It handles operating system specific tasks, such OpenGL window management,
keyboard, mouse and joystick input, reding a high precision timer,
creating threads, and more.

%prep
%setup -q -n %{name}-2.5

%build
./compile.sh
perl -pi -e "s#-Os#$RPM_OPT_FLAGS -O3 -ffast-math#" lib/x11/Makefile.x11
%make -C lib/x11/ -f Makefile.x11

%install
rm -rf %{buildroot}
install -m644 ./lib/x11/libglfw.a -D $RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/libglfw.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc docs/* examples license.txt readme.html
%{_prefix}/X11R6/%{_lib}/libglfw.a

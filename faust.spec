%define debug_package %{nil}

Summary:	Faust AUdio Stream (real-time audio signal processing language)

Name:		faust
Version:	2.27.2
Release:	1
License:	GPLv2+ and BSD
Group:		Development/Other
Url:		http://faust.grame.fr/
Source0:	https://github.com/grame-cncm/faust/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	faust.rpmlintrc
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	cmake
Requires:	glitz
Suggests:	jackit
Suggests:	csound
Suggests:	octave

%description
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. Its programming model combines two approaches : functional
programming and block diagram composition. You can think of FAUST as a
structured block diagram language with a textual syntax.

FAUST is intended for developers who need to develop efficient C/C++ audio
plugins for existing systems or full standalone audio applications. Thanks to
some specific compilation techniques and powerful optimizations, the C++ code
generated by the Faust compiler is usually very fast. It can generally compete
with (and sometimes outperform) hand-written C code.

Programming with FAUST is somehow like working with electronic circuits and
signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram: a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters)

%files
%doc COPYING README examples
%{_bindir}/%{name}
%{_bindir}/%{name}path
%{_bindir}/%{name}optflags
%{_libdir}/%{name}
%{_includedir}/%{name}

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}

License:	GPLv2+
Group:		Development/Other
BuildArch:	noarch

%description doc
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. This package provides documentation files to help with
writing programs with faust.

%files doc
%doc documentation/*
%doc dox

#----------------------------------------------------------------------------

%package tools
Summary:	3rd party tools written for %{name}

License:	GPLv2+
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description tools
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. These additional tools are provided by various contributors
to help the building process of applications and plugins with Faust.

%files tools
%doc tools/README README.supercollider README.appls
%{_bindir}/%{name}2*

#----------------------------------------------------------------------------

%package kate
Summary:	Kate/Kwrite plugin for %{name}

License:	GPLv2+
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description kate
Faust AUdio STreams is a functional programming language for real-time audio
signal processing. This package provides Faust code syntax highlighting support
for KDE's Kate/Kwrite.

%files kate
%doc syntax-highlighting/README
%{_datadir}/kde4/apps/katepart/syntax/%{name}.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
pushd build
%cmake

%make_build

popd

%install
%make_install -C build

# remove the android lib
rm -fr %{buildroot}%{_libdir}/faust/android/
rm -fr %{buildroot}%{_libdir}/faust/iOS/
rm -fr %{buildroot}%{_libdir}/faust/iPhone/



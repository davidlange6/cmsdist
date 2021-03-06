### RPM external ktjet 1.06
Source: http://www.hepforge.org/archive/ktjet/KtJet-%{realversion}.tar.gz
Patch1: ktjet-1.0.6-nobanner
Requires: clhep

%define keep_archives true

%if "%{?cms_cxx:set}" != "set"
%define cms_cxx g++
%endif

%if "%{?cms_cxxflags:set}" != "set"
%define cms_cxxflags -std=c++0x
%endif

%prep
%setup -n KtJet-%{realversion}
%patch1 -p1

%build
CPPFLAGS=" -DKTDOUBLEPRECISION -fPIC %cms_cxxflags" CXX="%cms_cxx" ./configure --with-clhep=$CLHEP_ROOT --prefix=%{i}
make

### RPM external rivet 1.8.2
Source: http://www.hepforge.org/archive/rivet/Rivet-%{realversion}.tar.gz

Requires: hepmc boost fastjet swig gsl
Requires: python
Patch0: rivet-1.4.0
Patch1: rivet-1.8.2-fix-isnan
Patch2: rivet-1.8.2-fix-duplicate-symbols
Patch3: rivet-1.8.2-disable-doc

%if "%{?cms_cxx:set}" != "set"
%define cms_cxx g++
%endif

%if "%{?cms_cxxflags:set}" != "set"
%define cms_cxxflags -O2 -std=c++0x
%endif

%prep
%setup -n Rivet-%{realversion}
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
./configure --disable-silent-rules --prefix=%i --with-boost=${BOOST_ROOT} --with-hepmc=$HEPMC_ROOT \
            --with-fastjet=$FASTJET_ROOT --with-gsl=$GSL_ROOT --disable-doxygen --disable-pdfmanual --with-pic \
            CXX="$(which %cms_cxx)" CXXFLAGS="%cms_cxxflags"
# The following hack insures that the bins with the library linked explicitly
# rather than indirectly, as required by the gold linker
perl -p -i -e "s|LIBS = $|LIBS = -lHepMC|g" bin/Makefile
%build
make %makeprocesses
%install
make install

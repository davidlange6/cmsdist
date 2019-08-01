### RPM external python_tools 2.0
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}
## INITENV +PATH PYTHON3PATH %{i}/${PYTHON3_LIB_SITE_PACKAGES}
Source: none
 
Requires: root curl python python3 xrootd llvm hdf5

%define isslc7 %(case %{cmsplatf} in (slc7_amd64*) echo 1 ;; (*) echo 0 ;; esac)
%define isamd64 %(case %{cmsplatf} in (*amd64*) echo 1 ;; (*) echo 0 ;; esac)
Requires: py2-scipy
Requires: py2-Keras
Requires: py2-Theano
Requires: py2-scikit-learn
Requires: py2-rootpy
Requires: py2-tensorflow
Requires: py2-googlePackages

Requires: py2-tables
Requires: py2-numexpr
Requires: py2-histogrammar
Requires: py2-pandas
Requires: py2-root_numpy
Requires: py2-Bottleneck
Requires: py2-downhill 
Requires: py2-theanets
Requires: py2-xgboost
Requires: py2-llvmlite
Requires: py2-numba
Requires: py2-hep_ml
Requires: py2-rep
Requires: py2-uncertainties
Requires: py2-hyperas
Requires: py2-hyperopt
Requires: py2-seaborn
Requires: py2-h5py
Requires: py2-h5py-cache
Requires: py2-thriftpy
Requires: py2-root_pandas
Requires: py2-uproot
Requires: py2-oamap

#this DOES NOT depend on numpy..
Requires: py2-xrootdpyfs

Requires: root curl python openldap

Requires: py2-entrypoints
Requires: py2-psutil
Requires: py2-repoze-lru
Requires: py2-Jinja2
Requires: py2-MarkupSafe
Requires: py2-Pygments
Requires: py2-appdirs
Requires: py2-argparse
Requires: py2-bleach
Requires: py2-certifi
Requires: py2-decorator
Requires: py2-html5lib
Requires: py2-ipykernel
Requires: py2-ipython
Requires: py2-ipython_genutils
Requires: py2-ipywidgets
Requires: py2-jsonschema
Requires: py2-jupyter
Requires: py2-jupyter_client
Requires: py2-jupyter_console
Requires: py2-jupyter_core
Requires: py2-mistune
Requires: py2-nbconvert
Requires: py2-nbformat
Requires: py2-notebook
Requires: py2-ordereddict
Requires: py2-packaging
Requires: py2-pandocfilters
Requires: py2-pathlib2
Requires: py2-pexpect
Requires: py2-pickleshare
Requires: py2-prompt_toolkit
Requires: py2-ptyprocess
Requires: py2-pyparsing
Requires: py2-pyzmq
Requires: py2-qtconsole
Requires: py2-scandir
Requires: py2-setuptools
Requires: py2-simplegeneric
Requires: py2-singledispatch
Requires: py2-six
Requires: py2-terminado
Requires: py2-testpath
Requires: py2-tornado
Requires: py2-traitlets
Requires: py2-wcwidth
Requires: py2-webencodings
Requires: py2-widgetsnbextension
Requires: py2-cycler
Requires: py2-docopt
Requires: py2-futures
Requires: py2-networkx
Requires: py2-parsimonious
Requires: py2-prettytable
Requires: py2-pycurl
Requires: py2-pytz
Requires: py2-requests
Requires: py2-schema
#Requires: py2-Jinja
Requires: py2-python-dateutil
Requires: py2-python-cjson
Requires: py2-enum34 
Requires: py2-functools32
Requires: py2-mock
Requires: py2-pbr
Requires: py2-mpmath
Requires: py2-sympy
Requires: py2-tqdm
Requires: py2-funcsigs
Requires: py2-nose
Requires: py2-pkgconfig
Requires: py2-pysqlite
Requires: py2-Click
Requires: py2-jsonpickle
Requires: py2-prwlock
Requires: py2-virtualenv
Requires: py2-virtualenvwrapper
Requires: py2-urllib3
Requires: py2-chardet
Requires: py2-idna
Requires: py2-Werkzeug
Requires: py2-pytest
Requires: py2-avro
Requires: py2-fs
Requires: py2-lizard
Requires: py2-flawfinder
Requires: py2-python-ldap
Requires: py2-plac

Requires: py2-matplotlib
Requires: py2-numpy-toolfile
Requires: py2-sqlalchemy
Requires: py2-pygithub
Requires: py2-dablooms-toolfile
Requires: py2-dxr-toolfile
Requires: py2-PyYAML
Requires: py2-pylint
Requires: py2-pip
%if %isamd64
Requires: py2-cx-oracle
%endif
Requires: py2-cython
Requires: py2-future
Requires: py2-pybind11-toolfile
Requires: py2-histbook
Requires: py2-flake8
Requires: py2-autopep8
Requires: py2-pycodestyle
Requires: py2-lz4
Requires: py2-ply
Requires: py2-py
Requires: py2-typing
Requires: py2-defusedxml
Requires: py2-atomicwrites
Requires: py2-attrs
Requires: py2-nbdime
Requires: py2-onnx
Requires: py2-backports
Requires: py2-backports_abc
Requires: py2-colorama
Requires: py2-lxml
Requires: py2-beautifulsoup4
Requires: py2-GitPython
Requires: py2-Send2Trash
Requires: py2-gitdb2
Requires: py2-ipaddress
Requires: py2-mccabe
Requires: py2-more-itertools
Requires: py2-pluggy
Requires: py2-prometheus_client
Requires: py2-pyasn1-modules
Requires: py2-pyasn1
Requires: py2-pyflakes
Requires: py2-python-ldap
Requires: py2-smmap2
Requires: py2-stevedore
Requires: py2-typing_extensions
Requires: py2-virtualenv-clone
Requires: py2-asn1crypto
Requires: py2-backcall
Requires: py2-cffi
Requires: py2-cryptography
Requires: py2-google-common
Requires: py2-jedi
Requires: py2-parso
Requires: py2-pycparser
Requires: py2-absl-py
Requires: py2-gast
Requires: py2-grpcio
Requires: py2-Markdown
Requires: py2-subprocess32
Requires: py2-kiwisolver
Requires: py2-pyOpenSSL
Requires: py2-bokeh
Requires: py2-climate
Requires: py2-mpld3
Requires: py2-neurolab
Requires: py2-nose-parameterized
Requires: py2-pillow
Requires: py2-pybrain
Requires: py2-pymongo
Requires: py2-pydot

Requires: py2-astroid
Requires: py2-coverage
Requires: py2-hepdata-lib
Requires: py2-isort
Requires: py2-lazy-object-proxy
Requires: py2-pylint
Requires: py2-pytest-cov
Requires: py2-wrapt

Requires: py3-absl-py
Requires: py3-appdirs
Requires: py3-argparse
Requires: py3-asn1crypto
Requires: py3-astroid
Requires: py3-atomicwrites
Requires: py3-attrs
Requires: py3-autopep8
Requires: py3-avro
Requires: py3-awkward
Requires: py3-backcall
Requires: py3-backports_abc
Requires: py3-backports-functools_lru_cache
Requires: py3-backports-shutil_get_terminal_size
Requires: py3-backports-shutil_which
Requires: py3-backports-ssl_match_hostname
Requires: py3-backports-weakref
Requires: py3-beautifulsoup4
Requires: py3-bleach
Requires: py3-bokeh
Requires: py3-Bottleneck
Requires: py3-cachetools
Requires: py3-certifi
Requires: py3-cffi
Requires: py3-chardet
Requires: py3-Click
Requires: py3-climate
Requires: py3-cmstest
Requires: py3-colorama
Requires: py3-configparser
Requires: py3-contextlib2
Requires: py3-coverage
Requires: py3-cryptography
Requires: py3-cycler
Requires: py3-cython
Requires: py3-decorator
Requires: py3-defusedxml
Requires: py3-docopt
Requires: py3-downhill
Requires: py3-entrypoints
Requires: py3-flake8
Requires: py3-flawfinder
Requires: py3-fs
Requires: py3-funcsigs
Requires: py3-future
Requires: py3-gast
Requires: py3-gitdb2
Requires: py3-GitPython
Requires: py3-google-common
Requires: py3-grpcio
Requires: py3-h5py-cache
Requires: py3-h5py
Requires: py3-hep_ml
Requires: py3-histbook
Requires: py3-histogrammar
Requires: py3-html5lib
Requires: py3-hyperas
Requires: py3-hyperopt
Requires: py3-idna
Requires: py3-ipaddress
Requires: py3-ipykernel
Requires: py3-ipython_genutils
Requires: py3-ipython
Requires: py3-ipywidgets
Requires: py3-isort
Requires: py3-jedi
Requires: py3-Jinja2
Requires: py3-jsonpickle
Requires: py3-jsonschema
Requires: py3-jupyter_client
Requires: py3-jupyter_console
Requires: py3-jupyter_core
Requires: py3-jupyter
Requires: py3-Keras
Requires: py3-keras-applications
Requires: py3-keras-preprocessing
Requires: py3-kiwisolver
Requires: py3-lazy-object-proxy
Requires: py3-lizard
Requires: py3-llvmlite
Requires: py3-lxml
Requires: py3-lz4
Requires: py3-Mako
Requires: py3-Markdown
Requires: py3-MarkupSafe
Requires: py3-mccabe
Requires: py3-mistune
Requires: py3-mock
Requires: py3-more-itertools
Requires: py3-mpld3
Requires: py3-mpmath
Requires: py3-nbconvert
Requires: py3-nbdime
Requires: py3-nbformat
Requires: py3-networkx
Requires: py3-neurolab
Requires: py3-nose-parameterized
Requires: py3-nose
Requires: py3-notebook
Requires: py3-numba
Requires: py3-numexpr
Requires: py3-onnx
Requires: py3-ordereddict
Requires: py3-packaging
Requires: py3-pandas
Requires: py3-pandocfilters
Requires: py3-parsimonious
Requires: py3-parso
Requires: py3-pathlib2
Requires: py3-pbr
Requires: py3-pexpect
Requires: py3-pickleshare
Requires: py3-pillow
Requires: py3-pkgconfig
Requires: py3-plac
Requires: py3-pluggy
Requires: py3-ply
Requires: py3-prettytable
Requires: py3-prometheus_client
Requires: py3-prompt_toolkit
Requires: py3-protobuf
Requires: py3-prwlock
Requires: py3-psutil
Requires: py3-ptyprocess
Requires: py3-pyasn1-modules
Requires: py3-pyasn1
Requires: py3-pybind11
Requires: py3-pybrain
Requires: py3-pycodestyle
Requires: py3-pycparser
Requires: py3-pycuda
Requires: py3-pycurl
Requires: py3-pydot
Requires: py3-pyflakes
Requires: py3-Pygments
Requires: py3-pylint
Requires: py3-pymongo
Requires: py3-pyOpenSSL
Requires: py3-pyparsing
Requires: py3-py
Requires: py3-pytest
Requires: py3-pytest-cov
Requires: py3-python-dateutil
Requires: py3-python-ldap
Requires: py3-pytools
Requires: py3-pytz
Requires: py3-PyYAML
Requires: py3-pyzmq
Requires: py3-qtconsole
Requires: py3-repoze-lru
Requires: py3-rep
Requires: py3-requests
Requires: py3-scandir
Requires: py3-schema
Requires: py3-scikit-learn
Requires: py3-scipy
Requires: py3-seaborn
Requires: py3-Send2Trash
Requires: py3-simplegeneric
Requires: py3-singledispatch
Requires: py3-six
Requires: py3-smmap2
Requires: py3-soupsieve
Requires: py3-stevedore
Requires: py3-subprocess32
Requires: py3-sympy
Requires: py3-tables
Requires: py3-terminado
Requires: py3-testpath
Requires: py3-theanets
Requires: py3-Theano
Requires: py3-thriftpy
Requires: py3-tornado
Requires: py3-tqdm
Requires: py3-traitlets
Requires: py3-typing_extensions
Requires: py3-typing
Requires: py3-uncertainties
Requires: py3-uproot-methods
Requires: py3-urllib3
Requires: py3-virtualenv-clone
Requires: py3-virtualenv
Requires: py3-virtualenvwrapper
Requires: py3-wcwidth
Requires: py3-webencodings
Requires: py3-Werkzeug
Requires: py3-wheel
Requires: py3-widgetsnbextension
Requires: py3-wrapt
Requires: py3-xgboost
Requires: py3-sqlalchemy


%prep

%build

%install
mkdir -p %{i}/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/python_tools.xml
<tool name="%{n}" version="%{v}">
</tool>
EOF_TOOLFILE


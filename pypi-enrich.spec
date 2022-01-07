#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-enrich
Version  : 1.2.6
Release  : 3
URL      : https://files.pythonhosted.org/packages/47/2b/b453d52a5cd1409d859d67c6a530971095406aedc0c0589c1c6a5212f506/enrich-1.2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/2b/b453d52a5cd1409d859d67c6a530971095406aedc0c0589c1c6a5212f506/enrich-1.2.6.tar.gz
Summary  : enrich
Group    : Development/Tools
License  : MIT
Requires: pypi-enrich-python = %{version}-%{release}
Requires: pypi-enrich-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(pip)
BuildRequires : pypi(rich)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
# enrich
Enriched extends [rich](https://pypi.org/project/rich/) library functionality
with a set of changes that were not accepted to rich itself.

%package python
Summary: python components for the pypi-enrich package.
Group: Default
Requires: pypi-enrich-python3 = %{version}-%{release}

%description python
python components for the pypi-enrich package.


%package python3
Summary: python3 components for the pypi-enrich package.
Group: Default
Requires: python3-core
Provides: pypi(enrich)
Requires: pypi(rich)

%description python3
python3 components for the pypi-enrich package.


%prep
%setup -q -n enrich-1.2.6
cd %{_builddir}/enrich-1.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639056742
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
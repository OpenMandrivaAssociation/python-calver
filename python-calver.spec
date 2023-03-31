Name:		python-calver
Version:	2022.6.26
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/calver/calver-%{version}.tar.gz
Summary:	Setuptools extension for CalVer package versions
URL:		https://pypi.org/project/calver/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Setuptools extension for CalVer package versions

%prep
%autosetup -p1 -n calver-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/calver
%{py_sitedir}/calver-*.*-info

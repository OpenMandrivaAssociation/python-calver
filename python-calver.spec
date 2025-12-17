Name:		python-calver
Version:	2025.10.20
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/calver/calver-%{version}.tar.gz
Summary:	Setuptools extension for CalVer package versions
URL:		https://pypi.org/project/calver/
License:	GPL
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Setuptools extension for CalVer package versions

%files
%{py_sitedir}/calver
%{py_sitedir}/calver-%{version}.dist-info

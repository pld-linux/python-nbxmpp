#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		nbxmpp
Summary:	Non blocking Jabber/XMPP module
Name:		python-nbxmpp
Version:	0.6.6
Release:	1
License:	GPL v3
Group:		Libraries/Python
# https://dev.gajim.org/gajim/python-nbxmpp/tags
Source0:	https://files.pythonhosted.org/packages/source/n/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	e9e0ba25282c892c7618014bbf93244d
URL:		https://dev.gajim.org/gajim/python-nbxmpp
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-pyOpenSSL
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-nbxmpp is a Python library that provides a way for Python
applications to use Jabber/XMPP networks in a non-blocking way. This
library is initialy a fork of xmpppy one, but using non-blocking
sockets.

%package -n python3-%{module}
Summary:	Non blocking Jabber/XMPP module
Group:		Libraries/Python
Requires:	python3-pyOpenSSL

%description -n python3-%{module}
python-nbxmpp is a Python library that provides a way for Python
applications to use Jabber/XMPP networks in a non-blocking way. This
library is initialy a fork of xmpppy one, but using non-blocking
sockets.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ChangeLog README
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

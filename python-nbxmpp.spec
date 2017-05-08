
%define		module		nbxmpp
Summary:	Non blocking Jabber/XMPP module
Name:		python-nbxmpp
Version:	0.5.5
Release:	1
License:	GPL v3
Group:		Libraries/Python
# https://dev.gajim.org/gajim/python-nbxmpp/tags
Source0:	https://dev.gajim.org/gajim/python-nbxmpp/uploads/ddc27304794916539c0c7b7ca71413a5/nbxmpp-%{version}.tar.gz
# Source0-md5:	d72008dd1b3fb471b72b1272c58a79dc
URL:		https://dev.gajim.org/gajim/python-nbxmpp
BuildRequires:	python-modules
BuildRequires:	python-setuptools
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

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

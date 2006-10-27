
%define	module	TurboMail

Summary:	Multi-threaded mail queue manager for TurboGears applications
Name:		python-TurboMail
Version:	2.0
Release:	1
License:	need check
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/T/TurboMail/TurboMail-%{version}.tar.gz
# Source0-md5:	c1b480702e3a76964fda8c3662e0c915
URL:		http://www.topfloor.ca/turbomail/
%pyrequires_eq	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6a9
BuildRequires:	python-TurboGears
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TurboMail is a TurboGears extension - meaning that it starts up and shuts down
alongside TurboGears applications you write in the same way that visit tracking
and identity do. TurboMail uses built-in Python modules for SMTP communication
and MIME e-mail creation, but greatly simplifies these tasks by performing the
grunt-work for you.

%prep
%setup -q -n %{module}-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d build/scripts-%{py_ver}
python ./setup.py install \
        --single-version-externally-managed \
        --optimize 2 \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/turbomail

# Python
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           crepo
Version:        0.1.8
Release:        1%{?dist}
Summary:        Multiple repositories management tool for git based projects
Group:          Development/Tools
License:        ASL 2.0 
URL:            http://github.com/cloudera/crepo/
# The source for this package was pulled from upstream's vcs.
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXX)

# Some issues with old suse
%if %{?suse_version: %{suse_version} > 1110} %{!?suse_version:1}
BuildArch:      noarch
%endif

%if %{defined suse_version}
BuildRequires:  python, python-setuptools
Requires:       python
%else
BuildRequires:  python, python-setuptools, python-simplejson
Requires:       python, python-simplejson
%endif


%description
Crepo is a lightweight git repository management tool similar to Google's "repo" tool.
Crepo makes it very easy to manage projects that pull together sources from multiple
remote repositories. In this respect, it is similar to sub-modules. However, it
avoids the direct integration with the git index which makes the use of 
sub-modules somewhat error prone, and also enables automatic tracking of remote
references without explicit commits to the containing repository.

%prep
%setup -q
chmod  644 bootstrap.py crepo/crepo.py setup.py test.py


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}

%if %{defined suse_version}
%{__python} setup.py install -O1 --skip-build --prefix=%{_prefix} --root %{buildroot} --record-rpm=INSTALLED_FILES
%else
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE PKG-INFO
%{_bindir}/%{name}
%{python_sitelib}/%{name}-%{version}-py*.egg-info/
%{python_sitelib}/%{name}/


%changelog
* Tue Jan 04 2011 Bruno Mahe <bruno@cloudera.com> - 0.1.8-2
- Make package working for Suse based distributions

* Thu Nov 11 2010 Bruno Mahe <bruno@cloudera.com> - 0.1.8-2
- Change permissions to 644

* Mon Oct 4 2010 Bruno Mahe <bruno@cloudera.com> - 0.1.8-1
- Initial package



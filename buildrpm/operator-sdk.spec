{{{$version := printf "%s.%s.%s" .major .minor .patch}}}
%global debug_package %{nil}

Name:		operator-sdk
Version:	{{{$version}}}
Release:	1%{?dist}
Summary:	A tookit for building Kubernetes Operators

License:	Apache License 2.0
URL:		https://github.com/operator-framework/operator-sdk
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	golang >= 1.15.5

%description
The Operator SDK is a set of tools that eases the creation of services that
follow the Kubernetes Operator pattern

%prep
%setup -q


%build
make build


%install
install -m 755 -d %{buildroot}/usr/bin
install -m 755 build/operator-sdk %{buildroot}/usr/bin/operator-sdk
install -m 755 build/helm-operator %{buildroot}/usr/bin/helm-operator
install -m 755 build/ansible-operator %{buildroot}/usr/bin/ansible-operator

%files
%license LICENSE THIRD_PARTY_LICENSES.txt

/usr/bin/operator-sdk
/usr/bin/helm-operator
/usr/bin/ansible-operator

%changelog
* Fri Mar 12 2021 Daniel Krasinski <daniel.krasinski@oracle.com> 1.4.2-1
* {{{.changelog-timestamp}}} - {{{$version}}}-1
- Initial Release


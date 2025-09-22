
%global debug_package %{nil}

%global _buildhost          build-ol%{?oraclelinux}-%{?_arch}.oracle.com

%ifarch %{arm} arm64 aarch64
%global arch aarch64
%else
%global arch x86_64
%endif

Name:		operator-sdk
Version:	1.28.0
Release:	1%{?dist}
Summary:	A tookit for building Kubernetes Operators

License:	Apache License 2.0
URL:		https://github.com/operator-framework/operator-sdk
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	golang >= 1.20.10

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
install -m 755 build/ansible-operator %{buildroot}/usr/bin/ansible-operator
install -m 755 build/helm-operator %{buildroot}/usr/bin/helm-operator

%files
%license LICENSE THIRD_PARTY_LICENSES.txt

/usr/bin/operator-sdk
/usr/bin/helm-operator
/usr/bin/ansible-operator

%changelog
* Mon Sep 22 2025 Olcne-Builder Jenkins <olcne-builder_us@oracle.com> - 1.28.0-1
- Initial Release


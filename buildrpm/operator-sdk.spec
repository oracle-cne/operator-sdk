{{{$version := printf "%s.%s.%s" .major .minor .patch}}}
%global debug_package %{nil}

%global _buildhost          build-ol%{?oraclelinux}-%{?_arch}.oracle.com

%ifarch %{arm} arm64 aarch64
%global arch aarch64
%else
%global arch x86_64
%endif

Name:		operator-sdk
Version:	{{{$version}}}
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
{{{- if semverCompare ">0.17.1" $version }}}
make build
{{{- else }}}
make build/operator-sdk-v0.17.1-2-gcd4373b2-%{arch}-linux-gnu
{{{- end }}}

%install
install -m 755 -d %{buildroot}/usr/bin
{{{- if semverCompare ">0.17.1" $version }}}
install -m 755 build/operator-sdk %{buildroot}/usr/bin/operator-sdk
install -m 755 build/ansible-operator %{buildroot}/usr/bin/ansible-operator
install -m 755 build/helm-operator %{buildroot}/usr/bin/helm-operator
{{{- else }}}
install -m 755 build/operator-sdk-v0.17.1-2-gcd4373b2-%{arch}-linux-gnu %{buildroot}/usr/bin/operator-sdk
{{{- end }}}

%files
%license LICENSE THIRD_PARTY_LICENSES.txt

/usr/bin/operator-sdk
/usr/bin/helm-operator
/usr/bin/ansible-operator

%changelog
* {{{.changelog_timestamp}}} - {{{$version}}}-1
- Initial Release


%define git 20130719git2e8fa9f

Name:           libclc
Version:        0.0.1
Release:        0.1.%{git}%{?dist}
Summary:        An open source implementation of the OpenCL 1.1 library requirements

License:        BSD
URL:            http://libclc.llvm.org/
# Created using:
# $ export PKG=libclc-$(date +%Y%m%d)git$(git describe --always) ; echo $PKG
# $ git archive --prefix $PKG/ --format tar HEAD | xz > $PKG.tar.xz
Source0:        %{name}-%{git}.tar.xz

BuildRequires:  llvm >= 3.3-0.6, llvm-devel, llvm-static
BuildRequires:  clang >= 3.3-0.6
BuildRequires:  zlib-devel
BuildRequires:  python

%description
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

  * 6.1: Supported Data Types
  * 6.2.3: Explicit Conversions
  * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
  * 6.9: Preprocessor Directives and Macros
  * 6.11: Built-in Functions
  * 9.3: Double Precision Floating-Point
  * 9.4: 64-bit Atomics
  * 9.5: Writing to 3D image memory objects
  * 9.6: Half Precision Floating-Point
  * 
libclc is intended to be used with the Clang compiler's OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it provides
generic implementations of most library requirements, allowing the target
to override the generic implementation at the granularity of individual
functions.

libclc currently only supports the PTX target, but support for more
targets is welcome.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{git}


%build
./configure.py --prefix=%{_prefix} --libexecdir=%{_libexecdir} --pkgconfigdir=%{_libdir}/pkgconfig/
make %{?_smp_mflags}


%install
%make_install


%files
%doc LICENSE.TXT README.TXT CREDITS.TXT
%{_libexecdir}/*.bc

%files devel
%doc
%{_includedir}/clc
# FIXME is there a predefined variable for pkgconfig?
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jul 19 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.0.1-0.1.20130719git2e8fa9f
- Update to latest upstream
- Release field now reflects that it's a pre-release

* Sun Jul 14 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.0.1-0.0.20130714git5217211
- Initial package

%define		fversion	%(echo %{version} |tr r -)
%define		modulename	reshape2
Summary:	Flexibly reshape data: a reboot of the reshape package
Name:		R-cran-%{modulename}
Version:	1.4.5
Release:	1
License:	MIT
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	2b99f857c715d1ebca9416e8b4dd51c2
URL:		https://github.com/hadley/reshape
BuildRequires:	R >= 3.1
BuildRequires:	R-cran-plyr >= 1.8.1
BuildRequires:	R-cran-Rcpp
BuildRequires:	R-cran-stringr
Requires(post,postun):	R >= 3.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
Requires:	R-cran-plyr >= 1.8.1
Requires:	R-cran-Rcpp
Requires:	R-cran-stringr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reshape lets you flexibly restructure and aggregate data using just
two functions: melt and cast.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}

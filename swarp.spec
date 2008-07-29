%define name   swarp 
%define version 2.10
%define release %mkrel 4

Name:           %{name}
Summary: 	Program that resamples and co-adds together FITS images
Group:		Graphics		
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Version:        %{version}
Release:        %{release}
License: 	GPL
URL:		http://terapix.iap.fr/soft/swarp/
#Requires:	
Source:         ftp://ftp.iap.fr/pub/from_users/bertin/swarp/%{name}-%{version}.tar.bz2
#Source1:
#Patch0:

%description
SWarp is a program that resamples and co-adds together FITS images using
any arbitrary astrometric projection defined in the WCS standard. 

%prep
rm -rf %{RPM_BUILD_ROOT}
%setup -q -n %{name}-%{version}
#%patch0 -p0
#cp %{SOURCE3} $RPM_BUILD_DIR/%{name}-%{version}/

%build
%configure 
%make

%install
%makeinstall
rm -rf %{buildroot}/%{_mandir}/manx*

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog COPYING HISTORY INSTALL README THANKS doc/*
%attr(644,root,root) %{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/swarp


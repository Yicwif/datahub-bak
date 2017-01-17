%define name         datahub
%define release      1
%define version      2.2.0
%define buildroot %{_topdir}/%{name}-%{version}-%{release}

BuildRoot:      %{buildroot}
Summary:        yaxin datahub 
License:        GPL
Name:           %{name}
Version:        %{version}
Release:        %{release}  
Source:         datahub-2.2.0.tar.gz  
Prefix:         /usr 
URL:            hub.dataos.io
  
%description  
The datahub program pull and publish repository/dataitem:tag using the command-line.  
  
%prep  
%setup -q  
  
#%build 
#Prefix:         /usr  

  
%install
mkdir -p $RPM_BUILD_ROOT/usr/bin  
cp $RPM_BUILD_DIR/%{name}-%{version}/datahub $RPM_BUILD_ROOT/usr/bin/

%files
/usr/bin/datahub

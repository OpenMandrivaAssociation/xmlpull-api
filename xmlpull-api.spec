# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support     1
%define section                free

Name:                xmlpull-api
Version:        1.1.4
Release:        1.0.5
Epoch:          0
Summary:        Simple to use XML pull parsing API 
License:        Public Domain
Url:            https://www.xmlpull.org/
Group:          Development/Java
#Vendor:        JPackage Project
#Distribution:  JPackage
Source0:        %{name}-%{version}.tar.gz
##cvs -d :pserver:anonymous@cvs.xmlpull.org:/l/extreme/cvspub login (password='cvsanon')
##cvs -d :pserver:anonymous@cvs.xmlpull.org:/l/extreme/cvspub export -r XMLPULL_1_1_4 xmlpull-api

BuildRequires:  java-rpmbuild >= 0:1.6
BuildRequires:  ant >= 1.4.1
BuildRequires:  junit >= 3.8.1
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
XmlPull v1 API is a simple to use XML pull parsing API that was
designed for simplicity and very good performance both in constrained
environment such as defined by J2ME and on server side when used in
J2EE application servers.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}

sed -i -e s:"<property name=\"version\" value=\"1_1_3_1\"/>":"<property name=\"version\" value=\"1_1_4\"/>":g build.xml

%build
export OPT_JAR_LIST=:
export CLASSPATH=
%{ant}
%{ant} javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/lib/xmlpull_1_1_4.jar \
                %{buildroot}%{_javadir}/%{name}-%{version}.jar

# create unprefixed and unversioned symlinks
(cd %{buildroot}%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)

#install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp *.txt *.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/api_impl/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc *.txt *.html
#%doc %{_docdir}/%{name}-%{version}/*
#%dir %{_docdir}/%{name}-%{version}
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}



%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:1.1.4-1.0.3mdv2010.0
+ Revision: 446198
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0:1.1.4-1.0.2mdv2009.1
+ Revision: 350075
- 2009.1 rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.1.4-1.0.1mdv2009.0
+ Revision: 170614
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 28 2007 David Walluck <walluck@mandriva.org> 0:1.1.4-1.0.1mdv2008.1
+ Revision: 138998
- import xmlpull-api


* Wed May 24 2006 Deepak Bhole <dbhole@redhat.com> 0:1.1.4-1jpp
- Initial build

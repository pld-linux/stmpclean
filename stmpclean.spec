Summary:	A safe temporary directory cleaner
Summary(pl):	Bezpieczny program porz±dkuj±cy katalogi z plikami tymczasowymi
Name:		stmpclean
Version:	0.3
Release:	1
License:	BSD
Group:		Applications/System
URL:		http://www.internet2.edu/~shalunov/stmpclean/
Source0:	http://www.internet2.edu/~shalunov/stmpclean/%{name}-%{version}.tar.gz
Source1:	%{name}.cron
Patch0:		%{name}-Owl.patch
PreReq:		/etc/cron.daily
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stmpclean utility removes old files (and old empty directories)
from the specified directory. Its typical use is to clean directories
such as /tmp where old files tend to accumulate.

%description -l pl
Program stmpclean usuwa stare pliki i puste podkatalogi z podanego
katalogu.  Zwykle u¿ywa siê go do porz±dkowania katalogów, w których
zbieraj± siê niepotrzebne pliki, jak /tmp.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags} -Wall" stmpclean

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT SBINDIR=%_sbindir MANDIR=%_mandir
cd $RPM_BUILD_ROOT
install -d etc/cron.daily
install -m 700 $RPM_SOURCE_DIR/stmpclean.cron etc/cron.daily/stmpclean

%files
%defattr(644,root,root,755)
%doc README FAQ
%_sbindir/%{name}
%_mandir/man8/%{name}*
/etc/cron.daily/stmpclean

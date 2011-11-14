%define	snap	20111114
%define	rel	1
Summary:	Utilities for monitoring your system and processes on your system
Summary(de.UTF-8):	Utilities zum Ueberwachen Ihres Systems und der Prozesse
Summary(es.UTF-8):	Utilitarios de monitoración de procesos
Summary(fr.UTF-8):	Utilitaires de surveillance des processus
Summary(pl.UTF-8):	Narzędzia do monitorowania procesów
Summary(pt_BR.UTF-8):	Utilitários de monitoração de processos
Summary(tr.UTF-8):	Süreç izleme araçları
Name:		procps
Version:	3.2.8
Release:	1.%{snap}.%{rel}
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://gitorious.org/procps/procps/archive-tarball/master#/%{name}-%{snap}.tar.gz
# Source0-md5:	7c9b068afce3ad7f1391c7506e48534c
Source1:	http://atos.wmid.amu.edu.pl/~undefine/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	60d24720b76c10553ed4abf68b76e079
Source2:	top.desktop
Source3:	top.png
Source4:	XConsole.sh
Patch2:		%{name}-FILLBUG_backport.patch
# http://www.nsa.gov/selinux/patches/procps-selinux.patch.gz
Patch3:		%{name}-selinux.patch
URL:		http://gitorious.org/procps/
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	rpmbuild(macros) >= 1.402
Requires(post):	/sbin/ldconfig
Requires:	fileutils
Obsoletes:	procps-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The procps package contains a set of system utilities which provide
system information. Procps includes ps, free, skill, snice, tload,
top, uptime, vmstat, w and watch. The ps command displays a snapshot
of running processes. The top command provides a repetitive update of
the statuses of running processes. The free command displays the
amounts of free and used memory on your system. The skill command
sends a terminate command (or another specified signal) to a specified
set of processes. The snice command is used to change the scheduling
priority of specified processes. The tload command prints a graph of
the current system load average to a specified tty. The uptime command
displays the current time, how long the system has been running, how
many users are logged on and system load averages for the past one,
five and fifteen minutes. The w command displays a list of the users
who are currently logged on and what they're running. The watch
program watches a running program. The vmstat command displays virtual
memory statistics about processes, memory, paging, block I/O, traps
and CPU activity.

%description -l de.UTF-8
Das procps-Paket enthält System-Utilities, die Systeminformationen
anzeigen. Procps enthält ps, free, skill, snice, tload, top, uptime,
vmstat, w und watch. ps zeigt an, welche Prozesse gerade laufen. Top
zeigt in regelmäßigen Abständen eine Prozessliste an. Free zeigt an,
wieviel Speicher frei ist, und wieviel Speicher benutzt wird. Skill
schickt den Terminierungsbefehl (oder ein anderes angegebenes Signal)
an angegebene Prozesse. Snice ändert die Priorität von angegebenen
Prozessen. tload zeigt einen Graphen der aktuellen Systemauslastung
an. Uptime zeigt an, wie lange das System am laufen ist, wieviele User
eingeloggt sind, und die Auslastungswerte der letzten Minute, der
letzten 5 Minuten, und 15 Minuten. Der w-Befehl zeigt eine Liste der
User an, die gerade eingeloggt sind, und welches Programm sie
benutzen. Vmstat zeigt Statistiken über den virtuellen Speicher,
Prozesse, Paging, Block I/O, Traps, und CPU-Aktivität.

%description -l es.UTF-8
Un paquete de utilitarios que relatan el estado del sistema. Se da
énfasis a los procesos en ejecución, total de memoria disponible y a
los usuarios que están "logados" en el sistema.

%description -l fr.UTF-8
Paquetage d'utilitaires donnant des informations sur l'état du
système, dont les états des processus en cours, le total de mémoire
disponible, et les utilisateurs loggés.

%description -l pl.UTF-8
Pakiet zawiera podstawowe narzędzia do monitorowania pracy systemu.
Dzięki tym programom będziesz mógł na bieżąco kontrolować jakie
procesy są w danej chwili uruchomione, ilość wolnej pamięci, kto jest
w danej chwili zalogowany, jakie jest aktualne obciążenie systemu itp.

%description -l pt_BR.UTF-8
Um pacote de utilitários que relatam o estado do sistema. É dado
ênfase aos processos em execução, total de memória disponível e aos
usuários que estão logados no sistema.

%description -l tr.UTF-8
Sistemin durumunu rapor eden araçlar paketidir. Koşan süreçlerin
durumunu, kullanılabilir bellek miktarını, ve o an için sisteme girmiş
kullanıcıları bildirir.

%package devel
Summary:	libproc header files
Summary(pl.UTF-8):	Pliki nagłówkowe libproc
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
libproc header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libproc.

%package static
Summary:	Static libproc library
Summary(pl.UTF-8):	Statyczna biblioteka libproc
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of libproc library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libproc.

%prep
%setup -q -n %{name}-%{name}

%patch2 -p1
%patch3 -p1

sed -i -e "s#usrbin_execdir=.*#usrbin_execdir='\${bindir}'#g" configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="-I%{_includedir}/ncurses" \
	--bindir=/bin \
	--sbindir=/sbin \
	--libdir=/%{_lib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_libdir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/%{_lib}/libproc-ng.{a,la,so} \
	$RPM_BUILD_ROOT%{_libdir}
sed -i -e "s|libdir='/%{_lib}'|libdir='%{_libdir}'|" \
	$RPM_BUILD_ROOT%{_libdir}/libproc-ng.la
ln -snf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libproc-ng-*.so) \
        $RPM_BUILD_ROOT%{_libdir}/libproc-ng.so
ln -snf libproc-ng.so $RPM_BUILD_ROOT%{_libdir}/libproc.so
ln -snf libproc-ng.a $RPM_BUILD_ROOT%{_libdir}/libproc.a

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/XConsole

rm -f $RPM_BUILD_ROOT/bin/kill
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{kill,oldps}.1
rm -f $RPM_BUILD_ROOT%{_bindir}/{oldps,kill}

bzcat -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man1/{kill,oldps}.1
rm -f $RPM_BUILD_ROOT%{_mandir}/README-procps-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS BUGS TODO
%attr(755,root,root) /%{_lib}/libproc*.*so
%attr(755,root,root) /bin/*
%attr(755,root,root) /sbin/sysctl
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/top.desktop
%{_pixmapsdir}/top.png
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(hu) %{_mandir}/hu/man*/*
%lang(it) %{_mandir}/it/man*/*
%lang(ja) %{_mandir}/ja/man*/*
%lang(ko) %{_mandir}/ko/man*/*
%lang(nl) %{_mandir}/nl/man*/*
%lang(pl) %{_mandir}/pl/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproc.so
%attr(755,root,root) %{_libdir}/libproc-ng.so
%{_includedir}/proc

%files static
%defattr(644,root,root,755)
%{_libdir}/libproc.a
%{_libdir}/libproc-ng.a

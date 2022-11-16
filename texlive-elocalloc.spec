Name:		texlive-elocalloc
Version:	42712
Release:	1
Summary:	Local allocation macros for LaTeX 2015
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elocalloc
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elocalloc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elocalloc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elocalloc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Local allocation macros, with names taken from etex.sty but
with implementation based on the LaTeX 2015 allocation macros.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/elocalloc
%{_texmfdistdir}/tex/latex/elocalloc
%doc %{_texmfdistdir}/doc/latex/elocalloc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

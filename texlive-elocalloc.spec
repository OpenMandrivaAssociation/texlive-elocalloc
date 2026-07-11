%global tl_name elocalloc
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03
Release:	%{tl_revision}.1
Summary:	Local allocation macros for LaTeX 2015
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elocalloc
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elocalloc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elocalloc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elocalloc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Local allocation macros, with names taken from etex.sty but with
implementation based on the LaTeX 2015 allocation macros.


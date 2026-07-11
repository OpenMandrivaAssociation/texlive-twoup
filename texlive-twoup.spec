%global tl_name twoup
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Print two virtual pages on each physical page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/twoup
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MiKTeX and many other TeX implementations include tools for massaging
PostScript into booklet and two-up printing -- that is, printing two
logical pages side by side on one side of one sheet of paper. However,
some LaTeX preliminaries are necessary to use those tools. The twoup
package provides such preliminaries and gives advice on how to use the
PostScript tools.


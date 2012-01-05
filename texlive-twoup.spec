# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/twoup
# catalog-date 2007-02-27 14:52:52 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-twoup
Version:	1.3
Release:	2
Summary:	Print two virtual pages on each physical page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/twoup
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MiKTeX and many other TeX implementations include tools for
massaging PostScript into booklet and two-up printing -- that
is, printing two logical pages side by side on one side of one
sheet of paper. However, some LaTeX preliminaries are necessary
to use those tools. The twoup package provides such
preliminaries and gives advice on how to use the PostScript
tools.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/twoup/twoup.sty
%doc %{_texmfdistdir}/doc/latex/twoup/README
%doc %{_texmfdistdir}/doc/latex/twoup/twoup.pdf
#- source
%doc %{_texmfdistdir}/source/latex/twoup/twoup.dtx
%doc %{_texmfdistdir}/source/latex/twoup/twoup.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

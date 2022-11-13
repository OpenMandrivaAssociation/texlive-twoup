Name:		texlive-twoup
Version:	15878
Release:	1
Summary:	Print two virtual pages on each physical page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/twoup
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/twoup.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

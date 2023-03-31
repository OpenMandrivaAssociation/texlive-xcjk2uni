Name:		texlive-xcjk2uni
Version:	54958
Release:	2
Summary:	Convert CJK characters to Unicode, in pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcjk2uni
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcjk2uni.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcjk2uni.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcjk2uni.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to convert CJK characters to
Unicode in non-UTF-8 encoding; it provides hooks to support
hyperref in producing correct bookmarks. The bundle also
provides /ToUnicode mapping file(s) for a CJK subfont; these
can be used with the cmap package, allowing searches of, and
cut-and-paste operations on a PDF file generated by pdfTeX..

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xcjk2uni
%doc %{_texmfdistdir}/doc/latex/xcjk2uni
#- source
%doc %{_texmfdistdir}/source/latex/xcjk2uni

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

# revision 31464
# category Package
# catalog-ctan /macros/latex/contrib/xcjk2uni
# catalog-date 2013-08-18 01:02:56 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-xcjk2uni
Version:	0.1
Release:	2
Summary:	Convert CJK characters to Unicode, in pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcjk2uni
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcjk2uni.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcjk2uni.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcjk2uni.source.tar.xz
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
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0001.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0002.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0003.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0004.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0005.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0006.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0007.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0008.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0009.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0010.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0011.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0012.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0013.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0014.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0015.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0016.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0017.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0018.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0019.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0020.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0021.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0022.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0023.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0024.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0025.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0026.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0027.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0028.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0029.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0030.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0031.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0032.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0033.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0034.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0035.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0036.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0037.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0038.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0039.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0040.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0041.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0042.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0043.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0044.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0045.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0046.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0047.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0048.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0049.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0050.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0051.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0052.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0053.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0054.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0055.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0056.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0057.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0058.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0901.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0902.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0903.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0904.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0905.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0906.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0907.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0908.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0909.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0910.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0911.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0912.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0913.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0914.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0915.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0916.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0917.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0918.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0919.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0920.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0921.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0922.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0923.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0924.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0925.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0926.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0927.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0928.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0929.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0930.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0931.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0932.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0933.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0934.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0935.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0936.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0937.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0938.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0939.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0940.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0941.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0942.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0943.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0944.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0945.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0946.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0947.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0948.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0949.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0950.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0951.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0952.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0953.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0954.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0955.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0956.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0957.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0958.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0959.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0960.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0961.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0962.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0963.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0964.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0965.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0966.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0967.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0968.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0969.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0970.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0971.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0972.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0973.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0974.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0975.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0976.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0977.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0978.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0979.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0980.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0981.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0982.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0983.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0984.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0985.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0986.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0987.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0988.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0989.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0990.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0991.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0992.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0993.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c0994.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1001.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1002.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1003.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1004.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1005.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1006.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1007.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1008.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1009.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1010.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1011.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1012.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1013.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1014.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1015.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1016.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1017.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1018.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1019.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1020.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1021.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1022.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1023.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1024.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1025.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1026.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1027.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1028.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1029.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1030.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1031.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1032.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1033.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1034.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1035.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1901.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1902.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1903.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1904.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1905.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1906.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1907.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1908.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1909.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1910.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1911.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1912.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1913.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1914.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1915.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1916.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1917.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1918.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1919.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1920.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1921.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1922.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1923.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1924.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1925.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1926.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1927.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1928.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1929.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1930.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1931.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1932.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1933.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1934.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1935.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1936.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1937.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1938.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1939.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1940.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1941.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1942.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1943.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1944.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1945.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1946.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1947.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1948.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1949.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1950.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1951.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1952.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1953.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1954.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1955.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1956.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1957.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1958.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1959.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1960.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1961.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1962.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1963.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1964.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1965.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1966.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1967.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1968.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1969.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1970.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1971.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1972.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1973.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1974.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1975.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1976.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1977.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1978.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1979.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1980.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1981.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1982.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1983.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1984.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1985.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1986.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1987.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1988.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1989.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1990.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1991.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1992.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1993.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c1994.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4001.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4002.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4003.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4004.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4005.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4006.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4007.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4008.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4009.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4010.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4011.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4012.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4013.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4014.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4015.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4016.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4017.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4018.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4019.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4020.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4021.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4022.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4023.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4024.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4025.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4026.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4027.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4028.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4029.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4030.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4031.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4032.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4033.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4034.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c4035.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6001.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6002.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6003.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6004.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6005.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6006.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6007.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6008.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6009.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6010.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6011.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6012.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6013.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6014.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6015.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6016.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6017.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6018.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6019.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6020.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6021.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6022.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6023.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6024.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6025.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6026.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6027.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6028.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6029.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6030.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6031.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6032.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6033.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6034.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/cmap/c6035.cmap
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni-UBg5plus.def
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni-UBig5.def
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni-UGB.def
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni-UGBK.def
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni-UJIS.def
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni-UKS.def
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni-make.ltx
%{_texmfdistdir}/tex/latex/xcjk2uni/xCJK2uni.sty
%doc %{_texmfdistdir}/doc/latex/xcjk2uni/README
%doc %{_texmfdistdir}/doc/latex/xcjk2uni/xCJK2uni.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xcjk2uni/xCJK2uni.dtx
%doc %{_texmfdistdir}/source/latex/xcjk2uni/xCJK2uni.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

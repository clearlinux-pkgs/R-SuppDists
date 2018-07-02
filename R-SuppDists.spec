#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SuppDists
Version  : 1.1.9.4
Release  : 9
URL      : https://cran.r-project.org/src/contrib/SuppDists_1.1-9.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SuppDists_1.1-9.4.tar.gz
Summary  : Supplementary Distributions
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-SuppDists-lib
BuildRequires : clr-R-helpers

%description
Inverse Gauss, Kruskal-Wallis, Kendall's Tau, Friedman's chi
        squared, Spearman's rho, maximum F ratio, the Pearson product
        moment correlation coefficient, Johnson distributions, normal
        scores and generalized hypergeometric distributions. In
        addition two random number generators of George Marsaglia are
        included.

%package lib
Summary: lib components for the R-SuppDists package.
Group: Libraries

%description lib
lib components for the R-SuppDists package.


%prep
%setup -q -c -n SuppDists

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521205572

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521205572
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SuppDists
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SuppDists
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SuppDists
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library SuppDists|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SuppDists/DESCRIPTION
/usr/lib64/R/library/SuppDists/INDEX
/usr/lib64/R/library/SuppDists/Meta/Rd.rds
/usr/lib64/R/library/SuppDists/Meta/features.rds
/usr/lib64/R/library/SuppDists/Meta/hsearch.rds
/usr/lib64/R/library/SuppDists/Meta/links.rds
/usr/lib64/R/library/SuppDists/Meta/nsInfo.rds
/usr/lib64/R/library/SuppDists/Meta/package.rds
/usr/lib64/R/library/SuppDists/NAMESPACE
/usr/lib64/R/library/SuppDists/R/SuppDists
/usr/lib64/R/library/SuppDists/R/SuppDists.rdb
/usr/lib64/R/library/SuppDists/R/SuppDists.rdx
/usr/lib64/R/library/SuppDists/help/AnIndex
/usr/lib64/R/library/SuppDists/help/SuppDists.rdb
/usr/lib64/R/library/SuppDists/help/SuppDists.rdx
/usr/lib64/R/library/SuppDists/help/aliases.rds
/usr/lib64/R/library/SuppDists/help/paths.rds
/usr/lib64/R/library/SuppDists/html/00Index.html
/usr/lib64/R/library/SuppDists/html/R.css
/usr/lib64/R/library/SuppDists/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/SuppDists/libs/SuppDists.so
/usr/lib64/R/library/SuppDists/libs/SuppDists.so.avx2
/usr/lib64/R/library/SuppDists/libs/SuppDists.so.avx512

#!/usr/bin/env bash
#https://github.com/asfadmin/gdal-lambda-layer

set -e
nproc=1

[[ -d tmp ]] || mkdir tmp
cd tmp
if [[ ! -f `which gdal-config` ]]; then
    # install build tools and dependencies available via yum
    sudo yum install -y gcc gcc-c++ make libtool file gzip zip wget openssl-devel libffi-devel
    sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    sudo yum install -y netcdf-devel hdf5-devel
    dnf --enablerepo=PowerTools install jasper-devel -y
    export LD_LIBRARY_PATH=/usr/local/lib
    # create folders for deployment package
    [[ -d /opt/python ]] || mkdir /opt/python
    [[ -d /opt/lib ]] || mkdir /opt/lib
    [[ -d /opt/lib/data ]] || mkdir /opt/lib/data
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
    ## install python and pip 3.8.1
    #wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz
    #tar xzf Python-3.8.1.tgz
    #cd Python-3.8.1
    #./configure
    #make -j $(nproc)
    #make install
    #cd ..
    # install sqlite
    wget https://www.sqlite.org/snapshot/sqlite-snapshot-202002181949.tar.gz
    tar xvzf sqlite-snapshot-202002181949.tar.gz
    cd sqlite-snapshot-202002181949
    ./configure
    make -j $(nproc)
    make install
    cd ..
    # install proj 6.3.1
    wget https://github.com/OSGeo/PROJ/releases/download/6.3.1/proj-6.3.1.tar.gz
    tar xvzf proj-6.3.1.tar.gz
    cd proj-6.3.1
    ./configure
    make -j $(nproc)
    make install
    cd ..
#     install gdal 3.0.4
    wget https://github.com/OSGeo/gdal/releases/download/v3.0.4/gdal-3.0.4.tar.gz
    tar xvzf gdal-3.0.4.tar.gz
    cd gdal-3.0.4
    ./configure
    make
    make install
    sudo ldconfig
    sudo ln -s /usr/lib/libgdal.so /usr/lib/libgdal.so.1
    cd ../..
fi

wget http://download.osgeo.org/geos/geos-3.8.1.tar.bz2
tar -xf geos-3.8.1.tar.bz2
cd geos-3.8.1
./configure
make
sudo make install
cd -
rm -rf tmp

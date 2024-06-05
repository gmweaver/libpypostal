#!/bin/bash

OS=$(uname -s)

case $OS in
    Linux)
        echo "Detected Linux"
        # Linux-specific commands here
        ;;
    Darwin)
        echo "Detected macOS"
        # macOS-specific commands here
        ;;
    FreeBSD)
        echo "Detected FreeBSD"
        # FreeBSD-specific commands here
        ;;
    *)
        echo "OS not supported"
        # Handle unsupported OS here
        ;;
esac

cd $1
git clone https://github.com/openvenues/libpostal
cd libpostal
git checkout tags/v1.1
./bootstrap.sh
./configure --datadir=/tmp/libpostal_data_files --disable-data-download --disable-sse2
make -j4
sudo make install

if [ "$OS" = "Linux" ]; then
    sudo ldconfig
fi

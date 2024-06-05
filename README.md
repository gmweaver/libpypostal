# pylibpostal

Python wrapper for open-source libpostal project. Custom libary built internally due to lack of continued support for current Python wrapper libraries.

## Usage

### Install libpostal C library

By default, libpostal will be installed when the Python package is installed, but without the data.

The commands run to install are below.

```
git clone https://github.com/openvenues/libpostal \
    && cd libpostal \
    && ./bootstrap.sh \
    && ./configure --datadir=/tmp/libpostal_data_files --disable-data-download --disable-sse2 \
    && make -j4 \
    && make install \
    && ldconfig
```

- `--disable-data-download` disables downloading data when installing. 
- `--disable-sse2` required for Mac M1.
- `ldconfig` only needed for linux.

See https://github.com/openvenues/libpostal?tab=readme-ov-file#installation-maclinux for more details. 

### Downloading libpostal data

```
libpostal_data download all <data-dir>
```

## Contributing
To test the project, run `poetry test`. Test files may live together with the code or in a separate
directory, but in order for them to be discovered, they should end with `_test.py`
(e.g. `pylibpostal/something_test.py` or `pylibpostal_test/something_test.py`).

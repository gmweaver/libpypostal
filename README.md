# libpypostal

Python bindings for [libpostal](https://github.com/openvenues/libpostal), an open-source address parsing library.

## Why another Python library for libpostal?

There are currently two Python packages available on PyPI that provide bindings for the libpostal C library.

1. [pypostal](https://github.com/openvenues/pypostal) (official)
2. [pylibpostal](https://github.com/openvenues/pypostal) (fork of pypostal)

Due to lack of development in either project for a number of years, here is yet another (non-forked) Python package to address some challenges in usability. 

Note that this package reuses the C extension code to avoid reinventing the wheel with some minor changes (e.g. remove Python 2 support). The Python API has also changed slightly in some cases for usability purposes as well.

## Installation

If a wheel is not available for your architecture and/or Python version, you need to first [install libpostal](https://github.com/openvenues/libpostal?tab=readme-ov-file#installation-maclinux).

```console
pip install libpypostal
```

## Usage

### Libpostal data configuration

Required to use the library. Use the following utility to download the data. 

NOTE: This function will also automatically set the LIBPOSTAL_DATA_DIR to the output directory specified.

```python
from libpypostal import data_utils

output_dir = "/tmp/libpostal_data_dir"
data_utils.download_libpostal_data(output_dir)
```

Alternatively, if you have already downloaded the data, you only need to run:

```python
from libpypostal import data_utils

output_dir = "/tmp/libpostal_data_dir"
data_utils.set_data_dir_env_var(output_dir)
```

### Address parser

```python
from libpypostal import parser

parser.parse_address("123 Main St, Somewhere, DC 00000")
```

## Versioning

Each release of `libpypostal` depends on a specific version of `libpostal` when building wheels to release.

The version used to build the Python wheels for a given release can be found as follows:

```python
from libpypostal import version

version.LIBPOSTAL_VERSION
```


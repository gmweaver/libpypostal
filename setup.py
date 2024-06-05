import ctypes.util
import subprocess
import tempfile

from setuptools import setup, Extension


def _libpostal_installed() -> bool:
    """Checks if libpostal is installed."""
    return ctypes.util.find_library("postal") is not None


def _install_libpostal() -> None:
    """Installs libpostal."""
    with tempfile.TemporaryDirectory() as tempdir:
        subprocess.run(
            ["./install_libpostal.sh", tempdir],
            text=True,
            capture_output=True,
            check=True,
        )


if not _libpostal_installed():
    _install_libpostal()

ext_modules = [
    Extension(
        "libpypostal._parser",
        sources=["src/pyparser.c", "src/pyutils.c"],
        libraries=["postal"],
        include_dirs=["/usr/local/include", "src/"],
        library_dirs=["/usr/local/lib"],
        extra_compile_args=["-std=c99"],
    ),
]

setup(ext_modules=ext_modules)

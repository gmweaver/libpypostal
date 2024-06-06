from setuptools import setup, Extension

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

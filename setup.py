from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

"""
setup(
    name="fastmask",
    ext_modules=cythonize("fastmask.pyx"),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)
"""

extensions = [
    Extension(
        name="util.bin.fastmask",                # <package>.<module>
        sources=["util/bin/fastmask.pyx"],       # path to .pyx
        include_dirs=[numpy.get_include()],
    )
]


setup(
    name="fastmask",
    packages=["fastmask"],
    ext_modules=cythonize(extensions,
        compiler_directives={
            "language_level": "3",
            "boundscheck": False,
            "wraparound": False,
            "cdivision": True,
    }),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)
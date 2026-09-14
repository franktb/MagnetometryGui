from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import sys



extra_compile_args = []
extra_link_args = []

if sys.platform == 'win32':
    extra_compile_args.append('/openmp')
else:
    extra_compile_args.append('-fopenmp')
    extra_link_args.append('-fopenmp')



extensions = [
    Extension(
        name="util.bin.fastmask",                # <package>.<module>
        sources=["util/bin/fastmask.pyx"],       # path to .pyx
        include_dirs=[numpy.get_include()],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
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
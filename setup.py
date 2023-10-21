from setuptools import setup
from Cython.Build import cythonize

# Convert Cython to C code, so that setuptools can build it to during building process
setup(ext_modules=cythonize("src/imppkg/harmonic_mean_c.pyx"))

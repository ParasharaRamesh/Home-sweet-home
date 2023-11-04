from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules = cythonize("custom_distance_metric.pyx"),
    include_dirs = [np.get_include()]
)

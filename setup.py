from setuptools import setup
from Cython.Build import cythonize

setup(
    name="ApexEgressGuardian",
    ext_modules=cythonize("pinner.py", compiler_directives={'language_level': "3"}),
    zip_safe=False,
)

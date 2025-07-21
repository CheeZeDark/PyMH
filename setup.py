from setuptools import setup
import setuptools

setup(
    name="PyMH",
    version="0.1",
    author="CheeZeDark",
    packages=setuptools.find_packages(),
    package_data={
        '': ['x64\\*.dll'],
        '': ['x32\\*.dll'],
    }
)
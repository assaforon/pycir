import os
from setuptools import setup, find_packages

# Get version
cwd = os.path.abspath(os.path.dirname(__file__))
version = '0.1'

# Get the documentation
with open(os.path.join(cwd, 'README.md'), "r") as fh:
    long_description = fh.read()

CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: Other/Proprietary License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.7",
]

setup(
    name="pycir",
    version=version,
    author="Assaf Oron",
    author_email="aoron@idmod.org",
    description="Centered isotonic regression",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://idmod.org',
    keywords=["regression"],
    platforms=["OS Independent"],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
)

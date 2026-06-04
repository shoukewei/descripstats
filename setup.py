from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.1.1"
DESCRIPTION = "Extended descriptive statistics for pandas DataFrames"

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="descripstats",
    version=VERSION,
    author="Shouke Wei, PhD",
    author_email="shouke.wei@deepsim.ca",
    license="MIT",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    url="https://github.com/shoukewei/descripstats",

    packages=find_packages(),

    install_requires=[
        "pandas>=2.0",
        "numpy>=1.21"
    ],

    keywords=[
        "python",
        "pandas",
        "dataframe",
        "descriptive statistics",
        "eda",
        "statistics"
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
    ],
)
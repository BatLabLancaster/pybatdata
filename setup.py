import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

desc = (
    "Analyse data from battery testers."
)

# This call to setup() does all the work
setup(
    name="pybatdata",
    version="0.0.2",
    packages=find_packages(exclude=("tests",),
    description=desc,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BatLabLancaster/pybatdata",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[
        "numpy>=1.15",
        "preparenovonix==1.0.1",
        # Note: Matplotlib is used for some plots
        "matplotlib>=3.0",
    ],
)

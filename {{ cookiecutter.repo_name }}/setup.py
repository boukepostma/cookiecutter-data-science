import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Here all dependencies that are required to run the package should be included  
base_packages = [
    "numpy",
    "scipy",
    "scikit-learn",
    "pandas",
    "plotly-express",
    "tqdm",
    "rich",
    "openpyxl",
] 

# Here all dependencies that are required to develop the package should be included
dev_packages = [
    "jupyter",
    "ipython",
    "ipykernel",
    "pip",
    "pytest",
    "flake8",
    "pre-commit",
    "black",
    "isort",
]

setup(
    name="src",
    version="0.0.1",
    packages=find_packages(exclude=["data", "notebooks"]),
    description="{{ cookiecutter.description }}",
    long_description=read("README.md"),
    install_requires=base_packages,
    author="{{ cookiecutter.author_name }}",
    extras_require={"dev": dev_packages},
)

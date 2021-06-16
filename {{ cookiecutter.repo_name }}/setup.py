import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


base_packages = [
    "numpy>=1.20.3",
    "scipy>=1.6.3",
    "scikit-learn>=0.24.2",
    "pandas>=1.2.4",
    "plotly-express>=0.4.1",
    "jupyter>=1.0.0",
    "tqdm>=4.61.1",
    "click>=8.0",
    "fastapi>=0.65.2",
    "rich",
]

dev_packages = [
    "pip",
    "pytest-cov",
    "pytest",
    "flake8",
    "mkdocs>=1.2.1",
    "mkdocs-material>=7.1.8",
    "mkdocs-jupyter==0.17.3",
    "mkdocstrings",
    "pygments",
    "pymdown-extensions",
    "pre-commit>=2.13.0",
    "coverage",
    "awscli",
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

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
    "rich",
    "openpyxl",
    "ipython>=7.27.0",
    "ipykernel>=6.4.1",
    "sktime==0.8.0",
    "pmdarima",
    "seaborn",
    {%- if cookiecutter.prophet == "True" %}
    "pystan==2.19.1.1",
    "fbprophet==0.7.1", 
    {%- endif %}
] 

dev_packages = [
    "pip",
    "pytest-cov",
    "pytest",
    "flake8",
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

{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------
```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── main.py            <- Script to run the entire pipeline
│
├── configurations
│   ├── __init__.py    <- Makes configurations a Python module
│   ├── names.py       <- Globally defined column names (e.g. of output dataframes)
│   ├── parameters.py  <- Globally defined parameters used in src 
│   └── paths.py       <- Globally defined folder and file paths 
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── logger.py          <- Definition of logger
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── tests
│   ├── __init.py__    <- Makes tests a Python module
│   └── test_basic.py  <- Basic pytest test
│
├── .flake8            <- flake8 settings
├── .gitignore         <- files to be ignored by git 
└── .pre-commit-config.yaml <- pre-commit hooks
```


--------
## Installation
First set the project folder as working directory and set up git using the following command

```bash
git init
```

Set up a virtual environment via:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source ./venv/Scripts/activate
```

Then install the project and required packages in the activated virtual environment via:

```bash
python -m pip install -U pip setuptools wheel
python -m pip install -e ".[dev]"
pre-commit install
```

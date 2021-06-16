# Cookiecutter 
#### [Forked from](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter https://github.com/boukepostma/cookiecutter-data-science.git

... and follow the instructions in the new project directory's README.md file.


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
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
├── docs               <- A simple mkdocs project; see mkdocs.org for details
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

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests

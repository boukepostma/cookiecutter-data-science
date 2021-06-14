import os

# Data_root_path
FOLDER_ROOT = os.get_cwd()

FOLDER_DATA = os.sep.join([FOLDER_ROOT, 'data'])
FOLDER_MODELS = os.sep.join([FOLDER_ROOT, 'models'])
FOLDER_NOTEBOOKS = os.sep.join([FOLDER_ROOT, 'notebooks'])
FOLDER_DOCS = os.sep.join([FOLDER_ROOT, 'docs'])
FOLDER_REFERENCES = os.sep.join([FOLDER_ROOT, 'references'])
FOLDER_REPORTS = os.sep.join([FOLDER_ROOT, 'reports'])

FOLDER_DATA_RAW = os.sep.join([FOLDER_DATA,'raw'])
FOLDER_DATA_EXTERNAL = os.sep.join([FOLDER_DATA,'external'])
FOLDER_DATA_INTERIM = os.sep.join([FOLDER_DATA,'interim'])
FOLDER_DATA_PROCESSED = os.sep.join([FOLDER_DATA,'processed'])

FOLDER_FIGURES = os.sep.join([FOLDER_REPORTS, 'figures'])

## FILE PATHS: Paths to files (.csv, .xlsx), databases (.db, .sqlite) and their respective table names  ##
# Raw data
FILE_PATH_EXAMPLE = os.sep.join([FOLDER_DATA_RAW, 'example.xlsx'])

# External data

# Interim data

# Processed data 


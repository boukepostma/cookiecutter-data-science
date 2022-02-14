"""
Example to use these configurations: 
from configurations import paths 
print(paths.FOLDER_ROOT)
"""

from pathlib import Path

# Repository root path. Note that this line will not work when copy-pasted into a terminal / notebook. 
FOLDER_ROOT = Path(__file__).resolve().parents[1]

FOLDER_DATA = FOLDER_ROOT / "data"
FOLDER_MODELS = FOLDER_ROOT / "models"
FOLDER_NOTEBOOKS = FOLDER_ROOT / "notebooks"
FOLDER_REPORTS = FOLDER_ROOT / "reports"
FOLDER_REFERENCES = FOLDER_ROOT / "references"
FOLDER_DOCS = FOLDER_ROOT / "docs"
FOLDER_LOGS = FOLDER_ROOT / "logs"

FOLDER_DATA_RAW = FOLDER_DATA / "raw"
FOLDER_DATA_EXTERNAL = FOLDER_DATA / "external"
FOLDER_DATA_INTERIM = FOLDER_DATA / "interim"
FOLDER_DATA_PROCESSED = FOLDER_DATA / "processed"

FOLDER_FIGURES = FOLDER_REPORTS / "figures"

# LOGGER FILE PATH
FILE_LOGGER = FOLDER_LOGS / "logs.log"

# FILE PATHS: Paths to files (.csv, .xlsx), databases (.db, .sqlite) and their respective table names

# Raw data
FILE_PATH_EXAMPLE = FOLDER_DATA_RAW / "example.xlsx"

# External data

# Interim data

# Processed data

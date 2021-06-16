# -*- coding: utf-8 -*-
from logger import logger
from pathlib import Path

def main(input_filepath:str, output_filepath:str) -> bool:
    """Execute data preprocessing pipeline

    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).

    Args:
        input_filepath (str): path of input file
        output_filepath (str): path of output file

    Returns:
        bool: True if successful
    """
    logger.info("making final data set from raw data")
    return True

if __name__ == "__main__":
    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    main()

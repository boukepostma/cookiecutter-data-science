# -*- coding: utf-8 -*-
from logger import logger


def main(input_filepath: str, output_filepath: str) -> bool:
    """Execute data preprocessing pipeline

    Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).

    Args:
        input_filepath (str): path of input file
        output_filepath (str): path of output file

    Returns:
        bool: True if successful
    """
    logger.info("Creating final data set from raw data")
    return True


if __name__ == "__main__":
    main('fake/file/path','other_fake/file/path')

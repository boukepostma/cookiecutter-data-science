"""
See this short series of videos for an introduction on logging: https://calmcode.io/logging/introduction.html

To use this logger, check out the following example: 

from logger import logger
logger.debug("some log statement")
"""

import logging
import os

from rich.logging import RichHandler

from configs.paths import FILE_LOGGER

logger = logging.getLogger(__name__)

try:
    # This will evoke an error when using ipython (e.g. notebooks)
    get_ipython()  # noqa
    
    # Use regular logger without rich or filehandler when using ipython (notebooks)
    shell_handler = logging.StreamHandler()

    # the formatter determines what our logs will look like
    fmt_shell = "%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
    formatter = logging.Formatter(fmt_shell)
    shell_handler.setFormatter(formatter)

    logger.addHandler(shell_handler)

    # FYI: Levels of logging go: debug, info, warning, critical, error
    logger.setLevel(logging.INFO)
    shell_handler.setLevel(logging.INFO)

except NameError:
    # the handler determines where the logs go: stdout/file
    shell_handler = RichHandler()
    file_handler = logging.FileHandler(filename=FILE_LOGGER)

    # the formatter determines what our logs will look like
    fmt_shell = "%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
    formatter = logging.Formatter(fmt_shell)
    shell_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(shell_handler)
    logger.addHandler(file_handler)

    # FYI: Levels of logging go: debug, info, warning, critical, error
    logger.setLevel(logging.DEBUG)
    shell_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

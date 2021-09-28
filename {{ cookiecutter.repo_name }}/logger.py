"""
See this short series of videos for an introduction on logging: https://calmcode.io/logging/introduction.html
"""

import logging
import os

from rich.logging import RichHandler

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
shell_handler = RichHandler()
file_handler = logging.FileHandler(filename=os.sep.join(["logs", "logs.log"]))

# the formatter determines what our logs will look like
fmt_shell = "%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
formatter = logging.Formatter(fmt_shell)
shell_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)

# FYI: Levels of logging go: debug, info, warning, critical, error
logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

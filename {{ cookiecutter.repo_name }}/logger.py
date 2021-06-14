import logging
from rich.logging import RichHandler

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
shell_handler = RichHandler()

# the formatter determines what our logs will look like
fmt_shell = (
    "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
)
formatter = logging.Formatter(fmt_shell)
shell_handler.setFormatter(formatter)

logger.addHandler(shell_handler)

# FYI: Levels of logging go: debug, info, warning, critical, error
logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.DEBUG)

import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """set up a logger with the specified name and confriguration"""

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  # already configured
    
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(handler)
    logger.propagate = False  # prevent double logging if root logger is also configured
    return logger
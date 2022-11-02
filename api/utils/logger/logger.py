"""Logger for logging operations.

This module contains:
    - Logger class
"""
import logging


class Logger:
    """Class for creating logging.Logger objects."""

    @staticmethod
    def get_logger_file(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler("movie_rental/logger/logs/logfile.log")
        formatter = logging.Formatter("%(name)s - "
                                      "[%(levelname)s] - "
                                      "%(lineno)d - "
                                      "%(message)s - "
                                      "%(pathname)s"
                                      )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    @staticmethod
    def get_logger_console(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(name)s - "
                                      "[%(levelname)s] - "
                                      "%(lineno)d - "
                                      "%(message)s - "
                                      "%(pathname)s"
                                      )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

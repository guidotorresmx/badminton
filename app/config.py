from loguru import logger
import sys

search_params = {
    'activity': ['badminton'],
    'postal_code': ['9000'],
    'distance': [''],
    'age_group ': [''],
}

globals = {
    'search_params': search_params
}

logger_options = {
    "format": "{time:YYYY-MM-DD HH:mm:ss} || {level} || {message}",
    "level": "DEBUG",
    "colorize": True,
    "backtrace": True,
    "diagnose": True
}


def log_init():
    logger.add(sys.stderr, **logger_options)
    logger.add("file.log", rotation="1 MB", **logger_options)
    logger.level("DEBUG", color='<yellow> <bold>')
    logger.level("ERROR", color='<RED> <bold>')
    logger.level("INFO", color='<BLUE> <bold>')
    logger.level("SUCCESS", color='<GREEN> <bold>')
    logger.level("WARNING", color='<YELLOW> <bold>')
    logger.success("Initializing logging features...")

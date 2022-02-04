from loguru import logger
import sys

search_params = {
    'activity': ['badminton'],
    'postal_code': ['9000'],
    'distance': [''],
    'age_group ': [''],
    'date': "03-02-2022"
}

globals = {
    'search_params': search_params,
    'URLs': URLs
}

logger_options = {
    "format": "{time:YYYY-MM-DD HH:mm:ss} || {level} || {message}",
    "level": "DEBUG",
    "colorize": True,
    "backtrace": True,
    "diagnose": True
}

URLs = {
    "CENTRE_URL": 'https://www.toronto.ca/data/parks/prd/facilities/complex/__route__/index.html',
}

show_options = {
    terminal: True,
    powershell: True,
    web: True,
    excel: True,
    csv: True,
    drive: True
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

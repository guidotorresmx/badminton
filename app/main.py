
from fastapi import FastAPI, HTTPException
from loguru import logger
import sys

from models.general_data_crawler import get_centres
from models.centre_data_crawler import get_data
from config import log_init


#import click
log_init()
app = FastAPI()


@app.get("/ping")
async def pong():
    logger.error("Error log")
    logger.warning("Warning log")
    logger.info("Info log")
    logger.debug("Debug log")
    return {"status": "OK"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def root():
    return {"status": "OK"}

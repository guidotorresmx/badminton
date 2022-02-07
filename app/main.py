
from fastapi import FastAPI, HTTPException
from loguru import logger
import sys
from pydantic import BaseModel

from models.general_data_crawler import get_centres
from models.centre_data_crawler import get_data
from config import log_init


#import click
log_init()
app = FastAPI()


@app.get("/ping")
async def ping():
    logger.error("pong error log")
    logger.warning("pong warning log")
    logger.info("pong info log")
    logger.debug("pong debug log")
    return {"answer": "pong"}


@app.get("/health")
async def health():
    return {"status": "OK"}


class Payload(BaseModel):
    output_type: "cli"
    postal_code: str
    map: False
    path: str


def get_activities_df(params):
    print(params)
    return params


@app.post("/badminton")
async def badminton(params, headers):
    params = get_params(params)
    return {"params": params}

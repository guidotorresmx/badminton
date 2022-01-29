from fastapi import FastAPI, HTTPException
from loguru import logger
import sys

logger.add(sys.stderr, format="{time} {level} {message}", level="DEBUG")
logger.add("file.log", format="{time} {level} {message}", level="DEBUG")
logger.debug("That's it, beautiful and simple logging!")

#logger.add("debug.log", filter=lambda record: record["level"].name == "DEBUG")
#logger.add("info.log", filter=lambda record: record["level"].name == "INFO")
#logger.add("error.log", filter=lambda record: record["level"].name == "ERROR")

app = FastAPI()


# formatter = logging.Formatter(
#    "[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s", "%Y-%m-%d %H:%M:%S")
#handler = RotatingFileHandler('/log/abc.log', backupCount=0)
# logging.getLogger().setLevel(logging.NOTSET)
# fastapi_logger.addHandler(handler)
# handler.setFormatter(formatter)


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

import os
import logging
from logging import FileHandler
from datetime import datetime


def setup_logger(app):
    today_date = datetime.now().strftime("%Y-%m-%d")
    logger_handler = FileHandler("./logs/log-" + today_date + ".log")
    logger_handler.setLevel(logging.WARNING)
    app.logger.addHandler(logger_handler)

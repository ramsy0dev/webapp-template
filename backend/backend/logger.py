"""
This file contains the gloal logger used accross the backend.


file:backend/backend/logger.py
"""

import sys
import logging

from logging import getLogger
from logging.handlers import RotatingFileHandler

logger = getLogger("api")
logger.handlers.clear()  # remove any old handlers (prevent duplicate logs)
logger.setLevel(logging.INFO)

# stdout → proc mux
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
stdout_handler.setFormatter(stdout_formatter)

# Logs file
file_handler = RotatingFileHandler(
    "webapp-template-backend.log", maxBytes=10_000_000, backupCount=5
)
file_handler.setFormatter(stdout_formatter)

logger.addHandler(stdout_handler)
logger.addHandler(file_handler)

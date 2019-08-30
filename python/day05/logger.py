#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import logging
from logging import handlers

# create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.ERROR)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create file handler and set level to warning
# fh = handlers.TimedRotatingFileHandler("access.log",when="S",interval=5,backupCount=3)
fh = handlers.RotatingFileHandler("access.log", maxBytes=4, backupCount=2)
fh.setLevel(logging.WARNING)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

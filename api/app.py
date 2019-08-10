#!/usr/bin/env python

import sys
import logging
import flask
import yaml
import os
import json
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import send_from_directory
from flask import Flask, abort, request
from flask import jsonify


# Custom
from handler.ping import healthCheck
from handler.bestseller import bestSellerList

# Get API Key
APIKEY = os.environ.get('NY_API_KEY')

app = Flask(__name__)


@app.route("/")
def bestseller():
    List = bestSellerList(API_KEY=APIKEY)
    return List


@app.route("/ping")
def ping():
    ping = healthCheck(message="pong")
    return ping


if __name__ == '__main__':
    logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
    logging.basicConfig(format=logFormatStr,
                        filename="global.log", level=logging.DEBUG)
    formatter = logging.Formatter(logFormatStr, '%m-%d %H:%M:%S')
    fileHandler = logging.FileHandler("summary.log")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.DEBUG)
    streamHandler.setFormatter(formatter)
    app.logger.addHandler(fileHandler)
    app.logger.addHandler(streamHandler)

    # Start app
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)

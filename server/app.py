import os, sys
sys.path.append('../modules/')

import pandas as ps
import numpy as np

import generation.nonnormal as nonnormalGenerator
import tests.generator as generator

from flask import Flask
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return np.array_str(generator.testNonNormalDistributedGenerator())

if __name__ == '__main__':
    socketio.run(app, debug=True)

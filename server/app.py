import os, sys
sys.path.append('../modules/')

import pandas as ps
import numpy as np

import generation.nonnormal as nonnormalGenerator
import tests.generator as generator

import generators.collection as generators

from flask import Flask
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

#print generators.get_instance()
#print generators.find_print_by_url('generate/apple/data') is None
#print generators.find_print_by_url('generate/appata') is None

app = Flask(__name__)
socketio = SocketIO(app)

# def index(path):
#     return np.array_str(generator.testNonNormalDistributedGenerator())

@app.route('/', defaults={'url': ''})
@app.route('/<path:url>')
def catch_url_generator_request(url):
    print url
    return generators.handle(url)

if __name__ == '__main__':
    socketio.run(app, debug=True)

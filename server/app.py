import os, sys
sys.path.append('../modules/')
import json

import pandas as pd
import numpy as np

import generators.collection as generators

from flask import Flask
from flask import request
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import schedule, time
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app)

host = "127.0.0.1"
port = 5000

@app.route('/', defaults={'url': ''})
@app.route('/<path:url>', methods=['GET', 'POST'])
def catch_url_generator_request(url):
    print 'method', request.method
    if request.method == 'POST':
        data = request.data
        dataDict = json.loads(data)
        print data
        return json.dumps({'answer':'server send data', 'data': { 'set': [1,2,3], 'type': "a"}}, separators=(',', ':'))
    else:
        return generators.handle('generator', url)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=port, host=host)

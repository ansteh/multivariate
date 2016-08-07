import os, sys
sys.path.append('../modules/')

import pandas as pd
import numpy as np
import requests
import json

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
port = 5001

@app.route('/', defaults={'url': ''})
@app.route('/<path:url>', methods=['GET', 'POST'])
def catch_url_generator_request(url):
    return generators.handle('listener', url)

import schedule, time
def post():
    dictToSend = {'question':'what is the answer?', 'data':[1,2,3]}
    res = requests.post('http://127.0.0.1:5000/generate/apple/data', json=dictToSend)
    print 'response from server:',res.text
    dictFromServer = res.json()

def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    schedule.every(4).seconds.do(post)
    t = Thread(target=run_schedule)
    t.start()
    socketio.run(app, debug=True, port=port, host=host)

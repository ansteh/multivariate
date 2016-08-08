import os, sys
sys.path.append('../modules/')
import json

import pandas as pd
import numpy as np

import generators.collection as generators

import requests
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
    #print 'method', request.method
    return generators.handle('generator', url)

def start_schedule_for_remote_listener_of(generator):
    if(generator.generator_web_interface == 'rest' and generator.has_frequence()):
        def post():
            url = generator.get_listener_url()
            select_options = generator.get_select_options()
            data = generator.simulate(select_options['limit'], select_options)

            try:
                res = requests.post(url, json=data.tolist())
            except:
                print "connecting to client listener failed"

            try:
                print np.array(res.json()).shape
            except:
                print res.text

        start_thread_of_function(post, generator.get_frequence_in_seconds())

def start_thread_of_function(func, seconds):
    def run_schedule():
        while 1:
            try:
                schedule.run_pending()
                # time.sleep(1)
            except:
                time.sleep(5)
                print "error"

    schedule.every(seconds).seconds.do(func)
    t = Thread(target=run_schedule)
    t.start()

map(start_schedule_for_remote_listener_of, generators.generators)


if __name__ == '__main__':
    # socketio.run(app, debug=True, port=port, host=host, use_reloader=False)
    socketio.run(app, debug=True, port=port, host=host)

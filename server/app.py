#server datagenerator configurations
host = "127.0.0.1"
port = 5000
emit_to_python_listener = False

#print app.root_path
# end server datagenerator configurations



import os, sys
sys.path.append('../modules/')
import json

import pandas as pd
import numpy as np

import generators.collection as generators

import requests
from flask import Flask, url_for, render_template
from flask import request
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import schedule, time
from threading import Thread
from flask_socketio import send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/testbed')
def show_testbed():
    return render_template('testbed.html')

@app.route('/', defaults={'url': ''})
@app.route('/<path:url>', methods=['GET', 'POST'])
def catch_url_generator_request(url):
    #print 'method', request.method
    return generators.handle('generator', url)

#web sockets

def init_socket(generator):
    @socketio.on(generator.url)
    def handle_my_custom_event(json):
        if('size' in json.keys()):
            #select_options=json["select_options"]
            emit(generator.url, generator.simulate(size=json["size"]).tolist())
        else:
            emit(generator.url, generator.simulate().tolist())

map(lambda generator: init_socket(generator), generators.get_web_sockets())

#remote python Listener
def start_schedule_for_remote_listener_of(generator):
    if(generator.generator_web_interface == 'rest' and generator.has_frequence()):
        def post():
            url = generator.get_listener_url()
            select_options = generator.get_select_options()
            data = generator.simulate(select_options['limit'], select_options)

            try:
                res = requests.post(url, json=data.tolist())
            except:
                print "connecting to remote python listener ... seems to be off"

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
                # print "error"

    schedule.every(seconds).seconds.do(func)
    t = Thread(target=run_schedule)
    t.start()

def start_sending_to_remote_python_listener(state=False):
    if(state):
        map(start_schedule_for_remote_listener_of, generators.generators)

start_sending_to_remote_python_listener(emit_to_python_listener)

if __name__ == '__main__':
    # socketio.run(app, debug=True, port=port, host=host, use_reloader=False)
    socketio.run(app, debug=True, port=port, host=host)

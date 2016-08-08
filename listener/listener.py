import pandas as pd
import numpy as np
import requests
import json

import core.collection as blueprints

from flask import Flask
from flask import request
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import schedule, time
from threading import Thread

class Listener():
    def __init__(self, generator_domain):
        self.generator_domain = generator_domain

    def find_generator_by_url(self, url):
        return blueprints.find_generator_by_url(url)

    def on(self, url, callback):
        generator = self.find_generator_by_url(url)
        generator.set_callback(callback)

    def emit(self, url, callback):
        generator = self.find_generator_by_url(url)
        #dictToSend = {'question':'what is the answer?', 'data':[1,2,3]}
        # res = requests.post(self.generator_domain+'/'+url, json=dictToSend)
        try:
            res = requests.post(self.generator_domain+'/'+url)
            callback(np.array(res.json()))
        except:
            callback({ "err": "post to dategenerator from listener failed!"})

    def run(self, app, debug, port, host):
        self.init_routers(app)
        self.socketio = SocketIO(app)
        return self.socketio.run(app, debug=debug, port=port, host=host)

    def init_routers(self, app):
        @app.route('/', defaults={'url': ''})
        @app.route('/<path:url>', methods=['POST'])
        def catch_url_generator_request(url):
            generator = self.find_generator_by_url(url)
            if(generator is None):
                return 'no url match with a datagenerator!'
            else:
                generator.execute_callback(np.array(request.json))
                return 'data transfered to client listener!'

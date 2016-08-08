import pandas as ps
import numpy as np

import core.fs as fs

class Generator():
    def __init__(self, options):
        self.threshold = 1e-6
        self.options = options
        self.url = self.options['url']

        self.generator_web_interface = self.options['generator']['web_interface']
        self.listener_web_interface = self.options['listener']['web_interface']

    def set_callback(self, callback):
        self.callback = callback

    def execute_callback(self, data):
        if(hasattr(self, 'callback')):
            self.callback(data)

    def get_listener_url(self):
        return self.options['listener']['domain']+'/'+self.url

    def get_select_options(self):
        return self.options['listener']['select_options']

    def get_frequence_in_seconds(self):
        return self.options['generator']['frequence']['value']

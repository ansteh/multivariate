import fs, json
import numpy as np
from instance import create

blueprints = fs.get_blueprints()

generators = map(lambda blueprint: create(blueprint), fs.get_blueprints())

def find_generator_by_url(url=""):
    try:
        return next(generator for generator in generators if generator.url == url)
    except StopIteration:
        return None

def get_web_sockets():
    return filter(lambda g: g.has_web_socket(), generators)

def get_mqtts():
    return filter(lambda g: g.has_mqtt(), generators)

def handle(action, url, select_options=None):
    generator = find_generator_by_url(url)

    if(action == 'generator'):
        if(generator is None):
            return 'no generator match for url!'
        else:
            select_options = generator.options['listener']['select_options']
            limit = select_options['limit']
            samples = generator.simulate(limit, select_options)
            return json.dumps(samples.tolist(), separators=(',', ':'))

    if(action == 'listener'):
        if(generator is None):
            return 'no generator match for url!'
        else:
            select_options = generator.options['listener']['select_options']
            limit = select_options['limit']
            samples = generator.simulate(limit, select_options)
            return json.dumps(samples.tolist(), separators=(',', ':'))

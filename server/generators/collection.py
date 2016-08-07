import fs, json
import numpy as np
from instance import Generator

blueprints = fs.get_blueprints()

generators = map(lambda blueprint: Generator(blueprint), fs.get_blueprints())

def find_generator_by_url(url=""):
    try:
        return next(generator for generator in generators if generator.url == url)
    except StopIteration:
        return None

def handle(action, url, select_options=None):
    generator = find_generator_by_url(url)

    # url = generator.options['listener']['domain']+'/'+generator.url
    # select_options = generator.options['listener']['select_options']
    # limit = select_options['limit']

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

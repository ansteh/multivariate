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

def handle(action, url):
    generator = find_generator_by_url(url)
    if(action == 'generator'):
        if(generator is None):
            return 'no generator match for url!'
        else:
            return json.dumps(generator.simulate().tolist(), separators=(',', ':'))
            #return np.array_str(generator.simulate())

    if(action == 'listener'):
        return json.dumps({ 'answer': 'no'})

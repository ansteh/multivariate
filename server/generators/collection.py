import fs
from instance import Generator

blueprints = fs.get_blueprints()
instance = blueprints[0]
Generator(instance)

def get_instance():
    return instance

def find_print_by_url(url=""):
    try:
        return next(blueprint for blueprint in blueprints if blueprint['url'] == url)
    except StopIteration:
        return None

def handle(url):
    blueprint = find_print_by_url(url)
    return url

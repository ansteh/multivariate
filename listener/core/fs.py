import json
import os
import pandas as ps

blueprintPath = "blueprints"
resourcePath = "resources"

def get_blueprints():
    filenames = get_filenames_of_blueprints()
    return map(get_blueprint_options, filenames)

def get_filenames_of_blueprints():
    return filter(lambda file: file.endswith(".json"), os.listdir(blueprintPath))

def get_blueprint_options(filename=None):
    with open(blueprintPath+"/"+filename) as json_file:
        return json.load(json_file)

def get_csv_resource(filename):
    return ps.read_csv(os.path.join(os.path.dirname(__file__), "resources/"+filename), sep = ',')

import json
import os
import pandas as ps

blueprintPath = "generators/blueprints"
resourcePath = "generators/resources"

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
#print get_filenames_of_blueprints()
#print get_blueprint_options(get_files_of_blueprints()[0])
#print get_blueprints()

import json
import os

path = "generators/blueprints"

def get_blueprints():
    filenames = get_filenames_of_blueprints()
    return map(get_blueprint_options, filenames)

def get_filenames_of_blueprints():
    return filter(lambda file: file.endswith(".json"), os.listdir(path))

def get_blueprint_options(filename=None):
    with open(path+"/"+filename) as json_file:
        return json.load(json_file)

#print get_filenames_of_blueprints()
#print get_blueprint_options(get_files_of_blueprints()[0])
#print get_blueprints()

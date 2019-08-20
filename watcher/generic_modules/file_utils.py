import os
import yaml
import json
from JSONObject import JSONObject

PROJECT_ROOT = os.path.dirname(__file__) + '/..'
CONFIG_DIR = PROJECT_ROOT + '/config'


def load_config(yaml_file_name):
    file = open('{0}/{1}'.format(CONFIG_DIR, yaml_file_name))
    yml_content = json.dumps(yaml.safe_load(file))
    return json.loads(yml_content, object_hook=JSONObject)

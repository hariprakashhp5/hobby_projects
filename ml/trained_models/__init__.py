
import glob
import joblib
from os import path

current_dir = path.dirname(__file__)
available_models = dict()

files = glob.glob(path.join(current_dir, '*.*'))
for file in files:
    if not file.endswith('.py'):
        model_name = path.split(file)[-1].split('.')[0]
        available_models[model_name] = joblib.load(file)

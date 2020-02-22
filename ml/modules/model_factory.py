
from ml.modules.svm_model import SVMModel

model_map = dict(
    svm=SVMModel
)


def get_model(req_obj):
    req_params = req_obj.get_json()
    model_idf = req_params.get('model')
    model = model_map.get(model_idf)
    return model(req_obj)

import numpy as np
from ml.trained_models import  available_models


class SVMModel:

    __class_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

    def __init__(self, req_obj):
        req_params = req_obj.get_json()
        self.kernal_function = req_params.get('kf')
        self.data = np.array(req_params.get('ip_data'))
        self.model = available_models.get(f'svm_{self.kernal_function}')

    def get_prediction(self):
        prediction = self.model.predict(self.data.reshape(1, -1))[0]
        return dict(prediction=SVMModel.__class_mapping.get(prediction))

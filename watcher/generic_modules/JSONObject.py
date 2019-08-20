
class JSONObject:

    def __init__(self, obj):
        vars(self).update(obj)

    def __iter__(self):
        return iter(self.__dict__.items())

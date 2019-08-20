

def type_cast(str_obj, to):
    if to == int or to == float:
        str_obj = str_obj.replace(',', '')
    return to(str_obj)

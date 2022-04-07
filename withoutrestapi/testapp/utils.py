import json

def is_json(data):
    try:
        p_data = json.loads(data)
        valid_data= True
    except ValueError:
        valid_data = False
    return valid_data



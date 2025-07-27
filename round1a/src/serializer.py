import json

def serialize_to_json(data, indent=1):
    return json.dumps(data, indent=indent)

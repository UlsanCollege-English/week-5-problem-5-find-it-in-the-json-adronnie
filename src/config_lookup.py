# src/config_lookup.py

def find_key(data, key):
    if isinstance(data, dict):
        if key in data:
            return data[key]
        for value in data.values():
            result = find_key(value, key)
            if result is not None:
                return result
    elif isinstance(data, (list, tuple)):
        for item in data:
            result = find_key(item, key)
            if result is not None:
                return result
    return None

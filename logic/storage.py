import json
from json import JSONDecodeError

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return {}

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def find_website_data(filename, website):
    data = load_data(filename)
    return data.get(website)

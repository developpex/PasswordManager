import json
import tempfile
import os

from logic.storage import load_data, save_data, find_website_data

def test_save_and_load_data():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    filename = temp_file.name
    data = {"testsite.com": {"email": "test@example.com", "password": "abc123"}}

    save_data(filename, data)
    loaded = load_data(filename)

    assert loaded == data

def test_find_website_data():
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w+", suffix=".json")
    filename = temp_file.name
    test_data = {"testsite.com": {"email": "test@example.com", "password": "abc123"}}
    json.dump(test_data, temp_file)
    temp_file.close()

    result = find_website_data(filename, "testsite.com")

    assert result == {"email": "test@example.com", "password": "abc123"}

    os.remove(filename)


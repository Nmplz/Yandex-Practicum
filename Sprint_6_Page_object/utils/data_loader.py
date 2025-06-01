import json
import os


def load_test_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "order_data.json")
    with open(file_path, encoding="utf-8") as f:
        return json.load(f) 
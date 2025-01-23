import json
from pathlib import Path


def load_test_data(file_name):
    file_path = Path("test_data") / file_name
    with file_path.open() as f:
        return json.load(f)
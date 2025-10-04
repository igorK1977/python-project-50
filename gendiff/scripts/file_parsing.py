import json
import pathlib

import yaml


def read_file(file_path):
    match pathlib.PurePath(file_path).suffix:
        case '.json':
            return json.load(open(file_path))
        case '.yml' | '.yaml':
            with open(file_path) as f:
                return yaml.load(f, Loader=yaml.Loader)
        case _:
            return None
        
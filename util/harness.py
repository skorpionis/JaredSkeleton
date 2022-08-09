import json
from pathlib import Path

from lib.base_case import BaseCase


class Util(BaseCase):

    @staticmethod
    def read_json_from_file(file_name: str):
        txt_path = Path("json_body_files/", file_name)
        f = open(txt_path)
        data = json.load(f)
        f.close()
        return data

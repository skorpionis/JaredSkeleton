import json
import pandas as pd
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

    @staticmethod
    def read_url_from_json():
        txt_path = Path("json_body_files/", 'example.txt')
        f = open(txt_path)
        data = f.readline().replace('\n', '')
        return data

    @staticmethod
    def decoding():
        filepath = "data.txt"
        with open(filepath, 'r') as file:
            for line in file:
                data_pan = []
                if "accept-encoding: " in line:
                    encode = line.split(": ")[1]
                    print(encode)
                if "content-type: " in line:
                    content = line.split(": ")[1]
                    print(content)
                if "user-agent: " in line:
                    agent = line.split(": ")[1]
                    print(agent)
                if "connection: " in line:
                    connection = line.split(": ")[1]
                    print(connection)
                if "{\\" in line:
                    yy = line.encode('utf-8').decode('ascii', 'ignore')
                    y = json.loads(yy)
                    y = json.loads(y)
                    print(type(y))



        row = {"accept-encoding": encode,
                   "content-type": content,
                   "user-agent": agent,
                   "connection": connection}

        data_pan.append(row)

        data = pd.DataFrame(data_pan)
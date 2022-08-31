from pathlib import Path

import pandas as pd
import json

# filepath = "12.txt"
filepath = Path("../", "files/example.txt")

with open(filepath, 'r') as file:
    for line in file.readlines():
        data_pan = []
        # print(line)
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

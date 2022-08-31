import json
from pathlib import Path

# filepath = "12.txt"
filepath = Path("../", "files/example.txt")

with open(filepath, 'r') as file:
    for line in file.readlines():
        if line != "" and "api" not in line:
            headers_array = []
            # print(line)
            if "accept-encoding: " in line:
                encode = line.split(": ")[1]
            if "content-type: " in line:
                content = line.split(": ")[1]
            if "user-agent: " in line:
                agent = line.split(": ")[1]
            if "connection: " in line:
                connection = line.split(": ")[1]

        if "{\\" in line:
            if "true" and "false" not in line:
                before_decode = line.encode('utf-8').decode('ascii', 'ignore')
                body = json.loads(before_decode)
                body = json.loads(body)

    row = {"accept-encoding": encode,
           "content-type": content,
           "user-agent": agent,
           "connection": connection}

    headers_array.append(row)
    map_result_body = {"headers": row, "body": body}

    # row data = pd.DataFrame(data_pan)

import re
from pathlib import Path

filepath = Path("../", "files/example.txt")


def map_http_method_url():
    with open(filepath, 'r') as file:
        first_line = file.readline()
        res = re.findall("\S+", first_line)

        mas_text = []
        array = file.readlines()
        for line in array:
            if 'HTTP' in line:
                file.close()
            if line == "\n":
                file.close()
                break
            mas_text.append(line.strip("\n"))
        for i, word1 in enumerate(array):
            for word2 in array[i + 2:]:
                if word1 == "\n" and word2 == "\n" and array[i - 1].startswith('"{\\"'):
                    body = array[i - 1]
    return dict(http_method=res[0], url=res[1], headers=mas_text, body=body)


map_http_method_url()

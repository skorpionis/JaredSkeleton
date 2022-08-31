import re
from pathlib import Path

filepath = Path("../", "files/example.txt")


def map_http_method_url():
    with open(filepath, 'r') as file:
        first_line = file.readline()
        res = re.findall("\S+", first_line)

        mas_text = []
        for line in file.readlines():
                if 'HTTP' in line:
                    file.close()
                if line == "\n":
                    file.close()
                    break
                mas_text.append(line.strip("\n"))

    return dict(http_method=res[0], url=res[1], headers=mas_text)


# def asd():
#     data = None
#     with open(filepath, 'r') as file:
#         for line in file.readline():
#             linez = next(file)
#             if data is None:
#                 data = []
#             if 'HTTP' in linez:
#                 continue
#             elif linez == '\n' or linez == ' ':
#                 break
#             else:
#                 data = data.append(linez)
#     return data

# def map_headers():
#     data = None
#     with open(filepath, 'r') as file:
#         for line in file:  # iterate over the lines
#             if data is None:  # we haven't found `NODE*` yet
#                 if "POST" in line[:5]:  # search for `NODE*` at the line beginning
#                     data = []  # make `data` an empty list to begin collecting
#             elif "HTTP/1.1 200 OK" in line[:2]:  # data initialized, we look for the sequence's end
#                 break  # no need to iterate over the file anymore
#             else:  # data initialized but not at the end...
#                 data.append(line)  # append the line to our data
#     return data


# l = "t=xx.x;h=xx.x;b=xxx;s=xx;sn=xxx;".split(";")
# for e in l:
#     if not e: continue
#     k, v = e.split("=")
#     locals()[k] = v
map_http_method_url()

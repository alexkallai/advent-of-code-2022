
from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")
input = open(file_arg).read().split("$")[1:]

size = {}
cursor = []

for command in input:
    lines = command.strip().split("\n")
    if lines[0].startswith("cd"):
        d = lines[0][3:]
        if d == "/":
            cursor = []
        if d == "..":
            cursor.pop()
        else:
            cursor.append(d)
    else:
        for line in lines[1:]:
            if not line.startswith("dir"):
                s = int(line.split(" ")[0])
                for i in range(0, len(cursor)+1):
                    key = tuple(cursor[0:i])
                    size[key] = size.get(key, 0) + s

available = 70000000 - size[()]
space_to_free = 30000000 - available
print(sorted(v for v in size.values() if v >= space_to_free)[0])
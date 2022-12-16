from pathlib import Path
import os
import re

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for item_idx, line in enumerate(file_lines_list):
    file_lines_list[item_idx] = file_lines_list[item_idx].strip()
# FILE READ IN

class Vertex:

    def __init__(self, id, neighbours, flow_rate) -> None:
        self.id = id
        self.flow_rate = flow_rate
        self.neighbours = neighbours
    def __repr__(self) -> str:
        return str(f"{self.id} -  {self.flow_rate}  - {self.neighbours}")

list_of_nodes = []

# File parsing
for index, line in enumerate(file_lines_list):
    valve_ids = re.findall(r"[A-Z]{2}", line)
    actual_valve_id = valve_ids[0]
    connected_valves = valve_ids[1:]
    flow_rate = re.findall(r"[0-9]+", line)
    flow_rate = int(flow_rate[0])
    list_of_nodes.append(Vertex( actual_valve_id, connected_valves, flow_rate))

for node in list_of_nodes:
    print(node)
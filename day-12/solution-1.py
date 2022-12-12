from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for item_idx, line in enumerate(file_lines_list):
    file_lines_list[item_idx] = file_lines_list[item_idx].strip()
# FILE READ IN

elevation_values = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "10",
    "k": "11",
    "l": "12",
    "m": "13",
    "n": "14",
    "o": "15",
    "p": "16",
    "q": "17",
    "r": "18",
    "s": "19",
    "t": "20",
    "u": "21",
    "v": "22",
    "w": "23",
    "x": "24",
    "y": "25",
    "z": "26",
}

GRAPH_WIDTH = len(file_lines_list[0])
GRAPH_HEIGHT = len(file_lines_list)
parsed_graph = [[None] * GRAPH_HEIGHT for _ in range(GRAPH_WIDTH)]

class GraphVertex:

    def __init__(self,
                 x_coord,
                 y_coord,
                 upper_neighbour_distance,
                 lower_neighbour_distance,
                 left_neighbour_distance, 
                 right_neighbour_distance 
                 ):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.upper_neighbour_distance = upper_neighbour_distance
        self.lower_neighbour_distance = lower_neighbour_distance
        self.left_neighbour_distance  = left_neighbour_distance 
        self.right_neighbour_distance = right_neighbour_distance

for index, line in enumerate(file_lines_list):
    for char_index, char in enumerate(line):
        if char == "S":
            # has elevation "a"
            starting_location = [char_index, index]
        if char == "E":
            # has elevation "z"
            target_location = [char_index, index]


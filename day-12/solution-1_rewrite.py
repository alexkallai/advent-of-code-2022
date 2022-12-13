from pathlib import Path
import os
from dijkstar import Graph, find_path

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for item_idx, line in enumerate(file_lines_list):
    file_lines_list[item_idx] = file_lines_list[item_idx].strip()
# FILE READ IN

elevation_values = {
    "a": 1,
    "S": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "E": 26
}

def coordinate_key(coordinate):
    return str(coordinate[0], coordinate[1])

GRAPH_WIDTH = len(file_lines_list[0])
GRAPH_HEIGHT = len(file_lines_list)
parsed_graph = [[""] *  GRAPH_WIDTH for _ in range(GRAPH_HEIGHT)]
dict_of_vertices = {}

class GraphVertex:

    def __init__(self,
                 value,
                 list_of_valid_neighbours
                 ):
        self.value = value
        self.list_of_neighbours = list_of_valid_neighbours

    def __repr__(self) -> str:
        return str(self.value)
    def __str__(self) -> str:
        return str(self.value)

starting_location = None
target_location = None
for y_index, line in enumerate(file_lines_list):
    for x_index, char in enumerate(line):
        current_coordinate = (y_index, x_index)
        if char == "S":
            # has elevation "a"
            starting_location = (y_index, x_index)
            current_value = int(elevation_values['a'])
        elif char == "E":
            # has elevation "z"
            target_location = (y_index, x_index)
            current_value = int(elevation_values['z'])
        else:
            current_value = int(elevation_values[char])

        top_value    = int(elevation_values[file_lines_list[y_index - 1][x_index]]) if (y_index - 1) in range(GRAPH_HEIGHT) else None
        bottom_value = int(elevation_values[file_lines_list[y_index + 1][x_index]]) if (y_index + 1) in range(GRAPH_HEIGHT) else None
        right_value  = int(elevation_values[file_lines_list[y_index][x_index + 1]]) if (x_index + 1) in range(GRAPH_WIDTH) else None
        left_value   = int(elevation_values[file_lines_list[y_index][x_index - 1]]) if (x_index - 1) in range(GRAPH_WIDTH) else None

        top_diff =    top_value - current_value     if top_value != None else 99
        bottom_diff = bottom_value - current_value  if bottom_value != None else 99
        right_diff =  right_value - current_value   if right_value != None else 99
        left_diff =   left_value - current_value    if left_value != None else 99

        top_neighbour_index =    (y_index - 1, x_index)  if top_value != None else None
        bottom_neighbour_index = (y_index + 1, x_index)  if bottom_value != None else None
        right_neighbour_index =  (y_index, x_index + 1)  if right_value != None else None
        left_neighbour_index =   (y_index, x_index - 1)  if left_value != None else None

        list_of_valid_neighbours = [
            top_neighbour_index     if top_diff     < 2 else None,
            bottom_neighbour_index  if bottom_diff  < 2 else None,
            right_neighbour_index   if right_diff   < 2 else None,
            left_neighbour_index    if left_diff    < 2 else None
        ]


        current_graph_vertex = GraphVertex( 
                                            current_value, 
                                            list_of_valid_neighbours
                                            )
        dict_of_vertices.update({tuple(current_coordinate): current_graph_vertex})
        print(".")


graph = Graph()
for vertex in dict_of_vertices.keys():
    for neighbour in dict_of_vertices[vertex].list_of_neighbours:
        if neighbour != None:
            graph.add_edge(vertex, neighbour, 1)
print(find_path(graph, starting_location, target_location))
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

GRAPH_WIDTH = len(file_lines_list[0])
GRAPH_HEIGHT = len(file_lines_list)
parsed_graph = [[""] *  GRAPH_WIDTH for _ in range(GRAPH_HEIGHT)]

class GraphVertex:

    def __init__(self,
                 value,
                 upper_neighbour_distance,
                 lower_neighbour_distance,
                 left_neighbour_distance, 
                 right_neighbour_distance 
                 ):
        self.value = value
        self.upper_neighbour_distance = upper_neighbour_distance
        self.lower_neighbour_distance = lower_neighbour_distance
        self.left_neighbour_distance  = left_neighbour_distance
        self.right_neighbour_distance = right_neighbour_distance
    def __repr__(self) -> str:
        return str(self.value)
    def __str__(self) -> str:
        return str(self.value)

starting_location = None
target_location = None
for index, line in enumerate(file_lines_list):
    for char_index, char in enumerate(line):
        if char == "S":
            # has elevation "a"
            starting_location = [char_index, index]
            current_value = int(elevation_values['a'])
        elif char == "E":
            # has elevation "z"
            target_location = [char_index, index]
            current_value = int(elevation_values['z'])
        else:
            current_value = int(elevation_values[char])


        top_value    = int(elevation_values[file_lines_list[index - 1][char_index]])     if (index - 1) in range(0, GRAPH_HEIGHT) else None
        bottom_value = int(elevation_values[file_lines_list[index + 1][char_index]])     if (index + 1) in range(0, GRAPH_HEIGHT) else None
        right_value  = int(elevation_values[file_lines_list[index][char_index + 1]])     if (char_index + 1) in range(0, GRAPH_HEIGHT) else None
        left_value   = int(elevation_values[file_lines_list[index - 1][char_index - 1]]) if (char_index - 1) in range(0, GRAPH_HEIGHT) else None

        top_diff =    top_value - current_value         if top_value != None else None
        bottom_diff = bottom_value - current_value      if bottom_value != None else None
        right_diff =  right_value - current_value       if right_value != None else None
        left_diff =   left_value - current_value        if left_value != None else None

        try:
            parsed_graph[index][char_index] = GraphVertex(current_value, top_diff, bottom_diff, left_diff, right_diff)
        except:
            pass
        print(".")

def dijkstra(source_coord):
    global parsed_graph
    for index, line in enumerate(parsed_graph):
        for vertex_index, vertex in enumerate(line):


dijkstra(starting_location)



"""
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, parsed_graph, node: list): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in parsed_graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, parsed_graph, starting_location)    # function calling
"""
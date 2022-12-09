from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

head_dict = {
    "x": 0,
    "y": 0
}
tail_dict = {
    "x": 0,
    "y": 0
}
body_dicts = [
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0},
    {"x": 0,"y": 0}
]
direction_dict = {
    "L": "x",
    "R": "x",
    "D": "y",
    "U": "y"
}
direction_sign_dict = {
    "L": -1,
    "R":  1,
    "D": -1,
    "U":  1
}

def add_tail_to_location_list():
    global tail_location_list
    global body_dicts
    tail_location_list.append(f"{body_dicts[-1]['x']} {body_dicts[-1]['y']}")

def move_body_section(head_dict, body_element_index):
    global body_dicts
    x_difference = head_dict["x"] - body_dicts[body_element_index]["x"]
    y_difference = head_dict["y"] - body_dicts[body_element_index]["y"]
    head_dict_x_greater = head_dict["x"] > body_dicts[body_element_index]["x"]
    head_dict_y_greater = head_dict["y"] > body_dicts[body_element_index]["y"]

    x_abs_diff = abs(x_difference)
    y_abs_diff = abs(y_difference)

    # the sign of difference to be added to tail
    tail_diff_sign_dict = {
        "x": 1 if head_dict_x_greater else -1,
        "y": 1 if head_dict_y_greater else -1 
    }
    
    # if they are neighbours
    if x_abs_diff < 2 and y_abs_diff < 2:
        return 0
    # diagonal movement needed
    if (x_abs_diff == 2 and y_abs_diff == 2):
        body_dicts[body_element_index]["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 1)
        body_dicts[body_element_index]["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 1)
    # diagonal, but movement was different dir
    if x_abs_diff == 2 and y_abs_diff == 1:
        body_dicts[body_element_index]["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 1)
        body_dicts[body_element_index]["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 0)
    # diagonal, but movement was different dir
    if x_abs_diff == 1 and y_abs_diff == 2:
        body_dicts[body_element_index]["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 0)
        body_dicts[body_element_index]["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 1)
    #
    if x_abs_diff == 0 and y_abs_diff == 2:
        body_dicts[body_element_index]["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 1)
    #
    if x_abs_diff == 2 and y_abs_diff == 0:
        body_dicts[body_element_index]["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 1)
    return 1


tail_location_list = []

for index_row, row in enumerate(file_lines_list):
    print("Current row: ", row)
    direction = row.split(" ")[0]
    cycle = int(row.split(" ")[1])
    add_tail_to_location_list()

    for cycle_no in range(cycle):
        head_dict_initial =head_dict.copy()
        body_dicts[0][ direction_dict[ direction ] ] += direction_sign_dict[ direction ] * 1
        for body_element_index in range(len(body_dicts)-1):
            result = move_body_section(body_dicts[body_element_index], body_element_index+1)
            if result == 0:
                break
        add_tail_to_location_list()

solution_2 = len(set(tail_location_list))
print(solution_2)
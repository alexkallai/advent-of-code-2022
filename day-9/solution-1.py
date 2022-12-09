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
    global tail_dict
    tail_location_list.append(f"{tail_dict['x']} {tail_dict['y']}")

def move_tail(head_dict_initial, head_dict):
    global tail_dict
    x_difference = head_dict["x"] - tail_dict["x"]
    y_difference = head_dict["y"] - tail_dict["y"]
    #print("x diff", x_difference)
    #print("y diff", y_difference)
    head_dict_x_greater = head_dict["x"] > tail_dict["x"]
    head_dict_y_greater = head_dict["y"] > tail_dict["y"]
    #print("head x greater:", head_dict_x_greater)
    #print("head y greater:", head_dict_y_greater)

    x_abs_diff = abs(x_difference)
    y_abs_diff = abs(y_difference)

    # the sign of difference to be added to tail
    tail_diff_sign_dict = {
        "x": 1 if head_dict_x_greater else -1,
        "y": 1 if head_dict_y_greater else -1 
    }
    
    print("Head dict initial", head_dict_initial)
    print("Head dict        ", head_dict)
    print("Tail dict        ", tail_dict)
    # if they are neighbours
    if x_abs_diff < 2 and y_abs_diff < 2:
        print("-------------->")
        return
    print("#######")
    # diagonal movement needed
    if x_abs_diff == 2 and y_abs_diff == 2:
        tail_dict["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 1)
        tail_dict["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 1)
    # diagonal, but movement was different dir
    if x_abs_diff == 2 and y_abs_diff == 1:
        tail_dict["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 1)
        tail_dict["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 0)
    # diagonal, but movement was different dir
    if x_abs_diff == 1 and y_abs_diff == 2:
        tail_dict["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 0)
        tail_dict["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 1)
    #
    if x_abs_diff == 0 and y_abs_diff == 2:
        #tail_dict["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 1)
        tail_dict["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 1)
    #
    if x_abs_diff == 2 and y_abs_diff == 0:
        tail_dict["x"] += tail_diff_sign_dict["x"] * (x_abs_diff - 1)
        #tail_dict["y"] += tail_diff_sign_dict["y"] * (y_abs_diff - 1)
    print("Head dict initial", head_dict_initial)
    print("Head dict        ", head_dict)
    print("Tail dict        ", tail_dict)
    pass


tail_location_list = []

for index_row, row in enumerate(file_lines_list):
    print("Current row: ", row)
    direction = row.split(" ")[0]
    cycle = int(row.split(" ")[1])
    #add_tail_to_location_list()

    for cycle_no in range(cycle):
        add_tail_to_location_list()
        head_dict_initial =head_dict.copy()
        head_dict[ direction_dict[ direction ] ] += direction_sign_dict[ direction ] * 1
        move_tail(head_dict_initial, head_dict)

        #print(f"Moving in the direction of: {direction_dict[direction]}")
        #print("Tail dict", tail_dict)
        #print("Head dict", head_dict)



solution_1 = len(set(tail_location_list))
print(solution_1)
print("6180 too low")
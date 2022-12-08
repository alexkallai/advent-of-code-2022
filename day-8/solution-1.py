from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

def check_if_actual_visible(row_idx, column_idx):
    global file_lines_list
    current_element = int(file_lines_list[row_idx][column_idx])
    if row_idx == 0 or column_idx == 0 or row_idx == len(file_lines_list)-1 or column_idx == len(file_lines_list[row_idx])-1:
        return True
    
    height = len(file_lines_list)
    width = len(file_lines_list[0])
    visible_from_left = True
    visible_from_right = True
    for runner_idx in range(row_idx-1, -1, -1):
        runner_element = int(file_lines_list[runner_idx][column_idx])
        if runner_element >= current_element:
            visible_from_left = False
    for runner_idx in range(row_idx+1, width):
        runner_element = int(file_lines_list[runner_idx][column_idx])
        if runner_element >= current_element:
            visible_from_right = False


    visible_from_top = True
    visible_from_bottom = True
    for runner_idx in range(column_idx-1, -1, -1):
        runner_element = int(file_lines_list[row_idx][runner_idx]) 
        if runner_element >= current_element:
            visible_from_top = False
    for runner_idx in range(column_idx+1, height):
        runner_element = int(file_lines_list[row_idx][runner_idx])
        if runner_element >= current_element:
            visible_from_bottom = False
    
    is_visible = visible_from_bottom or visible_from_top or visible_from_right or visible_from_left
    return is_visible


sum_of_visible_trees = 0
for index_row, row in enumerate(file_lines_list):
    for index_column, column_element in enumerate(row):
        if check_if_actual_visible(index_row, index_column):
            sum_of_visible_trees += 1

print(sum_of_visible_trees)
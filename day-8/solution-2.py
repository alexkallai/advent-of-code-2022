from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

def get_view_score(row_idx, column_idx):
    global file_lines_list
    height = len(file_lines_list)
    width = len(file_lines_list[0])
    current_element = int(file_lines_list[row_idx][column_idx])

    viewing_score_up = 0
    viewing_score_left = 0
    viewing_score_down = 0
    viewing_score_right = 0
    
    visible_from_left = True
    visible_from_right = True
    for runner_idx in range(row_idx-1, -1, -1):
        runner_element = int(file_lines_list[runner_idx][column_idx])
        viewing_score_up += 1
        if runner_element >= current_element:
            break
    for runner_idx in range(row_idx+1, width):
        runner_element = int(file_lines_list[runner_idx][column_idx])
        viewing_score_down += 1
        if runner_element >= current_element:
            break


    visible_from_top = True
    visible_from_bottom = True
    for runner_idx in range(column_idx-1, -1, -1):
        runner_element = int(file_lines_list[row_idx][runner_idx]) 
        viewing_score_left += 1
        if runner_element >= current_element:
            break
    for runner_idx in range(column_idx+1, height):
        runner_element = int(file_lines_list[row_idx][runner_idx])
        viewing_score_right += 1
        if runner_element >= current_element:
            break
    
    view_score = viewing_score_left * viewing_score_right * viewing_score_down * viewing_score_up
    print(current_element, ":", "up ", viewing_score_up, "left ", viewing_score_left, "down ", viewing_score_down, "right ", viewing_score_right, "---", view_score)
    return view_score


max_view_score = 0
for index_row, row in enumerate(file_lines_list):
    for index_column, column_element in enumerate(row):
        current_score = get_view_score(index_row, index_column)
        if current_score > max_view_score:
            max_view_score = current_score

print(max_view_score)
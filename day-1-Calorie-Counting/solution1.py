from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

# INPUT FILE ALREADY READ IN

def add_calories(list_of_calorie_values):
    total = 0
    for value in list_of_calorie_values:
        total += int(value)
    return total

from_idx = 0
max_calorie_value = 0

runner_index = 0
while runner_index < len(file_lines_list):

    if file_lines_list[runner_index] == "\n":
        actual_calorie_value = add_calories(file_lines_list[from_idx:runner_index])
        if actual_calorie_value > max_calorie_value:
            max_calorie_value = actual_calorie_value
        from_idx = runner_index +1

    runner_index += 1
print(max_calorie_value)
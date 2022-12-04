from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# FILE READ IN

number_of_fully_contained = 0
for line in file_lines_list:
    range_1_1 = int(line.split(",")[0].split("-")[0])
    range_1_2 = int(line.split(",")[0].split("-")[1])
    range_2_1 = int(line.split(",")[1].split("-")[0])
    range_2_2 = int(line.split(",")[1].split("-")[1])
    list_1 = []
    list_2 = []
    for element in range(range_1_1-1, range_1_2):
        list_1.append(int(element))
    for element in range(range_2_1-1, range_2_2):
        list_2.append(int(element))
    set_1 = set(list_1)
    set_2 = set(list_2)
    if set_1.issubset(set_2) or set_2.issubset(set_1):
        number_of_fully_contained += 1

print(number_of_fully_contained)
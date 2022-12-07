from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input_first_part.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# FILE READ IN

list_of_lists = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

for index, line in enumerate(file_lines_list):
    for index_char, char in enumerate(line):
        if (index_char-1) % 4 == 0:
            if line[index_char].isalpha():
                list_of_lists[index_char-1].insert(0, char)
                pass

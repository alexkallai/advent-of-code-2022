from pathlib import Path
import os
import benedict

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# FILE READ IN

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()

file_struct_dict_cursor = []
file_struct_dict = benedict.BeneDict()

current_command = ""
current_command_argument = ""
for index, line in enumerate(file_lines_list):
    if line.startswith("$"):
        current_command = line.split(" ")[1]
        continue
    if current_command == "cd":
        current_command_argument = line.split(" ")[2]

        if current_command_argument == "..":
            file_struct_dict_cursor.pop()
        elif current_command_argument == "/":
            file_struct_dict_cursor = []
        else:
            file_struct_dict_cursor.append(current_command_argument)
    if not line.startswith("$"):
        if current_command == "ls":
            if line.startswith("dir"):
                dir_name = line.split(" ")[-1]
                if file_struct_dict_cursor:
                    file_struct_dict[file_struct_dict_cursor] = {"dir": dir_name}
                else:
                    file_struct_dict["dir"] = dir_name

            if not line.startswith("dir"):
                file_size = line.split(" ")[0]
                file_name_with_ext = line.split(" ")[1]

                #file_name = file_name_with_ext.split(".")[0]
                #file_ext = file_name_with_ext.split(".")[1]
                if file_struct_dict_cursor:
                    file_struct_dict[file_struct_dict_cursor] = {file_name_with_ext: file_size}
                else:
                    file_struct_dict[file_name_with_ext] = file_size


    pass
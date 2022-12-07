from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

file_struct_dict_cursor = ["\\"]
file_struct_dict = {}

current_command = ""
current_command_argument = ""
for index, line in enumerate(file_lines_list):
    if line.startswith("$"):
        current_command = line.split(" ")[1]
    if current_command == "cd":
        current_command_argument = line.split(" ")[-1]

        if current_command_argument == "..":
            file_struct_dict_cursor.pop()
        elif current_command_argument == "/":
            file_struct_dict_cursor = ["\\"]
        else:
            file_struct_dict_cursor.append(current_command_argument)

    file_struct_dict_cursor_merged = os.path.join(*file_struct_dict_cursor)

    if not line.startswith("$"):
        if current_command == "ls":
            # if dir
            #if line.startswith("dir"):
                #dir_name = line.split(" ")[-1]
                #file_struct_dict.update({os.path.join(file_struct_dict_cursor_merged): dir_name})
            # if file
            if not line.startswith("dir"):
                file_size = line.split(" ")[0]
                file_name_with_ext = line.split(" ")[1]
                file_struct_dict.update({os.path.join(file_struct_dict_cursor_merged+file_name_with_ext): file_size})

    pass
files_path_list = list(file_struct_dict.keys())
files_path_list.sort()

dict_of_files = {}
for line in files_path_list:
    print(line)
    file_name = line.split("\\")[-1]
    folder_name = line.rpartition("\\")[0]
    print("\t"+folder_name)
    print("\t"+file_name)
    if folder_name in dict_of_files.keys():
        dict_of_files[folder_name].extend([file_name])
    else:
        dict_of_files.update({folder_name: [file_name]})
def sum_keys(path, filename):

size_of_dicts
for key in dict_of_files:
    

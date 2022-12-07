from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN


file_struct_dict_cursor = ["/"]
file_struct_list = []

# iterate through all lines
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
            file_struct_dict_cursor = ["/"]
        else:
            file_struct_dict_cursor.append(current_command_argument)

    if not line.startswith("$"):
        if current_command == "ls":
            if not line.startswith("dir"):
                file_size = int(line.split(" ")[0])
                file_name_with_ext = line.split(" ")[1]
                current_file_full_path = []
                current_file_full_path.extend(file_struct_dict_cursor)
                #current_file_full_path.append(file_name_with_ext)
                if [current_file_full_path, file_name_with_ext, file_size] not in file_struct_list:
                    file_struct_list.append([current_file_full_path, file_name_with_ext, file_size])

#file_struct_list.sort()

dir_sum_dict = {}
for line in file_struct_list:
    print(line)
    current_file_path = str(line[0])
    current_file_size = line[-1]
    if current_file_path in dir_sum_dict.keys():
        dir_sum_dict[current_file_path] += current_file_size
    else:
        dir_sum_dict.update({current_file_path: current_file_size})

real_dir_size_dict = dict(dir_sum_dict)
for line in real_dir_size_dict:
    #print(line, dir_sum_dict[line])
    for line_2 in dir_sum_dict:
        if line != line_2:
            #print(line)
            #print(line_2)
        # if line is parent dir to the current dir
            line_in_line_2 = all(elem in line_2 for elem in line)
            if line_in_line_2:
                real_dir_size_dict[line] += dir_sum_dict[line_2]

print("\n\n")
sum_of_lower_than_100000 = 0
for line in real_dir_size_dict:
    value = real_dir_size_dict[line]
    print(line, value)
    if value <= 100000:
        sum_of_lower_than_100000 += value
print(sum_of_lower_than_100000)
print("17823116 too high")
print("127250 too high")
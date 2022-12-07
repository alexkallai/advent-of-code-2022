from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# FILE READ IN

first_start_packet_location = 0
for index, line in enumerate(file_lines_list):
    for index_l, line_str in enumerate(line):
        if len(set(line[index_l:index_l+4])) == 4:
            print(line_str[index_l:index_l+4])
            print(set(line_str[index_l:index_l+4]))
            print(index_l+4)
            first_start_packet_location = index_l+4
            break

start_of_message_len = 14
first_start_of_message_location = 0
for index, line in enumerate(file_lines_list):
    for index_l, line_str in enumerate(line):
        if len(set(line[index_l:index_l+start_of_message_len])) == start_of_message_len:
            print(line_str[index_l:index_l+start_of_message_len])
            print(set(line_str[index_l:index_l+start_of_message_len]))
            print(index_l+start_of_message_len)
            first_start_of_message_location = index_l+start_of_message_len
            break
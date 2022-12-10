from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

def print_screen():
    global screen
    for line in screen:
        print(''.join(line))

def check_cycle(cycle_index):
    global register
    global CRT_HEIGHT
    global CRT_WIDTH
    global screen
    screen_line_number = int(cycle_index / CRT_WIDTH)
    screen_char_index = int(cycle_index % CRT_WIDTH)
    print(cycle_index)
    print("line ", screen_line_number)
    print("char ", screen_char_index)
    print("sprite:")
    print("\n")

    sprite_index_list = [register, register+1, register+2]
    if screen_char_index in sprite_index_list:
        screen[screen_line_number][screen_char_index] = "#"
    else:
        screen[screen_line_number][screen_char_index] = "."


CRT_WIDTH = 40
CRT_HEIGHT = 6

screen = [["-"] * CRT_WIDTH for _ in range(CRT_HEIGHT)]
register = 1
cycle_index = 1

for index, line in enumerate(file_lines_list):
    instruction = line.split(" ")[0] if " " in line else line
    argument = int(line.split(" ")[1]) if " " in line else None

    if instruction == "addx":
        check_cycle(cycle_index)
        cycle_index += 1
        check_cycle(cycle_index)
        register += argument
        cycle_index += 1

    if instruction == "noop":
        check_cycle(cycle_index)
        cycle_index += 1

print_screen()
# EPJBRKAH
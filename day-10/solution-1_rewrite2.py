from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip()
# FILE READ IN

def check_cycle(cycle_index):
    print(cycle_index)
    global sum_of_signal_strength
    global register

    cycles_to_check = [
    20,
    60,
    100,
    140,
    180,
    220
    ]

    if cycle_index in cycles_to_check:
        sum_of_signal_strength += register * cycle_index
    
sum_of_signal_strength = 0
register = 1
cycle_index = 1
for index, line in enumerate(file_lines_list):
    instruction = line.split(" ")[0] if " " in line else line
    argument = int(line.split(" ")[1]) if " " in line else None

    if instruction == "addx":
        # wait a cycle then add to register
        check_cycle(cycle_index)
        cycle_index += 1
        check_cycle(cycle_index)
        register += argument
        cycle_index += 1

    if instruction == "noop":
        # wait a cycle
        check_cycle(cycle_index)
        cycle_index += 1

print("10140, 11560, 12720 14700 incorrect")
print(sum_of_signal_strength)
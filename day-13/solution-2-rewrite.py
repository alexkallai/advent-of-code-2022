from pathlib import Path
import os
import ast

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for item_idx, line in enumerate(file_lines_list):
    file_lines_list[item_idx] = file_lines_list[item_idx].strip()
# FILE READ IN

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print("Left side is smaller, so inputs are in the right order")
            return 1
        if left > right:
            print("Right side is smaller, so inputs are NOT in the right order")
            return -1
        if left == right:
            print("The two elements are equal, continue")
            return 0
    else:
        if isinstance(right, int):
            right = [right]
        if isinstance(left, int):
            left = [left ]
        for left_element, right_element in zip(left, right):
            result = compare(left_element, right_element)
            if result != 0:
                return result
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0
            

from_idx = 0
actual_pair_index = 1
sum_of_indeces = 0
runner_index = 0
list_of_all_lines = []
while runner_index < len(file_lines_list):

    if file_lines_list[runner_index] == "":
        current_pair = file_lines_list[from_idx:runner_index]
        current_pair[0] = ast.literal_eval(current_pair[0])
        current_pair[1] = ast.literal_eval(current_pair[1])
        print(f"Pair {actual_pair_index}")
        in_the_right_order = compare(current_pair[0], current_pair[1])
        list_of_all_lines.append(current_pair[0])
        list_of_all_lines.append(current_pair[1])
        print(f"Compare returned with {in_the_right_order}")

        if in_the_right_order >= 0:
            print(f"Adding {actual_pair_index} to sum")
            sum_of_indeces += actual_pair_index

        print("\n")
        actual_pair_index += 1
        from_idx = runner_index +1

    runner_index += 1

print(sum_of_indeces)

divider_packets = [ [[2]], [[6]]]
list_of_all_lines.append(divider_packets[0])
list_of_all_lines.append(divider_packets[1])
print(list_of_all_lines)


def all_lines_in_order():
    global list_of_all_lines
    for index, line in enumerate(list_of_all_lines):
        if index < len(list_of_all_lines)-1:
            if compare(list_of_all_lines[index], list_of_all_lines[index+1]) < 0:
                return False
    return True

def swap(first, second):
    a = list_of_all_lines[first]
    b = list_of_all_lines[second]
    list_of_all_lines[first] = b
    list_of_all_lines[second] = a
    

while not all_lines_in_order():
    for index, line in enumerate(list_of_all_lines):
        if index < len(list_of_all_lines)-1:
            if compare(list_of_all_lines[index], list_of_all_lines[index+1]) < 0:
                swap(index, index+1)

index_divider_packet_1 = list_of_all_lines.index(divider_packets[0])+1
index_divider_packet_2 = list_of_all_lines.index(divider_packets[1])+1
print(list_of_all_lines)
print(index_divider_packet_1*index_divider_packet_2)
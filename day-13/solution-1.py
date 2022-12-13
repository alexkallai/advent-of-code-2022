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

def compare(current_slice) -> bool:
    left = current_slice[0]
    right = current_slice[1]
    len_left = len(left)
    len_right = len(right)
    print(f"Compare {left} vs {right}")

    is_the_order_correct = None
    # left should be lower!
    for idx in range(max(len_left, len_right) + 1):
        if idx >= len_left:
            print("ran out of elements!")
            print("right order!")
            return True
        if idx >= len_right:
            print("ran out of elements!")
            print("NOT right order!")
            return False

        lower = left[idx]
        higher = right[idx]
        print(f"\tCompare {lower} vs {higher}")
        pass

        # if both are integers:
        if isinstance(left[idx], int) and isinstance(right[idx], int):
            if higher < lower:
                print("NOT right order!")
                return False
            if higher > lower:
                print("right order!")
                return True
            if higher == lower:
                continue

        # both are lists
        if isinstance(left[idx], list) and isinstance(right[idx], list):
            return compare([left[idx], right[idx]])

        # only left is int
        if isinstance(left[idx], int) and not isinstance(right[idx], int):
            return compare( [[left[idx]], right[idx]] )

        # only right is int
        if not isinstance(left[idx], int) and isinstance(right[idx], int):
            return compare( [left[idx], [right[idx]]] )

from_idx = 0

sum_of_indeces = 0
pair_indeces = 1

list_runner_index = 0
while list_runner_index < len(file_lines_list):

    if file_lines_list[list_runner_index] == "":
        current_slice = file_lines_list[from_idx:list_runner_index]

        current_slice[0] = ast.literal_eval(current_slice[0])
        current_slice[1] = ast.literal_eval(current_slice[1])

        current_slice_is_in_right_order = compare(current_slice)
        if current_slice_is_in_right_order == None:
            pass
        if current_slice_is_in_right_order == True:
            sum_of_indeces += pair_indeces # first pair has index 1
            print(f"Added pair index: {pair_indeces}")
            pass


        pair_indeces += 1
        from_idx = list_runner_index +1
        print("\n")

    list_runner_index += 1

print(sum_of_indeces)
print("5971 too high, 516 too low")
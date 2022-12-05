from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# FILE READ IN

initial_list = [
["R", "S", "L", "F", "Q"],
["N", "Z", "Q", "G", "P", "T"],
["S", "M", "Q", "B"],
["T", "G", "Z", "J", "H", "C", "B", "Q"],
["P", "H", "M", "B", "N", "F", "S"],
["P", "C", "Q", "N", "S", "L", "V", "G"],
["W", "C", "F"],
["Q", "H", "G", "Z", "W", "V", "P", "M",],
["G", "Z", "D", "L", "C", "N", "R"]
]

for index, line in enumerate(file_lines_list):
    how_many = int(line.split(" ")[1])
    where_from = int(line.split(" ")[3])
    where_to = int(line.split(" ")[5])

    initial_list[where_to-1].extend(initial_list[where_from-1][0-how_many:])
    del initial_list[where_from-1][0-how_many:]

print("\n")
for index, line in enumerate(initial_list):
    print(line[-1])
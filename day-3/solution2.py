with open("input.txt", "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# INPUT FILE ALREADY READ IN

item_dict = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "10",
    "k": "11",
    "l": "12",
    "m": "13",
    "n": "14",
    "o": "15",
    "p": "16",
    "q": "17",
    "r": "18",
    "s": "19",
    "t": "20",
    "u": "21",
    "v": "22",
    "w": "23",
    "x": "24",
    "y": "25",
    "z": "26",
    "A": "27",
    "B": "28",
    "C": "29",
    "D": "30",
    "E": "31",
    "F": "32",
    "G": "33",
    "H": "34",
    "I": "35",
    "J": "36",
    "K": "37",
    "L": "38",
    "M": "39",
    "N": "40",
    "O": "41",
    "P": "42",
    "Q": "43",
    "R": "44",
    "S": "45",
    "T": "46",
    "U": "47",
    "V": "48",
    "W": "49",
    "X": "50",
    "Y": "51",
    "Z": "52"
}

elf_sum = 0
runner_idx = 0
while runner_idx < len(file_lines_list):
    elf_1 = file_lines_list[runner_idx].strip()
    elf_2 = file_lines_list[runner_idx+1].strip()
    elf_3 = file_lines_list[runner_idx+2].strip()
    elf_1_set = set(elf_1)
    elf_2_set = set(elf_2)
    elf_3_set = set(elf_3)
    elf_intersect = elf_1_set.intersection(elf_2_set).intersection(elf_3_set)
    intersect_char = str(next(iter(elf_intersect)))
    elf_sum += int(item_dict[intersect_char])

    runner_idx += 3
print(elf_sum)
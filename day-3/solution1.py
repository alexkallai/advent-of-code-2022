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

total_sum = 0
for line in file_lines_list:
    line_length = len(line)
    half = int(line_length/2)
    compartment_1 = line[:half]
    compartment_2 = line[half:]
    set_compartment_1 = set(compartment_1)
    set_compartment_2 = set(compartment_2)

    intersect = set_compartment_1.intersection(set_compartment_2)
    intersect_char = str(next(iter(intersect)))
    total_sum += int(item_dict[intersect_char])

print(total_sum)
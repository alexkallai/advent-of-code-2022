from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# INPUT FILE ALREADY READ IN
dict_enemy = {
"A": "rock",
"B": "paper",
"C": "scissors"
}
dict_me = {
"X": "rock",
"Y": "paper",
"Z": "scissors"
}
dict_who_beats_who = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
dict_who_loses_to_who = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}
dict_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

my_total_score = 0
for index, line in enumerate(file_lines_list):
    enemy_draw = line.split(" ")[0]
    my_draw = line.split(" ")[1].strip()

    my_draw_plain = dict_me[my_draw]
    enemy_draw_plain = dict_enemy[enemy_draw]
    draw = 0
    if enemy_draw_plain == my_draw_plain:
        draw = 1

    i_won = 0
    if draw != 1:
        if dict_who_beats_who[my_draw_plain] == enemy_draw_plain:
            i_won = 1
        else:
            i_won = 0
    this_rounds_score = i_won * 6 + dict_points[my_draw_plain] + draw * 3
    my_total_score += this_rounds_score

print(my_total_score)


from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()
# INPUT FILE ALREADY READ IN

my_dict = {
"X": "lose",
"Y": "draw",
"Z": "win"
}
enemy_dict = {
"A": "rock",
"B": "paper",
"C": "scissors"
}
value_dict = {
"rock": 1,
"paper": 2,
"scissors": 3
}
outcome_value_dict = {
"lose": 0,
"draw": 3,
"win": 6
}
# enemy draw : my draw
draw_this_to_win = {
"rock": "paper",
"paper": "scissors",
"scissors": "rock"
}
draw_this_to_lose = {
"rock": "scissors",
"paper": "rock",
"scissors": "paper"
}
draw_this_to_draw = {
"rock": "rock",
"paper": "paper",
"scissors": "scissors"
}
win_lose_draw_dicts = {
"win": draw_this_to_win,
"draw": draw_this_to_draw,
"lose": draw_this_to_lose
}

total_score = 0
for line in file_lines_list:
    enemy_draw_raw = line.split(" ")[0]
    my_draw_raw = line.split(" ")[1].strip()

    enemy_draw_evaluated = enemy_dict[enemy_draw_raw]

    should_i_win_lose_draw = my_dict[my_draw_raw]
    dict_to_get_what_i_should_draw_from = win_lose_draw_dicts[should_i_win_lose_draw]
    my_draw_evaluated = dict_to_get_what_i_should_draw_from[enemy_draw_evaluated]

    this_rounds_sum = value_dict[my_draw_evaluated] + outcome_value_dict[should_i_win_lose_draw]
    total_score += this_rounds_sum

print(total_score)
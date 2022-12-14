from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for item_idx, line in enumerate(file_lines_list):
    file_lines_list[item_idx] = file_lines_list[item_idx].strip()
# FILE READ IN


max_x = 0
min_x = 10000
max_y = 0
min_y = 10000
list_of_path_endpoints = []
set_of_populated_coordinates = set()
for index, line in enumerate(file_lines_list):
    split_line = line.split(" -> ")
    for idx, i in enumerate(split_line):
        current_x = int( i.split(",")[0] )
        current_y = int( i.split(",")[-1])
        split_line[idx] = [current_x, current_y]
        set_of_populated_coordinates.add((current_x, current_y))

        if current_x > max_x:
            max_x = current_x
        if current_x < min_x:
            min_x = current_x
        if current_y > max_y:
            max_y = current_y
        if current_y < min_y:
            min_y = current_y
    list_of_path_endpoints.append(split_line)
    pass

for index, line in enumerate(list_of_path_endpoints):
    for index_e, endpoint in enumerate(line):
        if index_e < len(line) - 1:
            current_x_value = line[index_e][0]
            next_x_value = line[index_e + 1][0]

            current_y_value = line[index_e][1]
            next_y_value = line[index_e + 1][1]

            if current_x_value != next_x_value:
                step = 1 if next_x_value > current_x_value else -1
                for x in range(current_x_value, next_x_value + step, step):
                    set_of_populated_coordinates.add((x, current_y_value))

            if current_y_value != next_y_value:
                step = 1 if next_y_value > current_y_value else -1
                for y in range(current_y_value, next_y_value + step, step):
                    set_of_populated_coordinates.add((current_x_value, y))

print(set_of_populated_coordinates)
print(f"Max x: {max_x} max y: {max_y}")
print(f"Min x: {min_x} min y: {min_y}")
print(set_of_populated_coordinates)

infinite_line_y_coordinate = max_y + 2

for x_index in range(min_x - 1000, max_x + 1000):
    set_of_populated_coordinates.add((x_index, infinite_line_y_coordinate))

# min should be 0?
MAP_WIDTH = len(range(0, max_x))+1
MAP_HEIGHT = len(range(0, max_y))+1
print(f"Map width: {MAP_WIDTH} map height: {MAP_HEIGHT}")
parsed_graph = [[""] *  MAP_WIDTH for _ in range(MAP_HEIGHT)]

STARTING_POINT = [500, 0]

number_of_sand_particles = 0

sand_particle_x = STARTING_POINT[0]
sand_particle_y = STARTING_POINT[1]
outer_while_idx = 0


print(f"Outer while: {outer_while_idx}")
outer_while_idx += 1
sand_particle_x = STARTING_POINT[0]
sand_particle_y = STARTING_POINT[1]
number_of_sand_particles += 1
print(f"Sand particles so far: {number_of_sand_particles}")

inner_while_idx = 0

while not (
    (sand_particle_x, sand_particle_y + 1) in set_of_populated_coordinates and
    (sand_particle_x - 1, sand_particle_y + 1) in set_of_populated_coordinates and
    (sand_particle_x + 1, sand_particle_y + 1) in set_of_populated_coordinates and
    sand_particle_x == STARTING_POINT[0] and
    sand_particle_y == STARTING_POINT[1]
    ):


    if not (sand_particle_x, sand_particle_y + 1) in set_of_populated_coordinates:
        #print(f"Empty below")
        sand_particle_y += 1
        continue
    elif not (sand_particle_x - 1, sand_particle_y + 1) in set_of_populated_coordinates:
        sand_particle_x -= 1
        sand_particle_y += 1
        #print(f"Not empty below, empty down, left")
        continue
    elif not (sand_particle_x + 1, sand_particle_y + 1) in set_of_populated_coordinates:
        sand_particle_x += 1
        sand_particle_y += 1
        #print(f"Not empty below, empty down, right")
        continue
    else:
        set_of_populated_coordinates.add((sand_particle_x, sand_particle_y))
        number_of_sand_particles += 1
        #print(f"All 3 populated")
        sand_particle_x = STARTING_POINT[0]
        sand_particle_y = STARTING_POINT[1]
        continue

print("Number of particles: ", number_of_sand_particles)
from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for item_idx, line in enumerate(file_lines_list):
    file_lines_list[item_idx] = file_lines_list[item_idx].strip()
# FILE READ IN

class Sensor:

    def __init__(self, sensor_x, sensor_y):
        self.x = sensor_x
        self.y = sensor_y
class Beacon:

    def __init__(self, closest_beacon_x, closest_beacon_y):
        self.x = closest_beacon_x
        self.y = closest_beacon_y

def manhattan_distance(x1, x2, y1, y2):
    return abs(x1-x2)+abs(y1-y2)


min_x = 0
max_x = 0
min_x = 0
max_y = 0

set_of_beacons = set()
set_of_sensors = set()
list_of_sensors = []
list_of_beacons = []
list_of_devices = []
# File parsing
for index, line in enumerate(file_lines_list):
    sensor_part = line.split(":")[0]
    closest_beacon_part = line.split(":")[1]
    sensor_x = int( sensor_part.split(",")[-2].split(" ")[-1].replace("x=", "").replace(",", "").strip() )
    sensor_y = int( sensor_part.split(",")[-1].replace("y=", "").replace(",", "").strip() )

    closest_beacon_x = int(closest_beacon_part.split(",")[-2].split(" ")[-1].replace("x=", "").replace(",", "").strip() )
    closest_beacon_y = int(closest_beacon_part.split(",")[-1].replace("y=", "").replace(",", "").strip() )
    list_of_sensors.append(Sensor(
        sensor_x,
        sensor_y
    ))
    list_of_beacons.append(Beacon(
        closest_beacon_x,
        closest_beacon_y
    ))
    set_of_sensors.add((sensor_x, sensor_y))
    set_of_beacons.add((closest_beacon_x, closest_beacon_y))
    list_of_devices.append(
        [Beacon(closest_beacon_x, closest_beacon_y),
        Sensor(sensor_x, sensor_y)]
    )


set_of_all_checked_coordinates = set()

for device in list_of_devices:
    sensor_x = device[1].x
    sensor_y = device[1].y
    beacon_x = device[0].x
    beacon_y = device[0].y
    current_sensor_beacon_manhattan_distance = manhattan_distance(beacon_x, sensor_x, beacon_y, sensor_y)

    for x_runner in range(sensor_x - current_sensor_beacon_manhattan_distance, sensor_x + current_sensor_beacon_manhattan_distance + 1):
        for y_runner in range( sensor_y - current_sensor_beacon_manhattan_distance, sensor_y + current_sensor_beacon_manhattan_distance + 1):

            current_manhattan_distance = manhattan_distance(x_runner, sensor_x, y_runner, sensor_y)
            if current_manhattan_distance <= current_sensor_beacon_manhattan_distance:
                set_of_all_checked_coordinates.add((x_runner, y_runner))

print("Last section")
number_of_taken_positions = 0
#sensor_y = 10
sensor_y = 2000000
for x_runner in range(-10000000, 10000000):
    if (x_runner, sensor_y) in set_of_all_checked_coordinates:
        number_of_taken_positions += 1

print(number_of_taken_positions)


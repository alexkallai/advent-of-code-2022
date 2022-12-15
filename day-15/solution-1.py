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

set_of_beacons = set()
set_of_sensors = set()
list_of_sensors = []
list_of_beacons = []
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

runner_distance = 0
runner_element = None

while runner_element != "":
    pass

from pathlib import Path
import os
import operator
import math

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for item_idx, line in enumerate(file_lines_list):
    file_lines_list[item_idx] = file_lines_list[item_idx].strip()
# FILE READ IN

class Monkey:

    def __init__(self, monkey_number, starting_items, operation_operator, operation_argument, divisibility_number, where_to_if_true, where_to_if_false):
        self.monkey_number: int = monkey_number
        self.items: list = starting_items
        self.operation_operator: operator = operation_operator
        self.operation_argument = operation_argument
        self.divisibility_number: int = divisibility_number
        self.where_to_if_true: int = where_to_if_true
        self.where_to_if_false: int = where_to_if_false
    
    def __repr__(self) -> str:
        return str(self.items)

def analyze_monkey_instance(list_slice):
    operator_dict = {
        "+": operator.add,
        "*": operator.mul
    }
    print(list_slice)
    monkey_number = list_slice[0].split(" ")[-1].replace(":", "")
    starting_items = list_slice[1].split(":")[-1].split(",")
    for index, item in enumerate(starting_items):
        starting_items[index] = int(starting_items[index].strip())
    operation_operator = list_slice[2].split("=")[-1].strip().split(" ")[1]
    operation_argument = list_slice[2].split("=")[-1].split(" ")[-1]
    divisibility_number = int(list_slice[3].split(" ")[-1].strip())
    where_to_if_true = int(list_slice[4].split(" ")[-1].strip())
    where_to_if_false = int(list_slice[5].split(" ")[-1].strip())

    return Monkey(monkey_number, 
                  starting_items, 
                  operator_dict[operation_operator], 
                  operation_argument, 
                  divisibility_number, 
                  where_to_if_true, 
                  where_to_if_false)

def is_divisible(number_to_divide, divisor):
    dict_of_args = {
        2: by_2,
        3: by_3,
        5: by_5,
        7: by_7,
        11: by_11,
        13: by_13,
        17: by_17,
        19: by_19,
        }

    # done
    def by_2():
        return str(number_to_divide).endswith(("0", "2", "4", "6", "8"))
    # done
    def by_3():
        sum = 0
        for number in str(number_to_divide):
            sum += int(number)
        if sum % 3 == 0:
            return True
        else:
            return False
        #sum([int(i) for i in str(num)]) % 3 == 0
    # done
    def by_5():
        return str(number_to_divide)[-1] in ['0','5']
    def by_7():
        pass
    def by_11():
        pass
    def by_13():
        pass
    def by_17():
        pass
    def by_19():
        pass
    # If divisibility rule implemented:
    if divisor in dict_of_args.keys():
        dict_of_args[divisor]()
    else:
        return number_to_divide % divisor == 0
    

inspection_list = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

from_idx = 0
parsed_monkey_list: list[Monkey] = []

runner_index = 0
while runner_index < len(file_lines_list):

    if file_lines_list[runner_index] == "":
        parsed_monkey_list.append(analyze_monkey_instance(file_lines_list[from_idx:runner_index]))
        from_idx = runner_index +1

    runner_index += 1

lkkt = 1
for x in parsed_monkey_list:
    lkkt = lkkt * x.divisibility_number 
print(lkkt)

for round in range(10000):
    if round % 100 == 0:
        print(round)
    for monkey_idx in range(len(parsed_monkey_list)):
        items = list(parsed_monkey_list[monkey_idx].items)
        item_idx = 0
        while item_idx < len(items):
            #print(f"Monkey inspects an item with a worry level of {parsed_monkey_list[monkey_idx].items[item_idx]}")

            # inspect item
            inspection_list[monkey_idx] += 1
            op = parsed_monkey_list[monkey_idx].operation_operator
            monkey_object: Monkey = parsed_monkey_list[monkey_idx]
            current_operation_argument = int(monkey_object.operation_argument) if monkey_object.operation_argument != "old" else monkey_object.items[item_idx]
            # do the operation
            monkey_object.items[item_idx] = op(monkey_object.items[item_idx], current_operation_argument)
            #print(f"Worry level is multiplied / increased by {current_operation_argument} to {monkey_object.items[item_idx]}")
            # relief
            #monkey_object.items[item_idx] = int(monkey_object.items[item_idx] / 3)
            monkey_object.items[item_idx] = int(monkey_object.items[item_idx] % lkkt)
            #print(f"Monkey gets bored with item. Worry level is divided by 3 to {parsed_monkey_list[monkey_idx].items[item_idx]}")
            pass

            # test if divisible
            if monkey_object.items[item_idx] % monkey_object.divisibility_number == 0:
                parsed_monkey_list[monkey_object.where_to_if_true].items.append(monkey_object.items[item_idx])
                #del monkey_object.items[item_idx]
            else:
                parsed_monkey_list[monkey_object.where_to_if_false].items.append(monkey_object.items[item_idx])
                #del monkey_object.items[item_idx]
            item_idx += 1
            pass
        parsed_monkey_list[monkey_idx].items = []
        pass
        
inspection_list.sort()
monkey_business = inspection_list[-2] * inspection_list[-1]
print(inspection_list)
print("Solution: ", monkey_business)

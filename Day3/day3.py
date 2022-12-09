import sys


def get_compartment_intersection(rucksack_content: str):
    compartment_size = len(rucksack_content)//2
    first_compartment = set(rucksack_content[:compartment_size])
    second_compartment = set(rucksack_content[compartment_size:])
    return first_compartment & second_compartment


def get_item_priority(item: str):
    item_lower = item.lower()
    score = ord(item_lower) - 96
    if item != item_lower:
        score += 26
    return score


def get_part1_score(f_name):
    total_score = 0
    with open(f_name) as f:
        for line in f:
            duplicated_items = get_compartment_intersection(line.strip())
            for i in duplicated_items:
                total_score += get_item_priority(i)
    print(f'Total priority score: {total_score}')
    return total_score

def get_group_id(rucksack_content1: str,
                 rucksack_content2: str,
                 rucksack_content3: str):
    group_id = list(set(rucksack_content1) & set(rucksack_content2) \
               &set(rucksack_content3))

    assert len(group_id) == 1, 'There can be only 1 group id'

    return group_id[0]


def get_part2_score(f_name):
    total_score = 0
    data = []
    with open(f_name) as f:
        for line in f:
            data.append(line.strip())

    i = 0
    while i < len(data):
        group_id = get_group_id(data[i], data[i+1], data[i+2])
        total_score += get_item_priority(group_id)
        i += 3
    print(f'Total priority score for elf groups: {total_score}')
    return total_score


input_file_name = sys.argv[1]
part_number = int(input("Which part do you want to calculate?\n1/2\n"))
if part_number == 1:
    get_part1_score(input_file_name)
if part_number == 2:
    get_part2_score(input_file_name)

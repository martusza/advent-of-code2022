import sys
import re


def read_file(file_name: str):
    data = []
    with open(input_file_name) as f:
        for line in f:
            data.append(line.rstrip())
    return data


def split_stacks_and_instructions(data):
    break_index = data.index("")
    stacks_of_crates = data[:break_index]
    instructions = data[break_index+1:]
    num_stacks = max([int(x) for x in stacks_of_crates[-1].split(" ") if x])

    data_in_stacks = [[] for x in range(num_stacks)]
    for c in stacks_of_crates[:-1]:
        for i in range(num_stacks):
            crate = c[i*4:(i+1)*4].strip()
            if crate:
                crate = re.sub('\[|]', '', crate)
                data_in_stacks[i].append(crate)

    instructions = [[int(i) for i in x.split(" ") if i.isnumeric()]
                    for x in instructions]

    return data_in_stacks, instructions


def single_move(data_in_stacks: list,
                move: list,
                part: int):
    assert part in (1, 2), 'Only 1 and 2 parts of task are considered'

    qty = move[0]
    start = move[1]-1
    stop = move[2]-1

    crate_to_move = data_in_stacks[start][:qty]
    if part == 1:
        for c in crate_to_move:
            data_in_stacks[stop] = [c] + data_in_stacks[stop]
    else:
        data_in_stacks[stop] = crate_to_move + data_in_stacks[stop]
    del data_in_stacks[start][:qty]


def get_top_items(data_in_stacks):
    response = ""
    for s in data_in_stacks:
        response += s[0]
    return response


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    part_number = int(input("Which part do you want to calculate?\n1/2\n"))
    data = read_file(input_file_name)
    data_in_stacks, instructions = split_stacks_and_instructions(data)

    for move in instructions:
        single_move(data_in_stacks,
                    move,
                    part_number)

    print(get_top_items(data_in_stacks))
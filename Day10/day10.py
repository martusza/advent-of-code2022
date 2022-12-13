import sys

instruction_cycles = {
    'noop': 1,
    'addx': 2
}

signals = [20, 60, 100, 140, 180, 220]


def read_file(file_name: str) -> list:
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(line.rstrip().split(" "))
    return data


def calc_part1(input_data: list) -> int:
    # Part 1 solution
    X_part1 = []
    current_x = 1
    for i in input_data:
        current_instruction = i[0]
        for j in range(instruction_cycles[current_instruction]):
            X_part1.append(current_x)
        if current_instruction == "addx":
            current_x += int(i[1])

    selected_signals = [X_part1[i-1]*i for i in signals]
    return sum(selected_signals)


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    instructions_data = read_file(input_file_name)

    part1_solution = calc_part1(instructions_data)
    print(f"Sum selected signals: {part1_solution}")

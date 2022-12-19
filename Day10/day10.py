import sys

instruction_cycles = {
    'noop': 1,
    'addx': 2
}


def read_file(file_name: str) -> list:
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(line.rstrip().split(" "))
    return data


def calc_x(input_data: list) -> list:
    X_vector = []
    current_x = 1
    for i in input_data:
        current_instruction = i[0]
        for j in range(instruction_cycles[current_instruction]):
            X_vector.append(current_x)
        if current_instruction == "addx":
            current_x += int(i[1])
    return X_vector


def calc_part1(X_input: list) -> int:
    # Part 1 solution
    signals = [20, 60, 100, 140, 180, 220]

    try:
        selected_signals = [X_input[i-1]*i for i in signals]
        return sum(selected_signals)
    except IndexError:
        print('Not enough observations')


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    instructions_data = read_file(input_file_name)
    X = calc_x(instructions_data)

    # Part 1
    part1_solution = calc_part1(X)
    print(f"Sum selected signals: {part1_solution}")

    # Part 2
    CRT = ""
    CRT_position = 0
    cycles = []
    for x in X:
        if x-1 <= CRT_position <= x+1:
            CRT += "#"
        else:
            CRT += "."
        CRT_position += 1
        if CRT_position >= 40:
            CRT_position = 0
            cycles.append(CRT)
            CRT=""

    print("\n".join(cycles))


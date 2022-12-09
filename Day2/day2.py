import sys


# Part 1
game_scenarios_part1 = {
    'A X': 1+3,
    'A Y': 2+6,
    'A Z': 3,
    'B X': 1,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 1+6,
    'C Y': 2,
    'C Z': 3+3
}

# Part 2
game_scenarios_part2 = {
    'A X': 3,
    'A Y': 1+3,
    'A Z': 2+6,
    'B X': 1,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 2,
    'C Y': 3+3,
    'C Z': 1+6
}

game_scenarios = {1: game_scenarios_part1,
                  2: game_scenarios_part2}

part_number = int(input("Which part do you want to calculate?\n1/2\n"))
while part_number not in (1,2):
    print("Incorrect part number. Only 1 and 2 are valid.")
    part_number = int(input("Which part do you want to calculate?\n1/2\n"))


selected_game_scenario = game_scenarios.get(part_number)
input_file_name = sys.argv[1]
total_score = 0
with open(input_file_name) as f:
    for line in f:
        line = line.strip()
        total_score += selected_game_scenario.get(line)

print(total_score)

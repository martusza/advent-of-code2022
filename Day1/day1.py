import sys


input_file_name = sys.argv[1]
elves_calories = []
elf_calories = 0
with open(input_file_name) as f:
    for line in f:
        line = line.strip()
        if line:
            elf_calories += int(line)
        else:
            elves_calories.append(elf_calories)
            elf_calories = 0

elves_calories.append(elf_calories)
elves_calories.sort(reverse=True)
print(f"Maximum calories : {max(elves_calories)}")
print(f"Sum calories carried by top 3 elves: {sum(elves_calories[:3])}")

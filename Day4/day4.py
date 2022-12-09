import sys


def check_if_contain(sections1: list,
                     sections2: list):
    assert len(sections1) == len(sections2) == 2, 'list must contain 2 elements'

    start1 = int(sections1[0])
    end1 = int(sections1[1])
    start2 = int(sections2[0])
    end2 = int(sections2[1])
    if start1 <= start2 and end1 >= end2:
        return 1
    elif start2 <= start1 and end2 >= end1:
        return 1
    return 0


def check_overlap(sections1: list,
                  sections2: list):
    assert len(sections1) == len(sections2) == 2, 'list must contain 2 elements'

    start1 = int(sections1[0])
    end1 = int(sections1[1])
    start2 = int(sections2[0])
    end2 = int(sections2[1])

    if end2 >= start1 >= start2 or end2 >= end1 >= start2:
        return 1
    elif end1 >= start2 >= start1 or end1 >= end2 >= start1:
        return 1
    else:
        return 0


input_file_name = sys.argv[1]
fully_containing_pairs = 0
overlap_pairs = 0
with open(input_file_name) as f:
    for line in f:
        elves_pair = line.strip().split(',')
        elves_pair = [x.split("-") for x in elves_pair]
        if elves_pair:
            fully_containing_pairs += check_if_contain(elves_pair[0],
                                                       elves_pair[1])
            overlap_pairs += check_overlap(elves_pair[0],
                                           elves_pair[1])

print(f"There are {fully_containing_pairs} pairs where one contains other")
print(overlap_pairs)

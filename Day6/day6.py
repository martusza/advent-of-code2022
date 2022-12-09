import sys


def read_file_to_string(file_name: str) -> str:
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(line.rstrip())
    return "".join(data)


def find_marker_char(datastream: str,
                     n: int):
    for i in range(len(datastream)-n):
        n_unique_chars = len(set(datastream[i:(n+i)]))
        if n_unique_chars == n:
            return i+n


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    data = read_file_to_string(input_file_name)
    marker = find_marker_char(data, 14)
    print(marker)

import sys


def read_file(file_name: str) -> list:
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(list(line.rstrip()))
    return data


def generate_grid(input_data):
    rows = list([list(map(int, x)) for x in [list(tree) for tree in input_data]])
    cols = list(list(zip(*rows)))
    return rows, cols


def check_visibility(input_data: list,
                     axis: int,
                     v_grid: list):
    assert axis in (0,1), "Axis must be 0 or 1"
    for row_number, row in enumerate(input_data):
        for i in range(len(row)):
            if i == 0 or i == len(row)-1:
                if axis == 0:
                    v_grid[row_number][i] = 1
                else:
                    v_grid[i][row_number] = 1
                continue
            current_tree = row[i]
            max_right_tree = max(row[-len(row)+i+1:])
            max_left_tree = max(row[:i])
            if current_tree > max_right_tree or current_tree>max_left_tree:
                if axis == 0:
                    v_grid[row_number][i] = 1
                else:
                    v_grid[i][row_number] = 1


def calc_scenic_score(input_data: list,
                      axis: int,
                      ):
    assert axis in (0,1), "Axis must be 0 or 1"

    scores = {}
    for row_number, row in enumerate(input_data):
        for i in range(len(row)):
            current_tree = row[i]
            score_right = 0
            score_left = 0
            for j in range(i+1, len(row)):
                next_tree_right = row[j]
                score_right += 1
                if next_tree_right >= current_tree:
                    break

            for j in range(i, 0, -1):
                next_tree_left = row[j-1]
                score_left += 1
                if next_tree_left >= current_tree:
                    break

            if axis == 0:
                scores[f'{row_number}_{i}'] = score_left*score_right
            else:
                scores[f'{i}_{row_number}'] = score_left*score_right

    return scores


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    data = read_file(input_file_name)
    num_rows = len(data)
    num_cols = len(data[0])

    tree_rows, tree_cols = generate_grid(data)

    visibility_grid = [[0 for i in range(num_cols)] for j in range(num_rows)]
    check_visibility(tree_rows, 0, visibility_grid)
    check_visibility(tree_cols, 1, visibility_grid)

    total_sum = sum([sum(x) for x in visibility_grid])
    print(f"Number of visible trees: {total_sum}")

    horizontal_visibility = calc_scenic_score(tree_rows, 0)
    vertical_visibility = calc_scenic_score(tree_cols, 1)

    summary_score = {}
    for k in horizontal_visibility:
        summary_score[k] = horizontal_visibility[k] * vertical_visibility[k]

    print(max(summary_score.values()))




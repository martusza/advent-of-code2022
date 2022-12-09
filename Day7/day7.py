import sys


def read_file(file_name: str) -> list:
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(line.rstrip())
    return data


def change_dir(command: str,
               current_dir: str):
    assert command.startswith("$ cd"), 'Command must change dir'

    if command == "$ cd /":
        return "/"
    elif command == "$ cd ..":
        new_dir = current_dir.split("/")
        if len(new_dir) > 2:
            new_dir = new_dir[:-1]
            return "/".join(new_dir)
        else:
            return "/"
    else:
        command_split = command.split(" ")
        if current_dir == "/":
            new_dir = f"/{command_split[-1]}"
        else:
            new_dir = f"{current_dir}/{command_split[-1]}"
        return new_dir


def calc_dir_file_size(ls_output):
    dir_content_summary = {"dirs": [],
                           "size": 0}
    for i in ls_output:
        info_split = i.split(" ")
        if info_split[0] == "dir":
            dir_content_summary["dirs"].append(info_split[1])
        elif info_split[0].isnumeric():
            dir_content_summary["size"] += int(info_split[0])
    return dir_content_summary


def get_dir_total_size(dir_to_check):
    total_dir_size = file_system[dir_to_check]['size']
    for d in file_system[dir_to_check]['dirs']:
        if dir_to_check != "/":
            global_dir = f"{dir_to_check}/{d}"
        else:
            global_dir = f"/{d}"
        total_dir_size += get_dir_total_size(global_dir)
    return total_dir_size


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    total_disk_space = 70000000
    required_size = 30000000
    data = read_file(input_file_name)

    current_dir = "/"
    all_dirs = []
    file_system = {}
    for i, line in enumerate(data):
        if line.startswith("$ cd"):
            current_dir = change_dir(line, current_dir)
            all_dirs.append(current_dir)
        elif line.startswith("$ ls"):
            if "$ ls" in data[i+1:]:
                next_ls_index = data[i+1:].index("$ ls")
                contents = data[i+1:next_ls_index+i+1]
            else:
                contents = data[i+1:]
            file_system[current_dir] = calc_dir_file_size(contents)

    file_system_size = {
        k: get_dir_total_size(k)
        for k in file_system
    }

    final_sum = 0

    # Part 1
    for v in file_system_size.values():
        if v <= 100000:
            final_sum += v
    print(f"Sum required in part 1: {final_sum}")

    # Part 2
    disk_space_left = total_disk_space - file_system_size['/']

    dir_options = []
    for v in file_system_size.values():
        if v + disk_space_left > required_size:
            dir_options.append(v)
    print(f"Minimum dir size to delete {min(dir_options)}")
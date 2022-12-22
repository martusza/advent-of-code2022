import sys


def read_file(file_name: str) -> list:
    data = []
    with open(file_name) as f:
        for line in f:
            data.append(line.rstrip())
    return data


class Monkey:
    modulo = 1

    def __init__(self,
                 monkey_data):
        self.monkey_data = monkey_data
        self.monkey_id = monkey_data[0].replace(":", "")
        self.starting_items = [int(x) for x in monkey_data[1].split(":")[-1].split(",")]
        self.operation = monkey_data[2].split("=")[-1]
        self.inspected_items = 0
        self.test_num = int(monkey_data[3].split(" ")[-1])
        Monkey.modulo *= self.test_num

    def __int__(self):
        return self.inspected_items

    def calc_operation(self, old):
        new = eval(self.operation) % Monkey.modulo
        self.inspected_items += 1
        return new

    def add_item(self,
                 value):
        self.starting_items.append(value)

    def perform_single_test(self,
                            value):
        test_lines = self.monkey_data[3:6]
        new_value = int(self.calc_operation(value))
        if not new_value % self.test_num:
            return int(test_lines[1].split(" ")[-1]), new_value
        else:
            return int(test_lines[2].split(" ")[-1]), new_value


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    all_monkey_data = read_file(input_file_name)

    num_monkeys = 8
    num_rounds = 10000
    monkeys = []
    for i in range(num_monkeys):
        monkey = Monkey(all_monkey_data[i*7:(i+1)*7])
        monkeys.append(monkey)

    for r in range(num_rounds):
        for m in monkeys:
            for i in m.starting_items:
                monkey_to_throw, item_number = m.perform_single_test(i)
                monkeys[monkey_to_throw].add_item(item_number)
            m.starting_items = []

    sorted_monkeys = sorted([int(x) for x in monkeys], reverse=True)

    print(f"level of monkey business after {num_rounds} rounds:\
            {sorted_monkeys[0]*sorted_monkeys[1]}")
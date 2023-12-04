from ast import Index


def yield_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line


def _calc_number_of_matches(game):
    return len(set.intersection(*map(lambda x: set(x.split()), game.strip().split(":")[1].split("|"))))


def solve_part1(file_path):
    solution = 0
    for line in yield_lines(file_path):
        number_of_matches = _calc_number_of_matches(line)
        if number_of_matches:
            solution += 2 ** (number_of_matches - 1)
    return solution


def solve_part2(file_path):
    solution = 0
    number_of_copies = list()
    for line in yield_lines(file_path):
        number_of_matches = _calc_number_of_matches(line)
        scratchcards = (number_of_copies.pop(0) + 1) if number_of_copies else 1
        solution += scratchcards
        for i in range(number_of_matches):
            try:
                number_of_copies[i] += scratchcards
            except IndexError:
                number_of_copies.append(scratchcards)
    return solution


assert solve_part1("example.txt") == 13
assert solve_part1("input.txt") == 17782
assert solve_part2("example.txt") == 30
assert solve_part2("input.txt") == 8477787
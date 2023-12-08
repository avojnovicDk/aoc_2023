from math import ceil, floor, sqrt


def yield_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line


def _calc_number_of_better_options(time, distance):
    min_hold = floor((time - sqrt(time*time - 4*distance))/2 + 1)
    max_hold = ceil((time + sqrt(time*time - 4*distance))/2 - 1)
    return max_hold - min_hold + 1


def solve_part1(file_path):
    races = zip(*(list(map(int, line.split(":")[1].split())) for line in yield_lines(file_path)))
    solution = 1
    for time, distance in races:
        solution *= _calc_number_of_better_options(time, distance)
    return solution


def solve_part2(file_path):
    time, distance = list(int(line.strip().split(":")[1].replace(" ", "")) for line in yield_lines(file_path))
    return _calc_number_of_better_options(time, distance)


assert solve_part1("example.txt") == 288
assert solve_part1("input.txt") == 252000

assert solve_part2("example.txt") == 71503
assert solve_part2("input.txt") == 36992486

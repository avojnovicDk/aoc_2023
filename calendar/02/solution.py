import re
from collections import namedtuple
from functools import reduce
from typing import Generator


QUANTITY_PER_COLOR = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


Cubes = namedtuple("Cubes", "color quantity")


def yield_lines(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line


def _yield_cubes(game:str) -> Generator[Cubes, None, None]:
    for subset in game.split(";"):
        for cube in subset.split(","):
            quantity, color = cube.split()
            yield Cubes(color, int(quantity))


def _validate_game(game: str) -> bool:
    for cubes in _yield_cubes(game):
        if QUANTITY_PER_COLOR[cubes.color] < cubes.quantity:
            return False
    return True


def _calc_power_of_min_quantites(game: str) -> int:
    min_quantities = dict()
    for cubes in _yield_cubes(game):
        if cubes.color not in min_quantities or min_quantities[cubes.color] < cubes.quantity:
            min_quantities[cubes.color] = cubes.quantity
    return reduce((lambda x, y: x * y), min_quantities.values())
    

def solve_part1(file_path: str) -> int:
    solution = 0
    for line in yield_lines(file_path):
        game_number, game = line.split(":")
        if _validate_game(game):
            solution += int(game_number.split()[1])
    return solution


def solve_part1_regex(file_path: str) -> int:
    pattern = "Game |\:|;|\,|" + "|".join(f" {i + 1} {c}" for c, q in QUANTITY_PER_COLOR.items() for i in range(q))

    solution = 0
    for line in yield_lines(file_path):
        try:
            solution += int(re.sub(pattern, "", line))
        except ValueError:
            pass
    return solution


def solve_part2(file_path: str) -> int:
    solution = 0
    for line in yield_lines(file_path):
        solution += _calc_power_of_min_quantites(line.split(":")[1])
    return solution


assert solve_part1("example.txt") == 8
assert solve_part1("input.txt") == 3059
assert solve_part2("example.txt") == 2286
assert solve_part2("input.txt") == 65371
assert solve_part1_regex("example.txt") == 8
assert solve_part1_regex("input.txt") == 3059

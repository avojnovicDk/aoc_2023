from typing import Dict, Generator, Iterator, Optional


NUMBERS = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

NUMBER_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}



def yield_lines(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line


class NumberFinder:
    def __init__(self, valid_numbers: Dict[str, int], from_start: bool = True):
        self.valid_numbers = valid_numbers
        self.from_start = from_start

    def _has_number_string(self, line: str, number_string: str) -> bool:
        if self.from_start:
            return line.startswith(number_string)
        else:
            return line.endswith(number_string)

    def __call__(self, line: str) -> Optional[int]:
        while line:
            for number_string, number in self.valid_numbers.items():
                if self._has_number_string(line, number_string):
                    return number
            line = line[1:] if self.from_start else line[:-1]


def solve(valid_numbers, lines: Iterator[str]) -> int:
    start_finder = NumberFinder(valid_numbers)
    end_finder = NumberFinder(valid_numbers, False)
    
    solution = 0

    for line in lines:
        solution += start_finder(line) * 10 + end_finder(line)

    return solution


def solve_part_1(file_path: str) -> int:
    return solve(NUMBERS, yield_lines(file_path))


def solve_part_2(file_path: str) -> int:
    return solve({**NUMBERS, **NUMBER_WORDS}, yield_lines(file_path))


assert solve_part_1("example1.txt") == 142
assert solve_part_1("input.txt") == 54953

assert solve_part_2("example2.txt") == 281
assert solve_part_2("input.txt") == 53868

import re


def yield_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line


class LineFrameSolver:
    def __init__(self, fn_solve):
        self.fn_solve = fn_solve

    def __call__(self, file_path):
        solution = 0
        prev_line, curr_line, next_line = None, None, None
        for line in yield_lines(file_path):
            if curr_line is None:
                curr_line = line
                continue

            next_line = line

            for subsolution in self.fn_solve(prev_line, curr_line, next_line):
                solution += subsolution

            prev_line = curr_line
            curr_line = next_line
        
        next_line = None

        for subsolution in self.fn_solve(prev_line, curr_line, next_line):
            solution += subsolution

        return solution


def _yield_frame_chars(prev_line, curr_line, next_line, start, length):
    left_pos = max(start - 1, 0)
    right_pos = min(start + length, len(curr_line))
    if prev_line:
        yield from prev_line[left_pos: right_pos + 1]
    yield(curr_line[left_pos])
    yield(curr_line[right_pos])
    if next_line:
        yield from next_line[left_pos: right_pos + 1]


def _is_symbol(c):
    return c  not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '\n']


def _is_part_number_position(prev_line, curr_line, next_line, start, length):
    for c in _yield_frame_chars(prev_line, curr_line, next_line, start, length):
        if _is_symbol(c):
            return True
    return False


def _yield_part_numbers(prev_line, curr_line, next_line):
    for match in re.finditer("\d{1,}", curr_line):
        pos, num = match.start(), match.group()
        if _is_part_number_position(prev_line, curr_line, next_line, pos, len(num)):
            yield int(num)


def solve_pt1(file_path):
    return LineFrameSolver(_yield_part_numbers)(file_path)


def _get_regex_match(pattern, s):
    match = re.match(pattern, s)
    if match:
        return match.group(1)


def _yield_numbers_around(line, pos):
    left_num = _get_regex_match(r".*?([0-9]+)$", line[:pos]) or ''
    right_num = _get_regex_match(r"^([0-9]+)", line[min(pos + 1, len(line)):]) or ''

    if line[pos].isnumeric():
        yield int(left_num + line[pos] + right_num)
    else:
        if left_num:
            yield(int(left_num))
        if right_num:
            yield(int(right_num))


def _calc_gear_ratio(prev_line, curr_line, next_line, pos):
    part_number_1, part_number_2 = None, None
    for line in (prev_line, curr_line, next_line):
        for part_number in _yield_numbers_around(line, pos):
            if part_number_1 is None:
                part_number_1 = part_number
            elif part_number_2 is None:
                part_number_2 = part_number
            else:
                return
    
    try:
        return part_number_1 * part_number_2
    except TypeError:
        return


def _yield_gear_ratios(prev_line, curr_line, next_line):
    for match in re.finditer("\*", curr_line):
        gear_ratio = _calc_gear_ratio(prev_line, curr_line, next_line, match.start())
        if gear_ratio:
            yield gear_ratio
    

def solve_pt2(file_path):
    return LineFrameSolver(_yield_gear_ratios)(file_path)


assert solve_pt1("example.txt") == 4361
assert solve_pt1("input.txt") == 535351
assert solve_pt2("example.txt") == 467835
assert solve_pt2("input.txt") == 87287096

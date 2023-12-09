from functools import reduce


def _yield_new_history(history):
    prev_el = None
    for curr_el in history:
        if prev_el is None:
            prev_el = curr_el
            continue
        yield curr_el - prev_el
        prev_el = curr_el


def _calc_extrapolated_value(history):
    solution = 0
    while any(history):
        solution += history[-1]
        history = list(_yield_new_history(history))

    return solution


def _calc_extrapolated_value(history, backwards=False):
    new_values = list()
    while any(history):
        new_values.append(history[0 if backwards else -1])
        history = list(_yield_new_history(history))
    
    return reduce(lambda x, y: y + (-1  if backwards else 1) * x, reversed(new_values))
    

def solve(file_path, backwards=False):
    solution = 0
    with open(file_path, 'r') as f:
        for line in f:
            solution += _calc_extrapolated_value(list(map(int, line.split())), backwards=backwards)
    return solution


assert solve("example.txt") == 114
assert solve("input.txt") == 2005352194

assert solve("example.txt", backwards=True) == 2
assert solve("input.txt", backwards=True) == 1077

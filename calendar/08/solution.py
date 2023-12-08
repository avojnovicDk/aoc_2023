from functools import reduce
from itertools import cycle
from math import sqrt


def _yield_prime_factors(n):  
    while n % 2 == 0: 
        yield 2
        n = int(n / 2)
          
    for i in range(3, int(sqrt(n)) + 1, 2): 
        while n % i== 0: 
            yield i
            n = int(n / i) 
               
    if n > 2: 
        yield n 


def solve(file_path, source_end, dest_end):
    lr_instruction = None
    network = dict()
    curr_els = list()
    with open(file_path, 'r') as f:
        lr_instruction = f.readline().strip()
        f.readline()
        for line in f:
            source, dests = line.split("=")
            dests = tuple(map(lambda x: x.strip(), dests.replace("(", "").replace(")", "").split(",")))
            source = source.strip()
            if source.endswith(source_end):
                curr_els.append(source)
            network[source] = dests

    step_counters = list()
    for curr_el in curr_els:
        step_counters.append(0)
        for i in cycle(lr_instruction):
            curr_el = network[curr_el][0 if i == "L" else 1]
            step_counters[-1] += 1
    
            if curr_el.endswith(dest_end):
                break
            
    solution = list()
    for c in step_counters:
        for s in solution:
            if c % s == 0:
                c = int(c / s)
        solution += list(_yield_prime_factors(c))
    
    solution = reduce(lambda x, y: x * y, solution)
    return solution


assert solve("example.txt", "AAA", "ZZZ") == 6
assert solve("input.txt", "AAA", "ZZZ") == 12361

assert solve("example2.txt", "A", "Z") == 6
assert solve("input2.txt", "A", "Z") == 18215611419223

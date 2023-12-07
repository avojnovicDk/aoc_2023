def yield_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line


def solve_part1(file_path):
    seeds = dict()
    
    for line in yield_lines(file_path):
        if not seeds:
            seeds = {s: None for s in map(int, line.split(":")[1].split())}
            continue

        try:
            dest_start, source_start, range_len = map(int, line.split())
        except ValueError:
            seeds = {a if b is None else b: None for a, b in seeds.items()}
            continue
        
        for a, b in seeds.items():
            if b is not None:
                continue

            if source_start <= a <= source_start + range_len:
                seeds[a] = a + dest_start - source_start
        
    seeds = {a if b is None else b: None for a, b in seeds.items()}
    return min(seeds.keys())


def solve_part2(file_path):
    seeds = dict()
    
    for line in yield_lines(file_path):
        if not seeds:
            start = None
            for s in map(int, line.split(":")[1].split()):
                if start is None:
                    start = s
                else:
                    seeds[(start, start + s - 1)] = None
                    start = None
            continue

        try:
            dest_start, source_start, range_len = map(int, line.split())
            source_end = source_start + range_len - 1
            difference = dest_start - source_start
        except ValueError:
            seeds = {a if b is None else b: None for a, b in seeds.items()}
            continue
        
        for start, end in list(seeds.keys()):
            if seeds[(start, end)] is not None:
                continue

            if source_start <= end and source_end >= start:
                overlap = (max(start, source_start), min(end, source_end)) 
                seeds[overlap] = tuple(map(lambda x: x + difference, overlap))

                if end > source_end:
                    seeds[(source_end + 1, end)] = None
                if start < source_start:
                    seeds[(start, source_start - 1)] = None
                if seeds[(start, end)] is None:
                    del seeds[(start, end)]
        
    seeds = {a if b is None else b: None for a, b in seeds.items()}
    return min(seeds.keys())[0]
        
assert solve_part1("example.txt") == 35
assert solve_part1("input.txt") == 309796150

assert solve_part2("example.txt") == 46
assert solve_part2("input.txt") == 50716416
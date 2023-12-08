from collections import Counter, defaultdict


def yield_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line


def _calc_type(hand):
    joker_counter = Counter(hand)["1"]
    card_counter = Counter(hand.replace("1", ""))
    if len(card_counter) < 2:
        return 6

    most_common_1st, most_common_2nd = map(lambda x: x[1], card_counter.most_common(2))
    if most_common_1st + joker_counter == 5:
        return 6
    
    if most_common_1st + joker_counter == 4:
        return 5
    
    if most_common_1st == 3:
        if most_common_2nd + joker_counter >= 2:
            return 4
        else:
            return 3
    
    if most_common_1st + joker_counter == 3:
        if most_common_2nd == 2:
            return 4
        else:
            return 3

    if most_common_1st == 2:   
        if most_common_2nd + joker_counter >= 2:
            return 2
        else:
            return 1

    if most_common_1st + joker_counter == 2:   
        if most_common_2nd == 2:
            return 2
        else:
            return 1
    return 0


def solve(file_path, with_jack=False):
    hands = dict()
    hands_per_type = defaultdict(list)
    for line in yield_lines(file_path):
        hand, bid = line.split()
        hand = hand.replace("T", "B").replace("J", "C").replace("Q", "D").replace("K", "E").replace("A", "F")
        if with_jack:
            hand = hand.replace("C", "1")
        hands[hand] = int(bid)
        hands_per_type[_calc_type(hand)].append(hand)
    rank = len(hands)
    solution = 0
    for hand_type in range(6, -1, -1):
        for hand in sorted(hands_per_type[hand_type], reverse=True):
            solution += rank * hands[hand]
            rank -= 1
    return solution


assert solve("example.txt") == 6440
assert solve("input.txt") == 251136060

assert solve("example.txt", with_jack=True) == 5905
assert solve("input.txt", with_jack=True) == 249400220

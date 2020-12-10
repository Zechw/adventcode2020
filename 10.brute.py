parse_nums = lambda inp: [int(x) for x in inp.split("\n")]

def brute_force(input_string):
    adps = set(parse_nums(input_string))
    adps.add(0)
    return bf_loop(0, max(adps), adps)

def bf_loop(current_joltage, target_joltage, adps):
    if current_joltage not in adps:
        return 0
    elif current_joltage == target_joltage:
        return 1
    else:
        return (
            bf_loop(current_joltage + 1, target_joltage, adps)
            + bf_loop(current_joltage + 2, target_joltage, adps)
            + bf_loop(current_joltage + 3, target_joltage, adps)
        )

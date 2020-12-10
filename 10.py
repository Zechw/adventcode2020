parse_nums = lambda inp: [int(x) for x in inp.split("\n")]


def count_jolts(input_string):
    # !! not including last jump to device
    adps = sorted(parse_nums(input_string))
    current_jolt = 0
    diff = [0] * 3
    for adp in adps:
        diff[adp - current_jolt - 1] += 1
        current_jolt = adp
    return diff

from collections import defaultdict

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

def count_perms(input_string):
    adps = [0] + sorted(parse_nums(input_string))
    c = defaultdict(int) # known counts dicitonary
    c[max(adps) + 3] = 1 # init the device
    while adps:
        adp = adps.pop()
        perms = c[adp+1] + c[adp+2] + c[adp+3]
        c[adp] = perms
    return c[0]

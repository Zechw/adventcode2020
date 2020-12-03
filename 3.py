
def count_trees(map, run=3, rise=1):
    i = 0
    count = 0
    for row in map[::rise]:
        if row[i] == "#":
            count += 1
        i = (i+run) % 31
    return count


def mult_slopes(map_string):
    map = map_string.split("\n")
    return (
        count_trees(map, 1, 1),
        count_trees(map, 3, 1),
        count_trees(map, 5, 1),
        count_trees(map, 7, 1),
        count_trees(map, 1, 2)
    )

def one_pass(map, rise_run_pairs):
    counts = [0] * len(rise_run_pairs)
    for i, row in enumerate(map):
        for j, (rise, run) in enumerate(rise_run_pairs):
            if i % rise == 0:
                if row[int(i * run / rise) % 31] == "#":
                    counts[j] += 1
    return counts

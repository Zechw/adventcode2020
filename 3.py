
def count_trees(map, rise=1, run=3):
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
        count_trees(map, 1, 3),
        count_trees(map, 1, 5),
        count_trees(map, 1, 7),
        count_trees(map, 2, 1)
    )

def variable_mult_slopes(map_string, rise_run_pairs):
    map = map_string.split("\n")
    results = []
    for rise, run in rise_run_pairs:
        results.append(count_trees(map, rise, run))
    return results



def one_pass(map, rise_run_pairs):
    counts = [0] * len(rise_run_pairs)
    for i, row in enumerate(map):
        for j, (rise, run) in enumerate(rise_run_pairs):
            if i % rise == 0:
                if row[(i // rise * run) % 31] == "#":
                    counts[j] += 1
    return counts

def ops(map_string):
    map = map_string.split("\n")
    return one_pass(map, [(1, 1),(1, 3),(1, 5),(1, 7),(2, 1)])


def variable_ops(map_string, rise_run_pairs):
    map = map_string.split("\n")
    return one_pass(map, rise_run_pairs)

from copy import deepcopy

NEIGHBOR_MAP = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def find_stable(inp):
    ferry = list(map(list, inp.split("\n")))
    size = (len(ferry), len(ferry[0]))
    while True:
        next_ferry = deepcopy(ferry)

        for i in range(size[0]):
            for j in range(size[1]):
                seat = ferry[i][j]
                n_occ = 0
                for direction in NEIGHBOR_MAP:
                    n = get_first_seat(direction, i, j, ferry, size)
                    if n == "#":
                        n_occ += 1

                if seat == "L" and n_occ == 0:
                    next_ferry[i][j] = "#"
                elif seat == "#" and n_occ > 4:
                    next_ferry[i][j] = "L"

        if ferry == next_ferry:
            return sum(map(lambda x: x.count("#"), ferry))
        ferry = next_ferry


def get_first_seat(direction, i, j, ferry, size):
    ii = i + direction[0]
    jj = j + direction[1]

    if ii < 0 or jj < 0 or ii == size[0] or jj == size[1]:
        return False

    seat = ferry[ii][jj]
    if seat == ".":
        return get_first_seat(direction, ii, jj, ferry, size)
    else:
        return seat

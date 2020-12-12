import numpy as np

directions = ['N', 'E', 'S', 'W']
d_map = {
    "N": np.array([1, 0]),
    "E": np.array([0, 1]),
    "S": np.array([-1, 0]),
    "W": np.array([0, -1]),
}
cw = lambda c: np.array([-c[1], c[0]])
ccw = lambda c: np.array([c[1], -c[0]])


# part 1
def follow_directions(inp):
    dirs = inp.split("\n")
    position = np.array([0, 0])
    direction = "E"
    for d in dirs:
        actn = d[0]
        val = int(d[1:])
        if actn in d_map:
            position = position + (d_map[actn] * val)
        elif actn == "F":
            position = position + (d_map[direction] * val)
        else:
            rot_dir = 1 if actn == "R" else -1
            roll = (directions.index(direction) + (rot_dir * (val // 90))) % 4
            direction = directions[roll]
    return position


# part 2
def follow_waypoint(inp):
    dirs = inp.split("\n")
    position = np.array([0, 0])
    waypoint = np.array([1, 10])
    for d in dirs:
        actn = d[0]
        val = int(d[1:])
        if actn in d_map:
            waypoint = waypoint + (d_map[actn] * val)
        elif actn == "F":
            position += waypoint * val
        else:
            f = cw if actn == "R" else ccw
            for _ in range(0, val // 90):
                waypoint = f(waypoint)
    return position

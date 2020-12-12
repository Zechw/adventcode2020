import numpy as np

directions = ['N', 'E', 'S', 'W']
d_map = {
    "N": np.array([1, 0]),
    "E": np.array([0, 1]),
    "S": np.array([-1, 0]),
    "W": np.array([0, -1]),
}




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

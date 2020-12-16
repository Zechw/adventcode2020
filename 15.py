
def recite_to(seq, n):
    last_seen_dict = {}
    i = 0
    next_num = seq.pop()
    # load seq (saving next_num for first cycle)
    for s in seq:
        last_seen_dict[s] = i
        i += 1
    while i < n - 1: # human friendly offset
        try:
            v = i - last_seen_dict[next_num]
        except:
            v = 0
        last_seen_dict[next_num] = i
        next_num = v
        i += 1
    return next_num

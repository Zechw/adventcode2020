

def dock(inp):
    instructions = inp.split("\n")
    mem = {}
    for ins in instructions:
        cmd, val = ins.split(" = ", 1)
        if cmd == "mask":
            mask = val
        else: #mem
            mem_loc = cmd.replace("mem[", "").replace("]", "")
            mem[mem_loc] = mask_val(mask, val)
    return sum(mem.values())


def mask_val(mask, val):
    binary = list(format(int(val), '036b'))
    for i, x in enumerate(mask):
        if x == 'X':
            continue
        else:
            binary[i] = x
    return int(''.join(binary), 2)

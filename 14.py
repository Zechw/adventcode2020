

def dock_v1(inp):
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



def dock_v2(inp):
    instructions = inp.split("\n")
    mem = {}
    for ins in instructions:
        cmd, val = ins.split(" = ", 1)
        if cmd == "mask":
            mask = val
        else:
            mem_loc = cmd.replace("mem[", "").replace("]", "")
            masked_mem_loc = mask_mem_loc(mask, mem_loc)
            recursively_write_masked_mem(mem, masked_mem_loc, int(val))
    return sum(mem.values())

def mask_mem_loc(mask, mem_loc):
    binary = list(format(int(mem_loc), '036b'))
    for i, x in enumerate(mask):
        if x != "0":
            binary[i] = x
    return ''.join(binary)


def recursively_write_masked_mem(mem, masked_mem_loc, val):
    fork = masked_mem_loc.find('X')
    if fork == -1:
        mem[masked_mem_loc] = val
    else:
        recursively_write_masked_mem(mem, masked_mem_loc.replace('X', '0', 1), val)
        recursively_write_masked_mem(mem, masked_mem_loc.replace('X', '1', 1), val)

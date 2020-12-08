from collections import namedtuple

ops = {
    'nop': lambda i, a, _: (i+1, a),
    'acc': lambda i, a, val: (i+1, a+val),
    'jmp': lambda i, a, val: (i+val, a)
}
Instruction = namedtuple('Instruction', 'op val')
parse_instructions = lambda txt:  [Instruction(ops[op], int(val)) for op, val in [x.split(" ") for x in txt.split("\n")]]
step = lambda i, a, ins: ins.op(i, a, ins.val)
swap = lambda ins: Instruction(ops['jmp'] if ins.op is ops['nop'] else ops['nop'], ins.val)

# part 1
def find_loop(input_text):
    instructions = parse_instructions(input_text)
    return run_till_loop(0, 0, set(), instructions)

def run_till_loop(i, a, ran_i, instructions):
    while i not in ran_i:
        ran_i.add(i)
        i, a = step(i, a, instructions[i])
    return (i, a)


# part 2
def fix_loop(input_text):
    instructions = parse_instructions(input_text)
    i, a, ran_i = 0, 0, set()
    edited = False
    while i < len(instructions):
        ins = instructions[i]
        has_been_ran = i in ran_i
        ran_i.add(i)
        if has_been_ran:
            # we looped! rewind and retry without edit
            # print('loop', i, a, ran_i)
            # input()
            i, a, ran_i = branch_point
            edited = False
        else:
            if not edited and ins.op is not ops['acc']:
                # print('branch', i, a, ran_i)
                # input()
                # save our spot, but try to fix this spot and continue
                branch_point = (i, a, ran_i.copy())
                ins = swap(ins)
                edited = True
        i, a = step(i, a, ins)
    return (i, a)

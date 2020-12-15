
# part 1
def find_bus(inp):
    depart, bus_inp = inp.split("\n", 1)
    depart = int(depart)
    buses = [int(x) for x in bus_inp.split(",") if x != "x"]
    best_bus = None
    wait = float("inf")
    for bus in buses:
        w = bus - (depart % bus)
        if w < wait:
            best_bus = bus
            wait = w
    return (best_bus, wait, best_bus * wait)




# part 2
def win_contest(inp, guess_start=1e14):
    buses = [None if x == "x" else int(x) for x in inp.split("\n")[1].split(",")]
    first_bus = buses[0]
    guess = (guess_start // first_bus) * first_bus # start us around the range of gs
    while True:
        if verify_guess(guess, buses):
            return guess
        guess += first_bus


def verify_guess(guess, buses):
    for bus in buses[1:]: # skip verifying first
        guess += 1
        if bus is None:
            continue
        if guess % bus != 0:
            return False
    return True


def win_2(inp, guess_start=1e14):
    bus_map = [(i, int(x)) for i,x in enumerate(inp.split("\n")[1].split(",")) if x != "x"]
    first_bus = bus_map.pop(0)[1]
    guess = (guess_start // first_bus) * first_bus # start us around the range of gs
    while True:
        if fast_verify(guess, bus_map):
            return guess
        guess += first_bus

def fast_verify(guess, bus_map):
    # bus_map: [(i,bus),]
    for i, bus in bus_map:
        if (guess + i) % bus != 0:
            return False
    return guess


from functools import reduce
from multiprocessing  import Pool

def win_3(inp, guess_start=1e14, paralell_factor=100, thread_count=8):
    # use max(bus) as the guess increment
    # use multiprocessing (WIP)
    bus_map = [(i, int(x)) for i,x in enumerate(inp.split("\n")[1].split(",")) if x != "x"]
    max_bus = reduce(lambda x, y: x if x[1] > y[1] else y, bus_map)[1]
    guess = (guess_start // max_bus) * max_bus
    guess_inc = max_bus * paralell_factor
    with Pool(thread_count) as p:
        while True:
            ## !! can't pickle (and thread) a lambda
            it = [(guess + i, bus_map) for i in range(0, guess_inc, max_bus)]
            results = p.starmap(fast_verify, it)
            if any(results):
                return [r for r in results if r != False]
            guess += guess_inc



## ??
def curry_fv(guess, bus_map):
    def inner(i):
        return fast_verify(guess + i, bus_map)
    return inner



def test_curry(a,b):
    def inner(c):
        return a+b+c
    return inner

def test_mp():
    with Pool(8) as p:
        f = test_curry(3,5)
        return p.map(f, range(0,10,2))

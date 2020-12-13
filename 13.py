
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

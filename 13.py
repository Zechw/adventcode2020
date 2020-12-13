

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

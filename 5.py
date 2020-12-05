
def parse_seat(seat_string):
    return (
        int(seat_string[:7].replace("F", "0").replace("B", "1"), 2),
        int(seat_string[7:].replace("L", "0").replace("R", "1"), 2)
    )

def occupied_seats(inputs):
    seat_ids = []
    for seat_string in inputs.split("\n"):
        seat = parse_seat(seat_string)
        seat_ids.append(seat[0] * 8 + seat[1])
    return seat_ids

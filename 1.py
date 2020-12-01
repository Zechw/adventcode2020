
def find_two_compliments(expenses, target=2020):
    while expenses:
        x = expenses.pop()
        c = target - x
        if c in expenses:
            return (c, x)


def find_three_compliments(expenses, target=2020):
    while expenses:
        x = expenses.pop()
        c = target - x
        c2 = find_two_compliments(expenses[:], c) # copy so we dont prune off OG expenses
        if c2:
            return (x,  c2[0], c2[1])

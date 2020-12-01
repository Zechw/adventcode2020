
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





def find_n_complements(expenses, target=2020, n=3):
    if n == 1 and target in expenses:
        return [target]
    elif n == 1:
        return None
    while expenses:
        x = expenses.pop()
        c = target - x
        found = find_n_complements(expenses[:], target=c, n=n-1)
        if found:
            found.append(x)
            return found

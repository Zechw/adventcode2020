

def fix_expences(expenses):
    while expenses:
        x = expenses.pop()
        c = 2020 - x
        if c in expenses:
            return c * x

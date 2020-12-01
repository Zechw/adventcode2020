8
def fix_expenses(expenses):
    while expenses:
        x = expenses.pop()
        c = 2020 - x
        if c in expenses:
            return c * x

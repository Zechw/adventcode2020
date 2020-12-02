import re

def count_valid_passwords(password_list):
    count = 0
    for row in password_list:
        if validate_password(row):
            count += 1
    return count



def validate_password(item):
    matches = re.match(r'(\d+)\-(\d+) (\w): (\w+)', item)
    if matches is None:
        raise ValueError("did not match expected format")
    lmin, lmax, c, p = matches.groups()
    lmin, lmax = int(lmin), int(lmax)
    return new_password_logic(lmin, lmax, c, p)



def old_password_logic(lmin, lmax, c, p):
    count = 0
    for x in p:
        if x == c:
            count += 1
            if count > lmax:
                return False
    if count < lmin:
        return False
    return True


def new_password_logic(i, j, c, p):
    return (p[i-1] == c) ^ (p[j-1] == c)

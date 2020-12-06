from functools import reduce

sum([len(set(x.replace("\n", ""))) for x in raw_data.split("\n\n")])

sum([len(reduce(lambda y, z: y & z, map(set, x.split("\n")))) for x in raw_data.split("\n\n")])

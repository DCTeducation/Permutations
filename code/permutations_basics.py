from itertools import permutations

items = ["A", "B", "C", "D", "E"]
r = 3

perms = list(permutations(items, r))
print(len(perms))
print(perms[:10])

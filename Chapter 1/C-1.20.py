from random import *


def shuffle(data):
    positions = {}
    used = []
    new_index = randint(0, (len(data) - 1))
    for i in data:
        while new_index in used:
            new_index = randint(0, (len(data) - 1))
        used.append(new_index)
        positions.setdefault(i, new_index)
    for i in positions:
        data[positions[i]] = i


app = [1, 3, 7, 8]
shuffle(app)
print(app)

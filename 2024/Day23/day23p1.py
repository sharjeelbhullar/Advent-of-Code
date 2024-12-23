import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
edges = [line.strip().split("-") for line in open(input_path)]
conns = {}

for x, y in edges:
    if x not in conns: conns[x] = set()
    if y not in conns: conns[y] = set()
    conns[x].add(y)
    conns[y].add(x)

sets = set()

for x in conns:
    for y in conns[x]:
        for z in conns[y]:
            if x != z and x in conns[z]:
                sets.add(tuple(sorted([x, y, z])))

print(len([s for s in sets if any(cn.startswith("t") for cn in s)]))
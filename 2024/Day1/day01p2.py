import os
input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

l, r = list(map(list, zip(*[list(map(int, line.split())) for line in open(input_path).read().splitlines()])))
print(sum(x * r.count(x) for x in l))
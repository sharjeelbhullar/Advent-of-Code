import os
input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
a = list(map(list, zip(*[list(map(int, line.split())) for line in open(input_path).read().splitlines()])))

for k in a: k.sort()

print(sum(abs(x - y) for x, y in zip(*a)))
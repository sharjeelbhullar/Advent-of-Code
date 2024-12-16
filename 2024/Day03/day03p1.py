import re
import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
memory = open(input_path).read()

total = 0

for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory):
    x, y = map(int, match[4:-1].split(","))
    total += x * y

print(total)
import re
import os
input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
memory = open(input_path).read()

on = True
total = 0

for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory):
    if match == "do()":
        on = True
    elif match == "don't()":
        on = False
    elif on:
        x, y = map(int, match[4:-1].split(","))
        total += x * y

print(total)
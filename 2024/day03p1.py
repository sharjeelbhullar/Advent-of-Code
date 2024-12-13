import re

memory = open("input.txt").read()

total = 0

for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory):
    x, y = map(int, match[4:-1].split(","))
    total += x * y

print(total)
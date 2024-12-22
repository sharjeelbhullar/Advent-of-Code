import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num

total = 0

for line in open(input_path):
    num = int(line)
    for _ in range(2000):
        num = step(num)
    total += num

print(total)
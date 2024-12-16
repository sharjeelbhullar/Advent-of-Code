import os
count = 0

def safe(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
for report in open(input_path):
    levels = list(map(int, report.split()))
    if safe(levels):
        count += 1

print(count)
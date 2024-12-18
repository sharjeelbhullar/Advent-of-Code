from collections import deque
import os

s = 70
n = 1024

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

grid = [[0] * (s + 1) for _ in range(s + 1)]
coords = [list(map(int, line.split(","))) for line in open(input_path)]

for c, r in coords[:n]:
    grid[r][c] = 1

q = deque([(0, 0, 0)])
seen = {(0, 0)}

while q:
    r, c, d = q.popleft()
    for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr > s or nc > s: continue
        if grid[nr][nc] == 1: continue
        if (nr, nc) in seen: continue
        if nr == nc == s:
            print(d + 1)
            exit(0)
        seen.add((nr, nc))
        q.append((nr, nc, d + 1))
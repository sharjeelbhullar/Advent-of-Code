from collections import deque
from typing import List, Tuple, Set, Dict
import os

input_path = os.path.join(os.path.dirname(__file__), 'input.txt')

def read_maze(filename: str) -> List[List[str]]:
    with open(filename) as f:
        return [list(line.strip()) for line in f.readlines()]

def find_start_end(maze: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    return start, end

def get_neighbors(pos: Tuple[int, int], maze: List[List[str]]) -> List[Tuple[int, int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dy, dx in directions:
        new_y, new_x = pos[0] + dy, pos[1] + dx
        if (0 <= new_y < len(maze) and 
            0 <= new_x < len(maze[0]) and 
            maze[new_y][new_x] != '#'):
            neighbors.append((new_y, new_x))
    return neighbors

def shortest_path(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for next_pos in get_neighbors(current, maze):
            if next_pos not in distances:
                distances[next_pos] = distances[current] + 1
                queue.append(next_pos)
    
    return distances

def find_cheats(maze: List[List[str]], normal_distances: Dict[Tuple[int, int], int], 
                start: Tuple[int, int], end: Tuple[int, int]) -> int:
    base_time = normal_distances[end]
    height, width = len(maze), len(maze[0])
    count = 0
    
    # Try all possible cheat start positions
    for y1 in range(height):
        for x1 in range(width):
            if maze[y1][x1] == '#':
                continue
            
            # If we can't reach this position, skip it
            if (y1, x1) not in normal_distances:
                continue
            
            # Try all possible cheat end positions within 2 steps
            for y2 in range(max(0, y1-2), min(height, y1+3)):
                for x2 in range(max(0, x1-2), min(width, x1+3)):  # Fixed: x2+3 -> x1+3
                    if maze[y2][x2] == '#':
                        continue
                        
                    # Calculate Manhattan distance for the cheat
                    cheat_length = abs(y2 - y1) + abs(x2 - x1)
                    if cheat_length > 2:
                        continue
                    
                    # Time to reach cheat start + cheat length + remaining distance
                    if (y2, x2) not in normal_distances:
                        continue
                        
                    total_time = (normal_distances[(y1, x1)] + 
                                cheat_length + 
                                normal_distances[end] - normal_distances[(y2, x2)])
                    
                    time_saved = base_time - total_time
                    if time_saved >= 100:
                        count += 1
    
    return count

def solve(filename: str) -> int:
    maze = read_maze(filename)
    start, end = find_start_end(maze)
    
    # Replace S and E with . for easier processing
    maze[start[0]][start[1]] = '.'
    maze[end[0]][end[1]] = '.'
    
    # Find shortest paths from both start and end
    normal_distances = shortest_path(maze, start, end)
    
    return find_cheats(maze, normal_distances, start, end)

if __name__ == "__main__":
    result = solve(input_path)
    print(f"Number of cheats saving ≥100 picoseconds: {result}")
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

def get_neighbors(pos: Tuple[int, int], maze: List[List[str]], ignore_walls: bool = False) -> List[Tuple[int, int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dy, dx in directions:
        new_y, new_x = pos[0] + dy, pos[1] + dx
        if (0 <= new_y < len(maze) and 
            0 <= new_x < len(maze[0]) and 
            (ignore_walls or maze[new_y][new_x] != '#')):
            neighbors.append((new_y, new_x))
    return neighbors

def shortest_path(maze: List[List[str]], start: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for next_pos in get_neighbors(current, maze):
            if next_pos not in distances:
                distances[next_pos] = distances[current] + 1
                queue.append(next_pos)
    
    return distances

def find_all_reachable_points(pos: Tuple[int, int], maze: List[List[str]], max_steps: int) -> Set[Tuple[Tuple[int, int], int]]:
    visited = set()
    queue = deque([(pos, 0)])
    result = set()
    
    while queue:
        current, steps = queue.popleft()
        if steps > max_steps:
            continue
            
        if maze[current[0]][current[1]] != '#':
            result.add((current, steps))
            
        if steps == max_steps:
            continue
            
        for next_pos in get_neighbors(current, maze, ignore_walls=True):
            next_state = (next_pos, steps + 1)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
                
    return result

def find_cheats_optimized(maze: List[List[str]], start_distances: Dict[Tuple[int, int], int], 
                         end_distances: Dict[Tuple[int, int], int], end: Tuple[int, int]) -> int:
    count = 0
    base_time = start_distances[end]
    visited_cheats = set()
    
    # Try all possible starting positions
    for start_pos, start_dist in start_distances.items():
        if maze[start_pos[0]][start_pos[1]] == '#':
            continue
            
        # Find all reachable points within 20 steps
        reachable_points = find_all_reachable_points(start_pos, maze, 20)
        
        # Check each endpoint
        for end_pos, cheat_length in reachable_points:
            if end_pos not in end_distances:
                continue
                
            # Skip if we've seen this cheat before
            cheat_key = (start_pos, end_pos)
            if cheat_key in visited_cheats:
                continue
                
            # Calculate time saved
            total_time = start_dist + cheat_length + end_distances[end_pos]
            time_saved = base_time - total_time
            
            if time_saved >= 100:
                count += 1
                visited_cheats.add(cheat_key)
    
    return count

def solve(filename: str) -> int:
    maze = read_maze(filename)
    start, end = find_start_end(maze)
    
    # Replace S and E with . for easier processing
    maze[start[0]][start[1]] = '.'
    maze[end[0]][end[1]] = '.'
    
    # Find shortest paths from both start and end
    start_distances = shortest_path(maze, start)
    end_distances = shortest_path(maze, end)
    
    return find_cheats_optimized(maze, start_distances, end_distances, end)

if __name__ == "__main__":
    result = solve(input_path)
    print(f"Number of cheats saving ≥100 picoseconds: {result}")
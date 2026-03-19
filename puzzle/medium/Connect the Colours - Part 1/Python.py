import sys
import time
from functools import lru_cache

grid = []
blockers = set()
vertical = set()
horizontal = set()
colour_tiles = {}
all_colour_tiles = {}
h, w = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    start = time.time()
    for j, char in enumerate(row):
        idx = i*w + j
        if char == "V":
            vertical.add(idx)
        elif char == "H":
            horizontal.add(idx)
        elif char == "X":
            blockers.add(idx)
        elif char != ".":
            all_colour_tiles[idx] = char
            colour_tiles.setdefault(char, [])
            colour_tiles[char].append(idx)
        if all_colour_tiles.get(idx, False) or char == "X":
            grid.append(char)
        else:
            grid.append(".")

checkpoints = {}
k = int(input())
for i in range(k):
    inputs = input().split()
    print(inputs, file = sys.stderr)
    idx = int(inputs[1])*w + int(inputs[0])
    checkpoints[idx] =  inputs[2]

neighbours = {}
for i in range(h):
    for j in range(w):
        idx = i*w + j
        for dy, dx in [[0,1],[-1,0],[0,-1],[1,0]]:
            new_idx = dy*w + idx + dx
            if 0<= i+dy < h and 0<=j+dx<w:
                if grid[new_idx] == "X": 
                    continue
                elif (idx in horizontal or new_idx in horizontal) and dy != 0: 
                    continue
                elif (idx in vertical or new_idx in vertical) and dx != 0: 
                    continue

                if new_idx in all_colour_tiles and idx in all_colour_tiles and all_colour_tiles[idx] != all_colour_tiles[new_idx]: 
                    continue
                
                if new_idx in all_colour_tiles:
                    if idx in checkpoints and checkpoints[idx] != all_colour_tiles[new_idx]: 
                        continue
                
                if idx in all_colour_tiles:
                    if new_idx in checkpoints and checkpoints[new_idx] != all_colour_tiles[idx]: 
                        continue

                neighbours.setdefault(idx, [])
                neighbours[idx].append(new_idx)

solution_found = [False]
colour_paths = {}
colours = list(colour_tiles.keys())
N = len(colours)

starting_bitmask = 0
for colour in colour_tiles.keys():
    for idx in colour_tiles[colour]:
        starting_bitmask |= (1 << idx)
for blocked in blockers:
    starting_bitmask |= (1 << blocked)

@lru_cache(None)
def find_paths(colour_idx, current_bitmask):
    if solution_found[0]:
        return True

    if colour_idx == N:
        goal_mask = (1 << (h * w)) - 1
        if current_bitmask == goal_mask:
            solution_found[0] = True
            return True
        return False

    @lru_cache(None)
    def find_colour_path(idx, path_mask):
        if solution_found[0]:
            return
        
        current_path.append((divmod(idx,w)))
        if idx == end_idx:
            if find_paths(colour_idx+1, current_bitmask | path_mask):
                colour_paths[colour] = list(current_path)
                solution_found[0] = True
            current_path.pop()
            return

        for nidx in neighbours[idx]:
            is_endpoint = nidx == end_idx
            is_empty = not ((current_bitmask >> nidx) & 1)
            
            if not ((path_mask >> nidx) & 1) and (nidx not in checkpoints or nidx in checkpoints and checkpoints[nidx] == colour):
                if is_empty or is_endpoint:
                    new_mask = path_mask | (1 << nidx)
                    find_colour_path(nidx, new_mask)
                    if solution_found[0]:
                        return
        current_path.pop()

    colour = colours[colour_idx]
    start_idx, end_idx = colour_tiles[colour]
    current_path = []
    find_colour_path(start_idx, (1 << start_idx)) 
    return solution_found[0]
    
if not find_paths(0, starting_bitmask):
    raise AssertionError("No valid full-covering path combination found")

for colour in colours:
    path = colour_paths[colour]
    for i in range(len(path) - 1):
        y1, x1 = path[i]
        y2, x2 = path[i+1]
        print(x1, y1, x2, y2, colour)

print(f"Execution time {round((time.time() - start)*1000)}ms" , file = sys.stderr)

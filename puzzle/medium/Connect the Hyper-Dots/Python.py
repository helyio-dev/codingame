import sys
import math

def solve():
    data = sys.stdin.readlines()
    
    count, n = map(int, data[0].split())
    
    points = []
    for line in data[1:count + 1]:
        parts = line.split()
        label = parts[0]
        coordinates = tuple(map(int, parts[1:]))
        points.append((label, coordinates))

    def dist_sq(p1, p2):
        d = 0
        for i in range(n):
            d += (p1[i] - p2[i]) ** 2
        return d

    def get_orthant(coords):
        orthant = []
        for c in coords:
            if c > 0:
                orthant.append(1)
            elif c < 0:
                orthant.append(-1)
            else:
                orthant.append(0)
        return tuple(orthant)

    phrase = ""
    
    current_coords = tuple([0] * n)
    current_label = ""
    current_orthant = get_orthant(current_coords)
    
    unused_indices = set(range(count))

    while unused_indices:
        
        best_index = -1
        min_dist_sq = float('inf')
        
        for idx in unused_indices:
            label, coords = points[idx]
            
            d_sq = dist_sq(current_coords, coords)
            
            if d_sq < min_dist_sq:
                min_dist_sq = d_sq
                best_index = idx
            
        if best_index == -1:
            break

        unused_indices.remove(best_index)
        
        next_label, next_coords = points[best_index]
        next_orthant = get_orthant(next_coords)
        
        should_space = False
        
        if next_label != current_label:
            cross_axis = False
            for i in range(n):
                c = current_orthant[i]
                n_c = next_orthant[i]
                
                if c == 0:
                    continue
                if c != n_c and n_c != 0:
                    cross_axis = True
                    break
            
            if cross_axis and phrase:
                should_space = True

        if should_space:
            phrase += " "
            
        phrase += next_label
        
        current_coords = next_coords
        current_orthant = next_orthant
        current_label = next_label

    print(phrase)

solve()
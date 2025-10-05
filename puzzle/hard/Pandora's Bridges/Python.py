import sys
import math

def solve():
    try:
        data = sys.stdin.read().splitlines()
    except:
        return

    if not data:
        return

    n = int(data[0])
    
    nodes = []
    nodes.append((1.0, 1.0, 1.0)) 

    for i in range(1, n + 1):
        try:
            x, y, z = map(float, data[i].split())
            nodes.append((x, y, z))
        except:
            continue 

    num_nodes = len(nodes)
    edges = []

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            x1, y1, z1 = nodes[i]
            x2, y2, z2 = nodes[j]

            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1

            length = math.sqrt(dx*dx + dy*dy + dz*dz)

            horizontal_dist = math.sqrt(dx*dx + dy*dy)
            
            angle_ok = False
            if horizontal_dist == 0:
                if dz == 0:
                    angle_ok = True
            elif abs(dz) / horizontal_dist < 1.0:
                angle_ok = True
            
            distance_ok = length <= 1000.0

            if angle_ok and distance_ok:
                edges.append((length, i, j))

    edges.sort()

    parent = list(range(num_nodes))
    rank = [0] * num_nodes

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False

    mst_edges = []
    for length, u, v in edges:
        if union(u, v):
            mst_edges.append((length, u, v))
    
    mst_edges.sort(key=lambda x: x[0], reverse=True)

    tree_length = 1000.0
    total_wood_required = 0.0
    trees_used = 0
    leftover_wood = [] 

    for length, u, v in mst_edges:
        total_wood_required += length
        
        found_leftover_index = -1
        for i in range(len(leftover_wood)):
            if leftover_wood[i] >= length:
                found_leftover_index = i
                break
        
        if found_leftover_index != -1:
            new_leftover = leftover_wood[found_leftover_index] - length
            leftover_wood[found_leftover_index] = new_leftover
        else:
            trees_used += 1
            new_leftover = tree_length - length
            leftover_wood.append(new_leftover)

    truncated_wood = math.floor(total_wood_required * 100) / 100.0
    
    sys.stdout.write(f"{truncated_wood:.2f}\n")
    sys.stdout.write(f"{trees_used}\n")

solve()
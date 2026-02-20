import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L, W, H = map(int, input_data[:3])
    slices_lines = input_data[3:]
    
    grid = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(L)]
    
    solid_volume = 0
    for l in range(L):
        current_slice_segments = slices_lines[l*H : (l+1)*H]
        for h in range(H):
            segment = current_slice_segments[h]
            for w in range(W):
                if segment[w] == '#':
                    grid[l][h][w] = 1
                    solid_volume += 1

    is_external = [[[False for _ in range(W)] for _ in range(H)] for _ in range(L)]
    external_void_count = 0
    
    for l in range(L):
        for h in range(H):
            for w in range(W):
                if (l == 0 or l == L-1 or h == 0 or h == H-1 or w == 0 or w == W-1):
                    if grid[l][h][w] == 0 and not is_external[l][h][w]:
                        stack = [(l, h, w)]
                        is_external[l][h][w] = True
                        while stack:
                            cl, ch, cw = stack.pop()
                            external_void_count += 1
                            for dl, dh, dw in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                                nl, nh, nw = cl + dl, ch + dh, cw + dw
                                if 0 <= nl < L and 0 <= nh < H and 0 <= nw < W:
                                    if not is_external[nl][nh][nw] and grid[nl][nh][nw] == 0:
                                        is_external[nl][nh][nw] = True
                                        stack.append((nl, nh, nw))

    surface_area = 0
    for l in range(L):
        for h in range(H):
            for w in range(W):
                if grid[l][h][w] == 1:
                    for dl, dh, dw in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                        nl, nh, nw = l + dl, h + dh, w + dw
                        if 0 <= nl < L and 0 <= nh < H and 0 <= nw < W:
                            if is_external[nl][nh][nw]:
                                surface_area += 1
                        else:
                            surface_area += 1
                                        
    bulk_volume = (L * W * H) - external_void_count
    
    activity = surface_area / solid_volume
    density = solid_volume / bulk_volume
    
    print(f"{activity:.4f} {density:.4f}")

if __name__ == "__main__":
    solve()
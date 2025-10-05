import sys
import math

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    x, y, a_deg = map(int, data[0].split())
    n = int(data[1])
    room = [list(row) for row in data[2:2+n]]

    a_rad = math.radians(a_deg)
    
    fov_half = math.radians(30)
    num_rays = 61
    frame_height = 15
    wall_height_factor = 1500

    def cast_ray(angle):
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        # Intersection Horizontale
        
        ya = math.floor(y / 100) * 100
        if sin_a > 1e-6:
            ya += 100
        
        dy = 100 if sin_a > 1e-6 else -100
        
        xa = x + (ya - y) / math.tan(angle) if math.fabs(sin_a) > 1e-6 else float('inf')
        
        dx = dy / math.tan(angle) if math.fabs(sin_a) > 1e-6 else 0
        
        h_wall_dist = float('inf')
        h_wall_hit = None
        
        current_xa = xa
        current_ya = ya
        
        while 0 <= current_xa <= n * 100 and 0 <= current_ya <= n * 100:
            r = int(current_ya / 100)
            c = int(current_xa / 100)
            
            if sin_a < 0:
                r -= 1
            
            if 0 <= r < n and 0 <= c < n and room[r][c] == '#':
                h_wall_dist = math.sqrt((current_xa - x)**2 + (current_ya - y)**2)
                h_wall_hit = '.'
                break
            
            current_xa += dx
            current_ya += dy

        # Intersection Verticale

        xa = math.floor(x / 100) * 100
        if cos_a > 1e-6:
            xa += 100
        
        dx = 100 if cos_a > 1e-6 else -100
        
        ya = y + (xa - x) * math.tan(angle) if math.fabs(cos_a) > 1e-6 else float('inf')
        
        dy = dx * math.tan(angle) if math.fabs(cos_a) > 1e-6 else 0
        
        v_wall_dist = float('inf')
        v_wall_hit = None
        
        current_xa = xa
        current_ya = ya
        
        while 0 <= current_xa <= n * 100 and 0 <= current_ya <= n * 100:
            r = int(current_ya / 100)
            c = int(current_xa / 100)
            
            if cos_a < 0:
                c -= 1
            
            if 0 <= r < n and 0 <= c < n and room[r][c] == '#':
                v_wall_dist = math.sqrt((current_xa - x)**2 + (current_ya - y)**2)
                v_wall_hit = ','
                break
            
            current_xa += dx
            current_ya += dy

        if h_wall_dist <= v_wall_dist:
            return h_wall_dist, h_wall_hit
        else:
            return v_wall_dist, v_wall_hit

    frame_cols = []
    
    for ray_index in range(num_rays):
        ray_angle_deg = a_deg - 30 + ray_index
        ray_angle_rad = math.radians(ray_angle_deg)
        
        angle_diff_rad = ray_angle_rad - a_rad
        
        distance, wall_char = cast_ray(ray_angle_rad)
        
        d_prime = distance * math.cos(angle_diff_rad)

        if d_prime > 0:
            h_int = round(wall_height_factor / d_prime)
        else:
            h_int = frame_height

        wall_block_size = min(h_int * 2 + 1, frame_height)
        
        num_spaces = frame_height - wall_block_size
        num_top_spaces = num_spaces // 2
        num_bottom_spaces = num_spaces - num_top_spaces
        
        col_str = ' ' * num_top_spaces + wall_char * wall_block_size + ' ' * num_bottom_spaces
        frame_cols.append(col_str)

    output = []
    for r in range(frame_height):
        row_str = ""
        for c in range(num_rays):
            row_str += frame_cols[c][r]
        output.append(row_str)

    sys.stdout.write('\n'.join(output) + '\n')

solve()
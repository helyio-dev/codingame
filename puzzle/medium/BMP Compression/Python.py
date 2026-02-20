import sys

def solve():
    header = sys.stdin.readline().split()
    if not header: return
    mode, width, height = header[0], int(header[1]), int(header[2])
    num_lines = int(sys.stdin.readline())
    
    if mode == 'B':
        grid = [sys.stdin.readline().strip() for _ in range(num_lines)]
        result = []

        def encode(x, y, w, h):
            if w == 0 or h == 0: return
            
            first = grid[y][x]
            uniform = True
            for r in range(y, y + h):
                for c in range(x, x + w):
                    if grid[r][c] != first:
                        uniform = False
                        break
                if not uniform: break
            
            if uniform:
                result.append('1' if first == '#' else '0')
            else:
                result.append('+')
                w_left = (w + 1) // 2
                w_right = w - w_left
                h_top = (h + 1) // 2
                h_bottom = h - h_top
                
                if h == 1: 
                    encode(x, y, w_left, h)
                    encode(x + w_left, y, w_right, h)
                elif w == 1: 
                    encode(x, y, w, h_top)
                    encode(x, y + h_top, w, h_bottom)
                else: 
                    encode(x, y, w_left, h_top) 
                    encode(x + w_left, y, w_right, h_top) 
                    encode(x, y + h_top, w_left, h_bottom) 
                    encode(x + w_left, y + h_top, w_right, h_bottom) 

        encode(0, 0, width, height)
        full_str = "".join(result)
        print(f"C {width} {height}")
        print((len(full_str) + 49) // 50)
        for i in range(0, len(full_str), 50):
            print(full_str[i:i+50])

    else:
        data = "".join(sys.stdin.readline().strip() for _ in range(num_lines))
        grid = [['' for _ in range(width)] for _ in range(height)]
        ptr = 0

        def decode(x, y, w, h):
            nonlocal ptr
            if w == 0 or h == 0: return
            
            char = data[ptr]
            ptr += 1
            
            if char == '+':
                w_left = (w + 1) // 2
                w_right = w - w_left
                h_top = (h + 1) // 2
                h_bottom = h - h_top
                
                if h == 1:
                    decode(x, y, w_left, h)
                    decode(x + w_left, y, w_right, h)
                elif w == 1:
                    decode(x, y, w, h_top)
                    decode(x, y + h_top, w, h_bottom)
                else:
                    decode(x, y, w_left, h_top)
                    decode(x + w_left, y, w_right, h_top)
                    decode(x, y + h_top, w_left, h_bottom)
                    decode(x + w_left, y + h_top, w_right, h_bottom)
            else:
                pixel = '#' if char == '1' else '.'
                for r in range(y, y + h):
                    for c in range(x, x + w):
                        grid[r][c] = pixel

        decode(0, 0, width, height)
        print(f"B {width} {height}")
        print(height)
        for row in grid:
            print("".join(row))

if __name__ == "__main__":
    solve()
import sys

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    qs = int(line.strip())
    
    q1 = [sys.stdin.readline().rstrip('\n') for _ in range(qs)]
    
    h_flip = {'b':'d', 'd':'b', 'p':'q', 'q':'p', '/': '\\', '\\': '/', '(': ')', ')': '(', '<': '>', '>': '<'}
    v_flip = {'b':'p', 'p':'b', 'd':'q', 'q':'d', '/': '\\', '\\': '/', '^': 'v', 'v': '^'}
    
    def get_char(char, flip_map):
        return flip_map.get(char, char)

    tile = []
    for r in range(qs):
        left = q1[r]
        right = "".join(get_char(c, h_flip) for c in reversed(left))
        tile.append(left + right)
        
    for r in range(qs - 1, -1, -1):
        row = "".join(get_char(c, v_flip) for c in tile[r])
        tile.append(row)

    border = "+" + "-" * (2 * qs) + "+" + "-" * (2 * qs) + "+"
    
    print(border)
    for _ in range(2):
        for row in tile:
            print(f"|{row}|{row}|")
        print(border)

if __name__ == "__main__":
    solve()
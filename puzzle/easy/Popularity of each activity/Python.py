import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        height = int(line1.strip())
    except ValueError:
        return

    grid = [sys.stdin.readline().rstrip('\n') for _ in range(height)]
    
    row_divs = [i for i, row in enumerate(grid) if '-' in row]
    col_divs = [j for j, char in enumerate(grid[row_divs[0]]) if char in (':', '+')]

    row_bounds = [0] + row_divs + [height]
    col_bounds = [0] + col_divs + [len(grid[0])]

    counts = []
    total = 0
    
    for r in range(3):
        row_counts = []
        for c in range(3):
            count = 0
            for i in range(row_bounds[r] + (1 if r > 0 else 0), row_bounds[r+1]):
                for j in range(col_bounds[c] + (1 if c > 0 else 0), col_bounds[c+1]):
                    if j < len(grid[i]) and grid[i][j] == '*':
                        count += 1
            row_counts.append(count)
            total += count
        counts.append(row_counts)

    print(f"{total} attendees")

    for row in counts:
        formatted_row = []
        for val in row:
            perc = round((val / total) * 100)
            formatted_row.append(f"{perc}%".rjust(4, '_'))
        print(" ".join(formatted_row))

if __name__ == "__main__":
    solve()
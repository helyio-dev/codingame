def normalize(ch, valid):
    return ch if ch in valid else None

def main():
    pieces = input()
    valid = set(pieces) | set(pieces.lower())

    before = [input() for _ in range(8)]
    after = [input() for _ in range(8)]

    before_grid = [[normalize(c, valid) for c in row] for row in before]
    after_grid = [[normalize(c, valid) for c in row] for row in after]

    source = None
    dest = None

    for i in range(8):
        for j in range(8):
            b = before_grid[i][j]
            a = after_grid[i][j]
            if b != a:
                if a is None and b is not None:
                    source = (i, j, b)
                elif a is not None:
                    dest = (i, j, a, b)

    si, sj, piece = source
    di, dj, moved_piece, captured = dest

    def coord(i, j):
        file_letter = chr(ord('a') + j)
        rank = 8 - i
        return f"{file_letter}{rank}"

    sep = "-" if captured is None else "x"
    print(f"{coord(si, sj)}{sep}{coord(di, dj)}")

    drow = abs(di - si)
    dcol = abs(dj - sj)
    is_knight = (drow, dcol) in [(1, 2), (2, 1)]
    print("Knight" if is_knight else "Other")

if __name__ == "__main__":
    main()
import sys

EPS = 1e-9

def intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    a1 = y2 - y1
    b1 = x1 - x2
    c1 = a1 * x1 + b1 * y1

    a2 = y4 - y3
    b2 = x3 - x4
    c2 = a2 * x3 + b2 * y3

    det = a1 * b2 - a2 * b1

    if abs(det) < EPS:
        return None

    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det

    return (x, y)


def clean_zero(value):
    if abs(value) < 1e-9:
        return 0.0
    return value


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    lines = []
    idx = 1

    for _ in range(n):
        x1 = float(data[idx]); y1 = float(data[idx+1])
        x2 = float(data[idx+2]); y2 = float(data[idx+3])
        idx += 4
        lines.append((x1, y1, x2, y2))

    points = set()

    for i in range(n):
        for j in range(i + 1, n):
            pt = intersection(lines[i], lines[j])
            if pt is not None:
                x = round(pt[0], 9)
                y = round(pt[1], 9)
                x = clean_zero(x)
                y = clean_zero(y)
                points.add((x, y))

    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))

    print(len(sorted_points))
    for x, y in sorted_points:
        x = clean_zero(x)
        y = clean_zero(y)
        print(f"{x:.3f} {y:.3f}")


if __name__ == "__main__":
    main()

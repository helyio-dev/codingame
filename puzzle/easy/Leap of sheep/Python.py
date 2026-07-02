import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    heights = [int(x) for x in input_data[1:]]

    left_min = [0] * n
    current_min = heights[0]
    for i in range(n):
        if heights[i] < current_min:
            current_min = heights[i]
        left_min[i] = current_min

    right_min = [0] * n
    current_min = heights[-1]
    for i in range(n - 1, -1, -1):
        if heights[i] < current_min:
            current_min = heights[i]
        right_min[i] = current_min

    max_diff = 0
    for i in range(1, n - 1):
        if heights[i] > left_min[i - 1] and heights[i] > right_min[i + 1]:
            diff = (heights[i] - left_min[i - 1]) + (
                heights[i] - right_min[i + 1]
            )
            if diff > max_diff:
                max_diff = diff

    print(max_diff)


if __name__ == "__main__":
    solve()
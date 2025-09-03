import sys
import math

W, H = [int(i) for i in input().split()]
grid = []
for i in range(H):
    grid.append([int(j) for j in input().split()])
EX = int(input())

movements = {
    1: {"TOP": (0, 1), "LEFT": (0, 1), "RIGHT": (0, 1)},
    2: {"LEFT": (1, 0), "RIGHT": (-1, 0)},
    3: {"TOP": (0, 1)},
    4: {"TOP": (-1, 0), "RIGHT": (0, 1)},
    5: {"TOP": (1, 0), "LEFT": (0, 1)},
    6: {"LEFT": (1, 0), "RIGHT": (-1, 0)},
    7: {"TOP": (0, 1), "RIGHT": (0, 1)},
    8: {"LEFT": (0, 1), "RIGHT": (0, 1)},
    9: {"TOP": (0, 1), "LEFT": (0, 1)},
    10: {"TOP": (-1, 0)},
    11: {"TOP": (1, 0)},
    12: {"RIGHT": (0, 1)},
    13: {"LEFT": (0, 1)},
}

while True:
    XI, YI, POS = input().split()
    XI = int(XI)
    YI = int(YI)

    current_piece_type = grid[YI][XI]
    dx, dy = movements[current_piece_type][POS]
    X_next = XI + dx
    Y_next = YI + dy

    print(str(X_next) + " " + str(Y_next))
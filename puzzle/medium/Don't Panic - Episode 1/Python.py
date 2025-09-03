import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators = {}
for _ in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

while True:
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1])
    direction = inputs[2]

    if clone_floor == -1:
        print("WAIT")
        continue

    target_pos = elevators.get(clone_floor, exit_pos)

    if direction == "RIGHT" and clone_pos > target_pos:
        print("BLOCK")
    elif direction == "LEFT" and clone_pos < target_pos:
        print("BLOCK")
    else:
        print("WAIT")

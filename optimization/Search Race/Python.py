import math

checkpoints = int(input())
cp_list = [tuple(map(int, input().split())) for _ in range(checkpoints)]

def angle_to_target(x, y, tx, ty):
    dx = tx - x
    dy = ty - y
    return math.degrees(math.atan2(dy, dx))

while True:
    checkpointIndex, x, y, vx, vy, angle = map(int, input().split())
    tx, ty = cp_list[checkpointIndex]

    target_angle = angle_to_target(x, y, tx, ty)
    angle_diff = ((target_angle - angle + 180) % 360) - 180

    if abs(angle_diff) > 90:
        thrust = 0
    elif abs(angle_diff) > 45:
        thrust = 50
    else:
        thrust = 200

    print(f"{tx} {ty} {thrust}")

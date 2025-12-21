import sys

grid = [input() for _ in range(15)]

players_a = []
players_b = []
ball = None
team = ""

for y in range(15):
    for x in range(51):
        c = grid[y][x]
        if c in "aA": players_a.append((x, c == "A"))
        elif c in "bB": players_b.append((x, c == "B"))
        elif c == "o": ball, team = x, "A"
        elif c == "O": ball, team = x, "B"

is_throw_in = any(grid[y][ball] in "oO" for y in [0, 14])

offside_count = 0
is_var_offside = False

if not is_throw_in:
    if team == "A":
        opponents_x = sorted([p[0] for p in players_b])
        limit = opponents_x[1]
        for x, active in players_a:
            if x < 25 and x < ball and x < limit:
                offside_count += 1
                if active: is_var_offside = True
    else:
        opponents_x = sorted([p[0] for p in players_a], reverse=True)
        limit = opponents_x[1]
        for x, active in players_b:
            if x > 25 and x > ball and x > limit:
                offside_count += 1
                if active: is_var_offside = True

if offside_count == 0:
    print("No player in an offside position.")
else:
    print(f"{offside_count} player(s) in an offside position.")

print("VAR: OFFSIDE!" if is_var_offside else "VAR: ONSIDE!")
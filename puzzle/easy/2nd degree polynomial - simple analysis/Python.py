import math

def fmt(x):
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{round(x+1e-8,2)}"

a,b,c = map(float, input().split())
points = []

if abs(a) < 1e-9:
    if abs(b) < 1e-9:
        if abs(c) < 1e-9:
            points.append((0,0))
        else:
            points.append((0,c))
    else:
        x = -c/b
        points.append((x,0))
        points.append((0,c))
else:
    delta = b**2 - 4*a*c
    if delta < -1e-9:
        points.append((0,c))
    elif abs(delta) < 1e-9:
        x = -b/(2*a)
        points.append((x,0))
        points.append((0,c))
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b - sqrt_delta)/(2*a)
        x2 = (-b + sqrt_delta)/(2*a)
        if x1 > x2:
            x1,x2 = x2,x1
        points.append((x1,0))
        points.append((0,c))
        points.append((x2,0))

points.sort(key=lambda p: p[0])
print(",".join(f"({fmt(x)},{fmt(y)})" for x,y in points))

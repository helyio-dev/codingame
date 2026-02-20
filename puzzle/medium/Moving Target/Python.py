import sys
import math

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    pex, pey, pez = map(float, data[0:3])
    vex, vey, vez = map(float, data[3:6])
    pgx, pgy, pgz = map(float, data[6:9])
    vp = float(data[9])

    dx = pex - pgx
    dy = pey - pgy
    dz = pez - pgz

    a = vex**2 + vey**2 + vez**2 - vp**2
    b = 2 * (dx * vex + dy * vey + dz * vez)
    c = dx**2 + dy**2 + dz**2

    t = None
    if abs(a) < 1e-9:
        if abs(b) > 1e-9:
            t_lin = -c / b
            if t_lin > 0:
                t = t_lin
    else:
        delta = b**2 - 4 * a * c
        if delta >= 0:
            sqrt_delta = math.sqrt(delta)
            t1 = (-b - sqrt_delta) / (2 * a)
            t2 = (-b + sqrt_delta) / (2 * a)
            
            valid_times = sorted([v for v in [t1, t2] if v > 1e-9])
            if valid_times:
                t = valid_times[0]

    if t is None:
        print("Impossible")
    else:
        vpx = (dx + t * vex) / t
        vpy = (dy + t * vey) / t
        vpz = (dz + t * vez) / t
        print(f"{vpx:.4f} {vpy:.4f} {vpz:.4f}")
        print(f"{t:.4f}")

if __name__ == "__main__":
    solve()
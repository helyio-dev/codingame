import sys

def solve():
    dist_map = {
        "inches": 1,
        "feet": 12,
        "yards": 12 * 3,
        "chains": 12 * 3 * 22,
        "furlongs": 12 * 3 * 22 * 10,
        "miles": 12 * 3 * 22 * 10 * 8
    }
    
    time_map = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 3600 * 24,
        "week": 3600 * 24 * 7,
        "fortnight": 3600 * 24 * 7 * 2
    }
    
    line = sys.stdin.readline().split()
    
    val1 = int(line[0])
    unit_d1 = line[1]
    unit_t1 = line[3]
    
    unit_d2 = line[6]
    unit_t2 = line[8]
    
    val_in_inches = val1 * dist_map[unit_d1]
    speed_inches_per_sec = val_in_inches / time_map[unit_t1]
    
    final_speed = (speed_inches_per_sec * time_map[unit_t2]) / dist_map[unit_d2]
    
    print(f"{round(final_speed, 1):.1f} {unit_d2} per {unit_t2}")

solve()
import math
import re

try:
    s = input()
    d = "".join(re.findall(r'\d', s))
    if not d:
        print("OUT OF RANGE")
    else:
        R = float(d)
        v = 158
        g = 9.8
        
        val = (R * g) / (v**2)
        
        if val > 1 or R > 1800:  
            print("OUT OF RANGE")
        else:
            theta_rad = math.asin(val) / 2
            angle1 = math.degrees(theta_rad)
            angle2 = 90 - angle1
            
            res_theta = None
            for a in [angle2, angle1]:
                if 40 <= a <= 85:
                    res_theta = a
                    break
            
            if res_theta is None:
                print("OUT OF RANGE")
            else:
                t = (2 * v * math.sin(math.radians(res_theta))) / g
                print(f"{res_theta:.1f} degrees")
                print(f"{t:.1f} seconds")
except EOFError:
    pass
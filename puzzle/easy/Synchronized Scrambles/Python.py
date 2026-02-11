import sys

def parse_offset(offset_str):
    sign = 1 if offset_str[0] == '+' else -1
    hours = int(offset_str[1:3])
    minutes = int(offset_str[3:5])
    return sign * (hours * 60 + minutes)

def get_hhmm(total_minutes):
    total_minutes %= 1440
    h, m = divmod(total_minutes, 60)
    return f"{h:02d}{m:02d}"

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    off1_min = parse_offset(input_data[0])
    off2_min = parse_offset(input_data[1])
    
    results = []
    
    for utc_min in range(1440):
        t1 = get_hhmm(utc_min + off1_min)
        t2 = get_hhmm(utc_min + off2_min)
        
        if is_anagram(t1, t2):
            results.append(f"{t1}, {t2}")
            
    for res in sorted(list(set(results))):
        print(res)

if __name__ == "__main__":
    solve()
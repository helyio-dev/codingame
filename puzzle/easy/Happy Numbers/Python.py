N = int(input())
numbers = [input().strip() for _ in range(N)]

def is_happy(num_str):
    seen = set()
    while True:
        if num_str == "1":
            return True
        if num_str in seen:
            return False
        seen.add(num_str)
        s = sum(int(d)**2 for d in num_str)
        num_str = str(s)

for num in numbers:
    print(f"{num} {':)' if is_happy(num) else ':('}")

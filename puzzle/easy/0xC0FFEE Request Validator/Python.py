import sys

frame_len = int(sys.stdin.readline())
frame = sys.stdin.readline().strip()

def solve():
    if frame_len < 12 or not frame.startswith("DECAFBAD"):
        print("403 Forbidden")
        return

    try:
        order_size = int(frame[8:11], 16)
    except ValueError:
        print("403 Forbidden")
        return

    if frame_len != 12 + order_size:
        print("403 Forbidden")
        return

    total_sum = sum(int(c, 16) for c in frame)
    if total_sum % 16 != 0:
        print("403 Forbidden")
        return

    order = frame[11:-1]
    counts = {}
    order_of_appearance = []

    for drink_id in order:
        if drink_id not in counts:
            counts[drink_id] = 0
            order_of_appearance.append(drink_id)
        counts[drink_id] += 1

    for drink_id in order_of_appearance:
        print(f"{counts[drink_id]} {drink_id}")

solve()
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    g = int(input_data[0])
    e = int(input_data[1])

    idx = 2
    student_to_group = {}
    for group_id in range(g):
        group_members = []
        while idx < len(input_data):
            val = int(input_data[idx])
            idx += 1
            student_to_group[val] = group_id
            if idx < len(input_data) and input_data[idx].find("\n") == -1:
                pass
            break

    lines = sys.stdin.read().splitlines()

def main():
    import sys

    input_text = sys.stdin.read().split()
    if not input_text:
        return

    g = int(input_text[0])
    e = int(input_text[1])

    student_to_group = {}
    idx = 2

if __name__ == "__main__":
    import sys

    lines = sys.stdin.read().splitlines()
    if not lines:
        exit()

    g, e = map(int, lines[0].split())

    student_to_group = {}
    for group_id in range(g):
        members = map(int, lines[1 + group_id].split())
        for m in members:
            student_to_group[m] = group_id

    events_line = []
    for i in range(1 + g, len(lines)):
        events_line.extend(lines[i].split())

    events = [int(x) for x in events_line]

    queue = []
    group_last_pos = {}

    for event in events:
        if event == -1:
            if queue:
                leaving = queue.pop(0)
                print(leaving)
                for gid in list(group_last_pos.keys()):
                    if group_last_pos[gid] == 0:
                        del group_last_pos[gid]
                    else:
                        group_last_pos[gid] -= 1
        else:
            student = event
            gid = student_to_group.get(student, -1)

            if gid != -1 and gid in group_last_pos:
                pos = group_last_pos[gid] + 1
                queue.insert(pos, student)
                group_last_pos[gid] = pos
                for other_gid in group_last_pos:
                    if (
                        other_gid != gid
                        and group_last_pos[other_gid] >= pos - 1
                    ):
                        group_last_pos[other_gid] += 1
            else:
                queue.append(student)
                if gid != -1:
                    group_last_pos[gid] = len(queue) - 1
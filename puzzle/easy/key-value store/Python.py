from collections import OrderedDict

N = int(input())
store = OrderedDict()

for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == "SET":
        for pair in cmd[1:]:
            key, value = pair.split("=")
            if key not in store:
                store[key] = value
            else:
                store[key] = value
    elif cmd[0] == "GET":
        output = []
        for key in cmd[1:]:
            output.append(store.get(key, "null"))
        print(" ".join(output))
    elif cmd[0] == "EXISTS":
        output = []
        for key in cmd[1:]:
            output.append("true" if key in store else "false")
        print(" ".join(output))
    elif cmd[0] == "KEYS":
        if store:
            print(" ".join(store.keys()))
        else:
            print("EMPTY")

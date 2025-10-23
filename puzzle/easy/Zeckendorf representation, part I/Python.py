import sys

def solve():
    try:
        N = int(sys.stdin.readline())
    except:
        return

    fib = [0, 1]
    a, b = 1, 1
    while b <= N:
        fib.append(b)
        a, b = b, a + b

    fib = fib[2:]
    
    representation = []
    
    for f in reversed(fib):
        if N >= f:
            representation.append(str(f))
            N -= f
            
    print("+".join(representation))

if __name__ == "__main__":
    solve()
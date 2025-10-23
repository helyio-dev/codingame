import sys
import io

def ip_to_int(ip_addr):
    parts = ip_addr.split('.')
    return (int(parts[0]) << 24) | (int(parts[1]) << 16) | (int(parts[2]) << 8) | int(parts[3])

M = int(sys.stdin.readline())

for _ in range(M):
    line = sys.stdin.readline().strip()
    if not line:
        continue
    ip_cidr = line.split('/')
    ip_addr = ip_cidr[0]
    S = int(ip_cidr[1])

    A = ip_to_int(ip_addr)
    V = 32 - S
    N = 1 << V

    if A & ((1 << V) - 1) == 0:
        print("valid " + str(N))
    else:
        if A == 0:
            T = 32
        else:
            T = (A & -A).bit_length() - 1
        
        S_new = 32 - T
        N_new = 1 << T
        
        print("invalid " + ip_addr + "/" + str(S_new) + " " + str(N_new))
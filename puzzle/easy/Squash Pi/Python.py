import sys
from math import isqrt

sys.set_int_max_str_digits(1000000)

def compute_pi_int(digits):
    C3_OVER_24 = 640320**3 // 24

    def bin_split(a, b):
        if b - a == 1:
            if a == 0:
                Pab = Qab = 1
            else:
                Pab = (6*a-5)*(2*a-1)*(6*a-1)
                Qab = a*a*a*C3_OVER_24
            Tab = Pab * (13591409 + 545140134*a)
            if a & 1:
                Tab = -Tab
            return Pab, Qab, Tab
        m = (a + b) // 2
        Pam, Qam, Tam = bin_split(a, m)
        Pmb, Qmb, Tmb = bin_split(m, b)
        return Pam*Pmb, Qam*Qmb, Tam*Qmb + Pam*Tmb

    DIGITS_PER_TERM = 14.1816474627254776555
    N = int(digits / DIGITS_PER_TERM) + 3
    P, Q, T = bin_split(0, N)

    one_squared = 10**(2*digits)
    sqrtC = isqrt(10005 * one_squared)
    return (Q * 426880 * sqrtC) // T

def main():
    index = int(input())
    n = int(input())
    GUARD = 5
    digits = index + n + GUARD
    pi_int = compute_pi_int(digits)
    shift = GUARD + 1
    extracted = (pi_int // 10**shift) % 10**n
    print(str(extracted).zfill(n))

if __name__ == "__main__":
    main()
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void solve() {
    long long N;
    if (scanf("%lld", &N) != 1) return;

    if (N <= 3) {
        printf("%lld\n", N);
        return;
    }

    long long fib[100];
    int count = 2;
    fib[0] = 1; 
    fib[1] = 2; 

    while (1) {
        long long next_fib = fib[count - 1] + fib[count - 2];
        if (next_fib > N) {
            break;
        }
        fib[count++] = next_fib;
    }

    long long representation[100];
    int rep_count = 0;
    
    for (int i = count - 1; i >= 0; i--) {
        if (N >= fib[i]) {
            representation[rep_count++] = fib[i];
            N -= fib[i];
        }
    }

    for (int i = 0; i < rep_count; i++) {
        printf("%lld", representation[i]);
        if (i < rep_count - 1) {
            printf("+");
        }
    }
    printf("\n");
}

int main() {
    solve();
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>

unsigned int ip_to_int(const char *ip_addr) {
    unsigned int a, b, c, d;
    sscanf(ip_addr, "%u.%u.%u.%u", &a, &b, &c, &d);
    return (a << 24) | (b << 16) | (c << 8) | d;
}

int main() {
    int M;
    if (scanf("%d", &M) != 1) return 1;

    for (int i = 0; i < M; ++i) {
        char line[50];
        if (scanf("%s", line) != 1) continue;

        char ip_addr[20];
        int S;
        char *slash = strchr(line, '/');
        
        if (slash) {
            *slash = '\0';
            strcpy(ip_addr, line);
            S = atoi(slash + 1);
        } else {
            continue;
        }

        unsigned int A = ip_to_int(ip_addr);
        int V = 32 - S;
        unsigned long long N = 1ULL << V;
        
        int is_valid = 0;
        if (V == 32) {
            if (A == 0) {
                is_valid = 1;
            }
        } else {
            if ((A & ((1U << V) - 1)) == 0) {
                is_valid = 1;
            }
        }

        if (is_valid) {
            printf("valid %llu\n", N);
        } else {
            int T;
            if (A == 0) {
                T = 32;
            } else {
                T = 0;
                unsigned int temp_A = A;
                if (temp_A != 0) {
                    while (!(temp_A & 1)) {
                        temp_A >>= 1;
                        T++;
                    }
                }
            }
            
            int S_new = 32 - T;
            unsigned long long N_new = 1ULL << T;
            
            printf("invalid %s/%d %llu\n", ip_addr, S_new, N_new);
        }
    }

    return 0;
}
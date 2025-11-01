#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

#define N_OUTCOMES 38
#define MAX_N 50

long double S[MAX_N + 1][MAX_N + 1] = {0};

void calculate_stirling() {
    S[0][0] = 1;
    for (int n = 1; n <= MAX_N; ++n) {
        for (int k = 1; k <= n; ++k) {
            S[n][k] = S[n - 1][k - 1] + k * S[n - 1][k];
        }
    }
}

long double combinations(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;
    if (k > n / 2) k = n - k;
    
    long double res = 1;
    for (int i = 1; i <= k; ++i) {
        res = res * (n - i + 1) / i;
    }
    return res;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int m, n;
    if (!(std::cin >> m >> n)) return 0;

    calculate_stirling();

    long double total_favorable_outcomes = 0;
    
    int max_k = std::min(n, N_OUTCOMES);
    
    for (int k = m; k <= max_k; ++k) {
        long double term_k = S[n][k];
        for (int i = 1; i <= k; ++i) {
             term_k *= i;
        }

        total_favorable_outcomes += combinations(N_OUTCOMES, k) * term_k;
    }

    long double total_outcomes = std::pow((long double)N_OUTCOMES, n);
    
    long double probability = total_favorable_outcomes / total_outcomes;

    long long result_percent = std::round(probability * 100);
    std::cout << result_percent << "%" << std::endl;
    
    return 0;
}
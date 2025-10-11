#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int L, C, N;
    cin >> L >> C >> N; cin.ignore();
    
    vector<int> p(N); 
    vector<int> earnings_memoized(N, -1); 
    vector<int> index_jump_memoized(N, -1); 
    
    for (int i = 0; i < N; ++i) {
        cin >> p[i]; cin.ignore();
    }
    
    unsigned long long total_earnings = 0;
    int index = 0;
    
    for (int ride = 0; ride < C; ++ride) {
        if (earnings_memoized[index] != -1) { 
            total_earnings += earnings_memoized[index];
            index = index_jump_memoized[index];
        }
        else {
            int earnings = 0;
            int places = L;
            int i = index;
            int groups = 0;
            
            while (places > 0 and p[i] <= places) {
                earnings += p[i];
                places -= p[i];
                i = (i + 1) % N;
                if (++groups == N) { 
                    i = 0;
                    break;
                }
            }
            
            earnings_memoized[index] = earnings;
            index_jump_memoized[index] = i;
            total_earnings += earnings;
            index = i;
        }
    }
    
    cout << total_earnings << endl;
}
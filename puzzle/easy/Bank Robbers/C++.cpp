#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    int r;
    cin >> r; cin.ignore();
    int v;
    cin >> v; cin.ignore();
    
    priority_queue<long long, vector<long long>, greater<long long>> robbers;
    for (int i = 0; i < r; i++) {
        robbers.push(0);
    }
    
    for (int i = 0; i < v; i++) {
        int c, n;
        cin >> c >> n; cin.ignore();
        
        long long combinations = 1;
        for (int j = 0; j < n; j++) combinations *= 10;
        for (int j = 0; j < (c - n); j++) combinations *= 5;
        
        long long earliest_available = robbers.top();
        robbers.pop();
        robbers.push(earliest_available + combinations);
    }
    
    long long total_time = 0;
    while (!robbers.empty()) {
        total_time = max(total_time, robbers.top());
        robbers.pop();
    }
    
    cout << total_time << endl;
    return 0;
}

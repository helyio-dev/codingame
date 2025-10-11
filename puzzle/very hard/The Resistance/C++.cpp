#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string alphabet[] = { 
    ".-", "-...", "-.-.", "-..", ".", "..-.", 
    "--.", "....", "..", ".---", "-.-", ".-..", 
    "--", "-.", "---", ".--.", "--.-", ".-.", 
    "...", "-", "..-", "...-", ".--", "-..-", 
    "-.--", "--..",
};
unordered_map<string,int> times; 
ll dp[(int)1e5];
string seq; 

string encode(const string& s)
{
    string r;
    for (char c : s) r += alphabet[c-'A'];
    return r;
}

ll cnt(int i)
{
    if (i == seq.size()) return 1;
    if (i > seq.size()) return 0;
    ll& mem = dp[i];
    if (mem == -1) {
        string s;
        mem = 0;
        for (int j = i; j <= i+80 and j < seq.size(); ++j) { 
            s += seq[j];
            auto it = times.find(s);
            if (it != times.end()) {
                mem += it->second * cnt(j+1);
            }
        }
    }
    return mem;
}

int main()
{
    memset(dp, 0xFF, sizeof(dp)); 
    int n;
    cin >> seq;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string word;
        cin >> word;
        ++times[encode(word)];
    }
    cout << cnt(0) << endl;
}
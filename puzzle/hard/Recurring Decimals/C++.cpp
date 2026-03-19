#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{   
    int n;
    cin >> n; cin.ignore();
    int remainder = 1;

    string res = "";
    int idx = 0;
    unordered_map<int, int> values = {};

    while (remainder != 0){
        if (values.contains(remainder)){
            string left = res.substr(0,values[remainder]);
            string right = res.substr(values[remainder],res.size());
            res = left + "(" + right + ")";
            break;
        }
        values[remainder] = idx;

        remainder *= 10;
        int val = remainder / n;
        res += std::to_string(val);
        remainder = remainder % n;
        
        idx += 1;
    }
    cout << "0." << res << endl;
}
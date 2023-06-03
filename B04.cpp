#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int x = 0;
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '1') x += (1 << (s.size()-1-i));
    }
    cout << x << endl;
}
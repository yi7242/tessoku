#include <bits/stdc++.h>
using namespace std;
 
int a[100009];
map<string, int> m;
int main() {
    int q;
    cin >> q;
    
    for (int i = 0; i < q; i++) {
        int shurui;
        cin >> shurui;
        if (shurui == 1) {
            string s;
            int point;
            cin >> s >> point;
            m[s] = point;
        }
        else {
            string s;
            cin >> s;
            cout << m[s] << endl;
        }
    }
}
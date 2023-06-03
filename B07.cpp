#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int t;
    int n;

    int jikanhi[500009];
    int timetable[500009];
    for (int i = 0; i < 500009; i++) {
        jikanhi[i] = 0;
        timetable[i] = 0;
    }

    cin >> t >> n;
    for (int i = 0; i < n; i++) {
        int l,r;
        cin >> l >> r;
        jikanhi[l]++;
        jikanhi[r]--;
    }
    int now = 0;
    for (int i = 0; i < t; i++){
        now += jikanhi[i];
        cout << now << endl;
    }
}
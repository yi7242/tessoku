#include <bits/stdc++.h>
using namespace std;
 
int a[100009];
int n,k;
void solve() {
    long long count = 0;
    int start = 1;
    a[0] = 0;
    for (int i = 1;i <= n; i++) a[i] += a[i-1];
    for (int i = 1; i <= n-1; i++) {
        while(start < n && (a[start + 1] - a[i]) <= k) {
            start++;
            // cout << i << ": " <<  start << endl;
        }
        count += start - i;
    }
    
    cout << count << endl;
    
}

int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++) cin >> a[i];
    solve();
    return 0;
}
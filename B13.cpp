#include <bits/stdc++.h>
using namespace std;
 
int a[100009];
int n,k;
void solve() {
    for (int i = 1; i <= n; i++) {
        a[i] += a[i-1];
    }
    int start = 0;
    long long count = 0;
    for (int i = 0; i < n; i++) {
        while (start < n&&a[start+1] - a[i] <=k) {
            start++;
        }
        count += (start - i);
    }
    cout << count << endl;
}

int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++) cin >> a[i];
    solve();
    return 0;
}
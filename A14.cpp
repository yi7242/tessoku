#include <bits/stdc++.h>
using namespace std;
 
int n,k;
int a[1009];
int b[1009];
int c[1009];
int d[1009];
int p[1000009];
int q[1000009];
int solve() {
    for(int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            p[(i-1) * n + j] = a[i] + b[j];
        }
    }
    // cout << "---------" << endl;
    for(int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            q[(i-1) * n + j] = c[i] + d[j];
        }
    }

    sort(q+1, q+(n*n)+1);

    for (int i = 1; i <= n*n; i++) {
        // cout << i << ", " << p[i] << endl;
        int pos1 = lower_bound(q+1, q+(n*n) + 1, k-p[i]) - q;
        // cout <<pos1 << ", " << q[pos1] << endl;
        if (pos1 <= n*n && q[pos1] == k-p[i]) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}

int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    for (int i = 1; i <= n; i++) {
        cin >> b[i];
    }
    for (int i = 1; i <= n; i++) {
        cin >> c[i];
    }
    for (int i = 1; i <= n; i++) {
        cin >> d[i];
    }
    solve();
}
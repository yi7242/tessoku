#include <bits/stdc++.h>
using namespace std;
 
int a[100009];
int p[100009];
int q[100009];

int main() {
    int n,d;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    cin >> d;
    for (int i = 0; i < 100009; i++) {
        p[i] = 0;
        q[i] = 0;
    }
    
    for (int i = 1; i <= n; i++){
        p[i] = max(p[i-1] , a[i]);
        // cout << "pno" << i << "is" << p[i] << endl;
    } 
    for (int i = n; i > 0; i--) {
        q[i] = max(q[i+1] , a[i]);
        // cout << "qno" << i << "is" << q[i] << endl;
    }

    for (int i = 0; i < d; i++) {
        int l, r;
        cin >> l >> r;
        int ans = max(p[l-1], q[r+1]);
        cout << ans << endl;
    }
}
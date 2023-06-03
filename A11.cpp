#include <bits/stdc++.h>
using namespace std;
 
int a[100009];

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    int q;
    cin >> q;
    // cout << "aaa" << endl;
    sort(a+1, a+n+1);   
    for (int i = 0; i < q; i++) {
        int x;
        cin >> x;
        int ans = lower_bound(a+1, a+n+1, x) -a;
        cout << ans-1 << endl;
    }
}
#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int n,x;
    int a[100009];
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    if (x > a[n-1]) {
        cout << -1 << endl;
        return 0;
    }
    
    int l = 0;
    int r = n-1;
    int m;
    while (true) {
        m = (l+r)/2;
        if (x <= a[m]) {
            
            r = m-1;
        }
        else {
            if (a[m+1] > x) {
                cout << m +1 << endl;
                return 0;
            }
            l = m+1;
        }
    }
}
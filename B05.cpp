#include <bits/stdc++.h>
using namespace std;
 
int main() {
    // cout << "-------" << endl;
    int n;
    int a[100009];
    int q;
    int b[100009];
    cin >> n;
    for (int i = 0; i < n; i++) {
        if (i==0) cin >> a[i];
        else {
            int x;
            cin >> x;
            a[i] = a[i-1] + x;
        }
        // cout << i << ":" << a[i] << endl;
    }
    
    
    cin >> q;
    for (int i = 0; i < q; i++) {
        int l,r;
        cin >> l >> r;
        int count;
        if (l >= 2) count = a[r-1] - a[l-2];
        else count = a[r-1];
        // cout << count << endl;

        if (count > ((r-l+1) -count)) cout << "win" << endl;
        else if (count < ((r-l+1) -count)) cout << "lose" << endl;
        else if (count == ((r-l+1) -count)) cout << "draw" << endl;
    }
    
}
#include <bits/stdc++.h>
using namespace std;
 
long long n, k;
long long a[100009];

bool check(long long x) {
    long long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += x/a[i];
    }
    if (sum >= k) return true;
    else return false;
}
int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    long long Left = 1, Right = 1000000000;
    while (Left < Right) {
        // cout << Left << " " << Right << endl;
        long long mid = (Left + Right) / 2;
        bool ans = check(mid);
        if (ans) Right = mid;
        else Left = mid + 1;
    }

    cout << Left << endl;
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
 

int main() {
    int n;
    cin >> n;
    int k;
    cin >> k;
    int a[100009];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int ruiseki[100009];
    ruiseki[0] = 0;
    for (int i = 1; i <= n; i++) {
        ruiseki[i] = a[i] + ruiseki[i-1];
    }

    for (int i = 1; i <= n; i++) {
        cout << ruiseki[i] << " ";
    }
    cout << endl;

    int kotae[100009];
    for (int i = 0; i < 100009; i++) {
        kotae[i] = i-1;
    }
    int mae = 0;
    for (int i = 1; i <= n; i++) {
        kotae[i] = mae;
        while (true){
            if ((ruiseki[kotae[i]+1] - ruiseki[i]) <= k) {
                kotae[i] += 1;
            }
            else {
                mae = kotae[i];
                break;
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        cout << i << ":" << kotae[i] << endl;
    }


}
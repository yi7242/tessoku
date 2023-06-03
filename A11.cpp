#include <bits/stdc++.h>
using namespace std;
 
int a[100009];

int main() {
    int n,x;
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }


    int left, right, mid;
    left = 0;
    right = n-1;
    while (true) {
        mid = (left+right)/2;
        if (a[mid] > x) right = mid -1;
        else if (a[mid] < x) left = mid + 1;
        else {
            cout << mid+1 << endl;
            return 0;
        }
    }
}
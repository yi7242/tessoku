#include <bits/stdc++.h>
// #include <unistd.h>
using namespace std;
 
int n;
double x;
bool check(double t) {
    double a = pow(t,3) + t;
    if (a >= n) return true;
    else return false;
}

int main() {
    cin >> n;
    double left = 0, right = n;
    while (abs(right-left) > 0.001) {
        // cout << left << " " << right << endl;
        double mid = (left + right) / 2;
        bool ans = check(mid);
        if (ans) right = mid;
        else left = mid;        
    }
    cout << left << endl;

    return 0;
}
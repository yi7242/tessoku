#include <bits/stdc++.h>
using namespace std;
 

stack<int> work[2009];
priority_queue<int> income;
int main() {
    long long count = 0;
    int n,d;
    cin >> n >> d;
    for (int i = 0; i < n; i++) {
        int x,y;
        cin >> x >> y;
        work[x].push(y);
    }

    for(int i = 1; i <= d; i++) {
        while (!work[i].empty()) {
            int p = work[i].top();
            work[i].pop();
            income.push(p);
        }
        if (!income.empty()) {

            count += income.top();
            income.pop();
        }
    }
    cout << count << endl;

}
#include <bits/stdc++.h>
using namespace std;

int main() {
    bool res = false;
    int a,b;
    cin >> a >> b;
    for (int i = a; i <= b; i++) {
        if (100%i == 0) {
            res=true;
        }
    }
    
    if (res) cout << "Yes" << endl;
    else cout<<"No"<<endl;
}
#include <bits/stdc++.h>
using namespace std;

vector<int> G[100009];
int n,m;
stack<int> s;
bool visited[100009];

bool dfs(int pos) {
    visited[pos] = true;
    s.push(pos);
    if (pos == (n-1)) {
        stack<int> s2;
        while (!s.empty()) {
            s2.push(s.top());
            s.pop();
        }
        while (!s2.empty()) {
            cout << s2.top()+1 << " ";
            s2.pop();
        }
        cout << endl;
        return true;
    }
    for (int i = 0;i < G[pos].size(); i++) {
        int nex = G[pos][i];
        if (visited[nex] == false) {
            bool x = dfs(nex);
            if (x) return true;
        }
    }
    s.pop();
    return false;
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a,b;
        cin >> a >> b;
        G[a-1].push_back(b-1);
        G[b-1].push_back(a-1);
    }

    for (int i = 0; i < n; i++){
        visited[i] = false;
    }

    bool ans = dfs(0);
    return 0;
}
from collections import defaultdict

d = defaultdict(set)
n = int(input())
s = []
s.append(input())
s.append(input())
for i in range(n - 1):
    now = s[0][i]
    migi = s[0][i + 1]
    if now != migi:
        d[now].add(migi)
        d[migi].add(now)
    sita = s[1][i]
    if now != sita:
        d[now].add(sita)
        d[sita].add(migi)
print(d)

n,m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))
count = 0
for i in range(n):
    if c[i] in d:
        count += p[d.index(c[i])+1]
    else:
        count += p[0]
print(count)
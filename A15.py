import bisect
n = int(input())
a = list(map(int, input().split()))
choose = sorted(set(a))
b = []
for i in range(n):
    x = bisect.bisect(choose, a[i])
    b.append(x)
print(*b)
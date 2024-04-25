def Division(a, b, m):
    return (a * pow(b, m - 2, m)) % m


n, r = map(int, input().split())
m = 1000000007
a = 1
for i in range(1, n + 1):
    a = (a * i) % m
b = 1
for i in range(1, r + 1):
    b = (b * i) % m
for i in range(1, n - r + 1):
    b = (b * i) % m
print(Division(a, b, m))

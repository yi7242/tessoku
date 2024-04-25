def Division(a, b, m):
    return (a * pow(b, m - 2, m)) % m


def ModdedComb(n, r, m):
    a = 1
    for i in range(1, n + 1):
        a = (a * i) % m
    b = 1
    for i in range(1, r + 1):
        b = (b * i) % m
    for i in range(1, n - r + 1):
        b = (b * i) % m
    return Division(a, b, m)


import math

h, w = map(int, input().split())
print(ModdedComb(h + w - 2, w - 1, 10**9 + 7))

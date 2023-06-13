def checkallsum(hairetsu):
    hairetsu2 = []
    # print(2**len(hairetsu))
    for i in range(2**len(hairetsu)):
        count = 0
        l = []
        for j in range(len(hairetsu)):
            if ((i >> j) & 1):
                count += hairetsu[j]
        hairetsu2.append(count)
    return hairetsu2

n,k = map(int, input().split())
a = list(map(int, input().split()))
first = sorted(a[:n//2])
second = sorted(a[n//2:])
# print(first)
# print(second)
l1 = checkallsum(first)
l2 = set(checkallsum(second))
# print(l1)
# print(l2)
for x in l1:
    if (k-x) in l2:
        print("Yes")
        exit()
print("No")

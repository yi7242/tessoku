n = int(input())
p = list(map(int, input().split()))

sp = sorted(p)
l1 = []
l2 = []
while sp != p:
    cantb = True
    for i in range(n-2):
        if p[i+2] < p[i]:
            cantb = False
            depo = p[i]
            p[i] = p[i+2]
            p[i+2] = depo
            l1.append("B")
            l2.append(i)
    if not cantb:
        continue
    else:
        for i in range(n-1):
            if p[i+1] < p[i]:
                depo = p[i]
                p[i] = p[i+1]
                p[i+1] = depo
                l1.append("A")
                l2.append(i)
                continue
# print(p)
print(len(l1))
for i in range(len(l1)):
    print(l1[i], l2[i]+1)
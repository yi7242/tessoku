n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a)
q = int(input())


def binary(x):
    left = 0
    right = len(a)-1
    while right >= left:
        mid = (left+right)//2
        print(x, mid, a[mid])
        # print(mid)
        if x > a[mid]:
            left = mid+1
        elif x < a[mid]:
            right = mid-1
        else:
            return mid
    return -1

for i in range(q):
    print(binary(int(input())))

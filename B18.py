n = int(input())
count = 0
for i in range(n):
    if input() == "For":
        count += 1
if n // 2 < count:
    print("Yes")
else:
    print("No")

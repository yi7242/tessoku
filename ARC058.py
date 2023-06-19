def get_maxabove(x):
    if x not in d:
        return str(x)
    else:
        return get_maxabove() + str(min(gyakud))


n,k = map(int, input().split())
s = "0" + str(n)
d = list(map(int, input().split()))
gyakud = []
for i in range(10):
    if i not in d:
        gyakud.append(i)

now = 0
while now < len(s):
    if now == 0 and s[0] == '0':
        now += 1
    elif 
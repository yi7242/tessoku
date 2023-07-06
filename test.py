from collections import deque
def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

snuke = list("snuke")

#探索関数：ゴールしたらそのときの位置・移動数を返す
def Maze(start):
    #スタート位置（x座標, y座標, 移動回数）をセット
    pos = deque(start)

    while len(pos) > 0:#探索可能ならTrue
        x, y, index = pos.popleft() #リストから探索する位置を取得

        #ゴールについた時点で終了
        if x == h and y == w:
            return True

        #探索済みとしてセット
        maze[x][y] = 9
        # print(x,y, index)
        next = (index + 1)%5
        #現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
        if maze[x-1][y] == next:#左
            pos.append([x-1, y, next])
        if maze[x+1][y] == next:
            pos.append([x+1, y, next])
        if maze[x][y-1] == next:
            pos.append([x, y-1, next])
        if maze[x][y+1] == next:
            pos.append([x, y+1, next])

    return False
h,w= map(int, input().split())
maze = []
maze.append([9]*(w+2))
for i in range(h):
    s = list(input())
    x=[9]
    for j in s:
        x.append(my_index(snuke, j, 9))
    x.append(9)
    maze.append(x)
maze.append([9]*(w+2))
# print(maze)
start = [[1, 1, 0]]     #スタート位置

result = Maze(start)  #探索

if result:
    print("Yes")
else:
    print("No")
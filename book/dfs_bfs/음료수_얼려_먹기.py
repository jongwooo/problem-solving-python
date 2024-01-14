n, m = map(int, input().split())
tray = [list(map(int, input())) for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]


def dfs(y, x):
    if 0 <= y < n and 0 <= x < m:
        if tray[y][x] == 0:
            tray[y][x] = -1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                dfs(ny, nx)
            return True
    return False


cnt = 0
for y in range(n):
    for x in range(m):
        if dfs(y, x):
            cnt += 1
print(cnt)

from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]


def bfs(y, x):
    queue = deque([])
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 1:
                queue.append((ny, nx))
                maze[ny][nx] = maze[y][x] + 1
    return maze[n - 1][m - 1]


print(bfs(0, 0))

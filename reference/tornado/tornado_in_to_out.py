def tornado_in_to_out():
    global arr
    x, y = len(arr) // 2, len(arr) // 2
    num = 0
    dist = 1
    d = 0
    move = 0
    while True:
        for _ in range(dist):
            dx, dy = dirs[d]
            nx = x + dx
            ny = y + dy
            if (nx, ny) == (0, -1):
                return
            num += 1
            arr[nx][ny] = num
            x, y = nx, ny
        move += 1
        d = (d + 1) % 4
        if move == 2:
            dist += 1
            move = 0


arr = [[0] * 5 for _ in range(5)]
dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
tornado_in_to_out()
for a in arr:
    print(*a)

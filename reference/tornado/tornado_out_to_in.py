def tornado_out_to_in(n):
    if n == 1:
        return [[1]]
    new_arr = [[0] * n for _ in range(n)]
    x, y = 0, 0
    d = 0
    for i in range(1, n ** 2 + 1):
        new_arr[x][y] = i
        if d == 0:
            y += 1
            if y == n - 1 or new_arr[x][y + 1] != 0:
                d = 1
        elif d == 1:
            x += 1
            if x == n - 1 or new_arr[x + 1][y] != 0:
                d = 2
        elif d == 2:
            y -= 1
            if y == 0 or new_arr[x][y - 1] != 0:
                d = 3
        elif d == 3:
            x -= 1
            if x == 0 or new_arr[x - 1][y] != 0:
                d = 0
    return new_arr


arr = tornado_out_to_in(5)
for a in arr:
    print(*a)

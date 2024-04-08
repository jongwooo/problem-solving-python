def rotate_90(sx, sy, length):
    global arr, new_arr
    for x in range(sx, sx + length):
        for y in range(sy, sy + length):
            ox = x - sx
            oy = y - sy
            rx = oy
            ry = length - ox - 1
            new_arr[sx + rx][sy + ry] = arr[x][y]
    for x in range(sx, sx + length):
        for y in range(sy, sy + length):
            arr[x][y] = new_arr[x][y]


arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 7 for _ in range(7)]
rotate_90(2, 2, 3)
for a in arr:
    print(*a)

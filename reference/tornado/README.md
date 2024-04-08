# 나선형 배열 (토네이도, 달팽이)

## 안에서 밖으로

```python
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
```

## 밖에서 안으로

```python
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
```

# 회전

## `zip()`을 활용한 회전

> [!NOTE]
> 정사각형, 직사각형 모두 적용 가능하다.

**시계 방향 90 (= 반시계 방향 270)**

```python
def rotate_90(arr):
    return list(map(list, zip(*arr[::-1])))


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_arr = rotate_90(arr)
for row in new_arr:
    print(*row)
```

**시계 방향 180 (= 반시계 방향 180)**

```python
def rotate_180(arr):
    return [a[::-1] for a in arr[::-1]]


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_arr = rotate_180(arr)
for row in new_arr:
    print(*row)
```

**시계 방향 270 (= 반시계 방향 90)**

```python
def rotate_270(arr):
    return list(map(list, reversed(list(zip(*arr)))))


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_arr = rotate_270(arr)
for row in new_arr:
    print(*row)
```

## 인덱스 규칙 찾아서 회전

### 정사각형

**시계 방향 90 (= 반시계 방향 270)**

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(arr)
new_arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_arr[i][j] = arr[n - j - 1][i]
for row in new_arr:
    print(*row)
```

**시계 방향 180 (= 반시계 방향 180)**

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(arr)
new_arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_arr[i][j] = arr[n - i - 1][n - j - 1]
for row in new_arr:
    print(*row)
```

**시계 방향 270 (= 반시계 방향 90)**

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(arr)
new_arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_arr[i][j] = arr[j][n - i - 1]
for row in new_arr:
    print(*row)
```

## 직사각형

**시계 방향 90 (= 반시계 방향 270)**

```python
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m = len(arr)
n = len(arr[0])
new_arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        new_arr[i][j] = arr[m - j - 1][i]
for row in new_arr:
    print(*row)
```

**시계 방향 180 (= 반시계 방향 180)**

```python
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m = len(arr)
n = len(arr[0])
new_arr = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        new_arr[i][j] = arr[m - i - 1][n - j - 1]
for row in new_arr:
    print(*row)
```

**시계 방향 270 (= 반시계 방향 90)**

```python
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m = len(arr)
n = len(arr[0])
new_arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        new_arr[i][j] = arr[j][n - i - 1]
for row in new_arr:
    print(*row)
```

## 부분 회전

```python
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
```

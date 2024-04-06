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

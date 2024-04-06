# itertools

> [!NOTE]
> 삼성 SW 역량테스트에서는 [itertools](https://docs.python.org/ko/3/library/itertools.html) 라이브러리를 사용할 수 없다.
> 따라서 백트래킹으로 직접 구현해야 한다.

## 순열 (itertools.permutations)

```python
def permutations(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutations(n, new_arr + [arr[i]])
            visited[i] = False


arr = [1, 2, 3, 4]
visited = [False] * len(arr)
permutations(2, [])
```

## 중복 순열 (itertools.product)

```python
def product(n, new_arr):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])


arr = [1, 2, 3, 4]
product(2, [])
```

## 조합 (itertools.combinations)

```python
def combinations(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i + 1)


arr = [1, 2, 3, 4]
combinations(2, [], 0)
```

## 중복 조합 (itertools.combinations_with_replacement)

```python
def combinations_with_replacement(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations_with_replacement(n, new_arr + [arr[i]], i)


arr = [1, 2, 3, 4]
combinations_with_replacement(2, [], 0)
```

# 정렬 알고리즘

- 정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다.

## 선택 정렬

- 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복**한다.

### 선택 정렬 소스코드 (Python)

```python
arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)
```

### 선택 정렬의 시간 복잡도

- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같다:
  - N + (N - 1) + (N - 2) + ... + 2
- 이는 (N ^ 2 + N - 2) / 2로 표현할 수 있는데, 빅 오 표기법에 따라서 O(N ^ 2)라고 작성한다.

## 삽입 정렬

- 처리되지 않은 데이터를 하나씩 골라 **적절한 위치에 삽입**한다.
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작한다.

### 삽입 정렬 소스코드 (Python)

```python
arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break
print(arr)
```

### 삽입 정렬의 시간 복잡도

- 삽입 정렬의 시간 복잡도는 O(N ^ 2)이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용된다.
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
  - 최선의 경우 O(N)의 시간 복잡도를 가진다.

## 퀵 정렬

- 기준 데이터를 설정하고 그 **기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**이다.
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나이다.
- 병합 정렬과 더불어 대부분의 프로그래밍 언어에서 졍렬 라이브러리의 근간이 되는 알고리즘이다.
- 가장 기본적인 퀵 정렬은 **첫 번째 데이터를 기준 데이터(Pivot)로 설정**한다. 피벗을 기준으로 데이터 묶음을 나누는 작업을 **분할**이라고 한다.

### 퀵 정렬이 빠른 이유: 직관적인 이해

- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(N log N)을 기대할 수 있다.
  - 너비 * 높이 = N * log N = N log N

### 퀵 정렬의 시간 복잡도

- 퀵 정렬은 평균의 경우 O(N log N)의 시간 복잡도를 가진다.
- 하지만 최악의 경우 O(N ^ 2)의 시간 복잡도를 가진다.

### 퀵 정렬 소스코드: 일반적인 방식 (Python)

```python
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
```

### 퀵 정렬 소스코드: 파이썬의 장점을 살린 방식

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
print(quick_sort(arr))
```

## 계수 정렬

- 특정한 조건이 부합할 때만 사용할 수 있지만 **매우 빠르게 동작하는** 정렬 알고리즘이다.
  - 계수 정렬은 **데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때** 사용 가능하다.
  - 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N + K)를 보장한다.

### 계수 정렬 소스코드 (Python)

```python
arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
cnt = [0] * (max(arr) + 1)
for i in range(len(arr)):
    cnt[arr[i]] += 1
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=' ')
```

### 계수 정렬의 복잡도 분석

- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N + K)이다.
- 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다.
  - 데이터가 0과 999,999로 단 2개만 존재하는 경우 비효율적이다.
- 계수 정렬은 **동일한 값을 가지는 데이터가 여러 개 등장할 때** 효과적으로 사용할 수 있다.
  - 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적이다.

## 정렬 알고리즘 비교하기

- 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(N log N)을 보장하도록 설계되어 있다.

**선택 정렬**

- 평균 시간 복잡도: O(N ^ 2)
- 공간 복잡도: O(N)
- 특징: 아이디어가 매우 간단하다.

**삽입 정렬**

- 평균 시간 복잡도: O(N ^ 2)
- 공간 복잡도: O(N)
- 특징: 데이터가 거의 정렬되어 있을 때는 가장 빠르다.

**퀵 정렬**

- 평균 시간 복잡도: O(N log N)
- 공간 복잡도: O(N)
- 특징: 대부분의 경우에 가장 적합하며, 충분히 빠르다.

**계수 정렬**

- 평균 시간 복잡도: O(N + K)
- 공간 복잡도: O(N + K)
- 특징: 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작한다.

---

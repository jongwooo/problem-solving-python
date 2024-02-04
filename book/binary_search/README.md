# 이진 탐색

[메인으로 돌아가기](../../README.md)

- 순차 탐색: 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인**하는 방법이다.
- 이진 탐색: 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법이다.
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.

## 이진 탐색의 시간 복잡도

- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 **연산 횟수는 log2 N에 비례**한다.
- 예를 들어 초기 데이터의 개수가 32개일 때, 이상적으로 1단계를 거치면 16개 가량의 데이터만 남는다.
  - 2단계를 거치면 8개 가량의 데이터만 남는다.
  - 3단계를 거치면 4개 가량의 데이터만 남는다.
- 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(log N)을 보장한다.

## 이진 탐색 소스코드: 재귀적 구현 (Python)

```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n, target = map(int, input().split())
array = sorted(list(map(int, input().split())))
result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
```

## 이진 탐색 소스코드: 반복문 구현 (Python)

```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = map(int, input().split())
array = sorted(list(map(int, input().split())))
result = binary_search(array, target, 0, n - 1)
if result is None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
```

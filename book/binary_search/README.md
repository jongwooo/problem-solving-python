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

## 파이썬 이진 탐색 라이브러리

- `bisect_left(a, x)`: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환한다.
- `bisect_right(a, x)`: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환한다.

### 값이 특정 범위에 속하는 데이터 개수 구하기

```python
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))  # 값이 4인 데이터 개수 출력
print(count_by_range(a, -1, 3))  # 값이 [-1, 3] 범위에 있는 데이터 개수 출력
```

## 파라메트릭 서치 (Parametric Search)

- **파라메트릭 서치**란 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법이다.
  - 예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **이진 탐색을 이용하여 해결**할 수 있다.

---

**<문제>** 떡볶이 떡 만들기 : 문제 설명

- 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총
  길이는 절단기로 잘라서 맞춰준다.
- 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
- 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기의 높이를 15cm으로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm이 될 것이다. 잘린 떡의 길이는 차례대로 4, 0,
  0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
- 손님이 왔을 때 요청한 총 길이가 M일 때 **적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램**을 작성하라.

**<문제>** 떡볶이 떡 만들기 : 문제 조건

- 입력 조건: 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다(1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000). 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의
  총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 작은 양의 정수 또는 0이다.
- 출력 조건: 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

**<문제>** 떡볶이 떡 만들기 : 답안 예시 (Python)

```python
n, m = map(int, input().split())
heights = list(map(int, input().split()))
start = 0
end = max(heights)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for h in heights:
        if h > mid:
            total += h - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
```

---

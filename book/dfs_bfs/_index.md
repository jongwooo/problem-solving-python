# DFS/BFS

- 탐색(Search)이란 많은 양의 데이터 중에서 **원하는 데이터를 찾는 과정**을 말한다.
- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다.

## 스택 자료구조

- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조이다.
- **입구와 출구가 동일한 형태**로 스택을 시각화할 수 있다.

### 스택 구현 예제 (Python)

```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)  # 최하단 원소부터 출력
```

## 큐 자료구조

- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조이다.
- 큐는 **입구와 출구가 모두 뚫려 있는 터널과 같은 형태**로 시각화 할 수 있다.

### 큐 구현 예제 (Python)

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 출력
```

## 재귀 함수

- **재귀 함수**란 자기 자신을 다시 호출하는 함수를 의미한다.
  - 단순한 형태의 재귀 함수 예제:
    - '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력한다.
    - 어느 정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력된다.
      ```python
      def recursive_function():
          print('재귀 함수를 호출합니다.')
          recursive_function()
      ```

### 재귀 함수의 종료 조건

- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.
  - **종료 조건**을 포함한 재귀함수 예제
    ```python
    def recursive_function(i):
        # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
        if i == 100:
          return
        print(f'{i}번째 재귀함수에서 {i +1}번째 재귀 함수를 호출합니다.')
        recursive_function(i + 1)
        print(f'{i}번째 재귀함수를 종료합니다.')
    ```

### 팩토리얼 구현 예제

- n! = 1 x 2 x 3 x ... x (n - 1) x n
- 수학적으로 0!과 1!의 값은 1이다.

```python
  # 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)
```

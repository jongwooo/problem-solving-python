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

### 최대공약수 계산 (유클리드 호제법) 예제

- 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있다.
- **유클리드 호제법**
  - 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하자.
  - 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
- 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있다.

```python
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
```

### 재귀 함수 사용의 유의사항

- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
  - 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 한다.
  - 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
  - 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
  - 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임이 쌓인다.
    - 그래서 스택을 사용해야 할 때 구현상 **스택 라이브러리 대신 재귀 함수를 이용**하는 경우가 많다.

## DFS (Depth-First Search)

- DFS는 **깊이 우선 탐색**이라고도 부르며 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘**이다.
- DFS는 **스택 자료구조(혹은 재귀함수)를 이용**하며, 구체적인 동작은 다음과 같다:
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

### DFS 소스코드 예제 (Python)

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)
```

## BFS (Breadth-First Search)

- BFS는 **너비 우선 탐색**이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**이다.
- BFS는 **큐 자료구조**를 이용하며, 구체적인 동작 과정은 다음과 같다:
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드와 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

### DFS 소스코드 예제 (Python)

```python
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)
```

---

**<문제>** 음료수 얼려 먹기 : 문제 설명

- N x M 크기의 얼음 틀이 있다. 구명이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

**<문제>** 음료수 얼려 먹기 : 문제 조건

- 입력 조건: 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다(1 <= N, M <= 1,000). 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다. 이때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1이다.
- 출력 조건: 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

**<문제>** 음료수 얼려 먹기 : 답안 예시 (Python)

```python
n, m = map(int, input().split())  
tray = [list(map(int, input())) for _ in range(n)]  
dy = [0, 0, 1, -1]  
dx = [-1, 1, 0, 0]  
  
  
def dfs(y, x):  
    if 0 <= y < n and 0 <= x < m:  
        if tray[y][x] == 0:  
            tray[y][x] = -1  
            for i in range(4):  
                ny = y + dy[i]  
                nx = x + dx[i]  
                dfs(ny, nx)  
            return True  
    return False  
  
cnt = 0  
for y in range(n):  
    for x in range(m):  
        if dfs(y, x):  
            cnt += 1  
print(cnt)
```

---

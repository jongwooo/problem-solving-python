# 최단 경로 알고리즘

[메인으로 돌아가기](../../README.md)

- 최단 경로 알고리즘은 **가장 짧은 경로를 찾는 알고리즘**을 의미한다.
- 다양한 문제 상황:
  - 한 지점에서 다른 한 지점까지의 최단 경로
  - 한 지점에서 다른 모든 지점까지의 최단 경로
  - 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 그래프에서 **노드**로 표현한다.
- 지점 간 연결된 도로는 그래프에서 **간선**으로 표현한다.

## 다익스트라 최단 경로 알고리즘 개요

- **특정한 노드**에서 출발하여 **다른 모든 노드**로 가는 최단 경로를 계산한다.
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작한다.
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류된다.
  - **매 상황에서 가장 비용이 적은 노드를 선택**해 임의의 과정을 반복한다.

## 다익스트라 최단 경로 알고리즘

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3번과 4번을 반복한다.

- 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있다.
- 처리 과정에서 더 짧은 경로를 찾으면 갱신한다.

## 다익스트라 알고리즘의 특징

- 그리디 알고리즘: **매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택**해 임의의 과정을 반복한다.
- 단계를 거치며 **한 번 처리된 노드의 최단 거리는 고정**되어 더 이상 바뀌지 않는다.
  - **한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해**할 수 있다.
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장된다.
  - 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 한다.

## 다익스트라 알고리즘: 간단한 구현 방법 (Python)

- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 **매 단계마다 1차원 테이블의 모든 원소를 순차 탐색**한다.

```python
import heapq


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for destination, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[destination]:
                distance[destination] = new_cost
                heapq.heappush(queue, (new_cost, destination))


INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dijkstra(start)
for i in range(1, n + 1):
    print('INFINITY' if distance[i] == INF else distance[i])
```

## 플로이드 워셜 알고리즘 개요

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다.
- 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 **거쳐 가는 노드를 기준으로 알고리즘을 수행**한다.
  - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다.
- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장한다.
- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형에 속한다.

## 플로이드 워셜 알고리즘

- 각 단계마다 **특정한 노드 k를 거쳐 가는 경우를 확인**한다.
  - a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 검사한다.

**점화식**

```text
Dab = min(Dab, Dak + Dkb)
```

## 플로이드 워셜 알고리즘: 구현 방법 (Python)

```python
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print('INFINITY' if graph[a][b] == INF else graph[a][b])
```

---

# 기타 그래프 이론

[메인으로 돌아가기](../../README.md)

## 서로소 집합

- 서로소 집합(Disjoint Sets)란 공통 원소가 없는 두 집합을 의미한다.

## 서로소 집합 자료구조

- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- 서로소 집합 자료구조는 두 종류의 연산을 지원한다
  - **합집합(Union)** : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산이다
  - **찾기(Find)** : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산이다
- 서로소 집합 자료구조는 **합치기 찾기(Union Find) 자료구조**라고 불리기도 한다
- 여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같다
  1. 합집합(Union) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다
     a. A와 B의 루트 노드 A', B'를 각각 찾는다
     b. A'를 B'의 부모 노드로 설정한다
  2. 모든 합집합(Union) 연산을 처리할 때까지 1번의 과정을 반복한다

## 서로소 집합 자료구조: 연결성

- 기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없다
  - 루트 노드를 찾기 위해 부모 테이블을 계속 확인해서 거슬러 올라가야 한다

## 서로소 집합 자료구조:  기본적인 구현 방법 (Python)

```python
def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    union(a, b)
# 각 원소가 속한 집합 출력하기
for i in range(1, v + 1):
    print(find(i))
# 부모 테이블 내용 출력하기
for i in range(1, v + 1):
    print(parent[i])
```

## 서로소 집합 자료구조: 경로 압축

- 찾기(Find) 함수를 최적화하기 위한 방법으로 경로 압축을 이용할 수 있다
  - 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신한다
- 경로 압축 기법을 적용하면 각 노드에 대하여 찾기(Find) 함수를 호출한 이후에 해당 노드의 루트 노드가 바로 부모 노드가 된다
- 기본적인 방법에 비하여 시간 복잡도가 개선된다

## 서로소 집합 자료구조:  경로 압축 (Python)

```python
def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
```

## 서로소 집합을 활용한 사이클 판별

- 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다
- 사이클 판별 알고리즘은 다음과 같다
  1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인한다
     1. 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(Union) 연산을 수행한다
     2. 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것이다
  2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다

```python
def find(x):
    if parent[x] != x:
        parent[x] =  find(parent[x])
    return parent[x]


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
cycle = False
for _ in range(e):
    a, b = map(int, input().split())
    if find(a) == find(b):
        cycle = True
        break
    else:
        union(a, b)
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
```

## 신장 트리

- 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다
  - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 **트리**의 조건이기도 하다

## 크루스칼 알고리즘

- 대표적인 **최소 신장 트리 알고리즘**이다
- 그리디 알고리즘으로 분류된다
- 구체적인 동작 과정은 다음과 같다
  1. 간선 데이터를 비용에 따라 **오름차순으로 정렬**한다
  2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다
      1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다
      2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다
  3. 모든 간선에 대하여 2번의 과정을 반복한다

```python
def find(x):
    if parent[x] != x:
        parent[x] =  find(parent[x])
    return parent[x]


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edges = []
result = 0
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
# 간선을 비용순으로 정렬
edges.sort()
# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find(a) != find(b):
        union(a, b)
        result += cost
print(result)
```

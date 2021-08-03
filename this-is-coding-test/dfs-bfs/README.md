# DFS/BFS
## 꼭 필요한 자료구조
- 탐색  
많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 자료구조  
데이터를 표현하고 관리하고 처리하기 위한 구조  

### 스택
먼저 들어온 데이터가 나중에 나가는 `선입후출` 구조이다
### 큐
먼저 들어온 자료가 먼저 나가는 `선입선출` 구조이다

```
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.popleft()
queue.popleft()
```

### 재귀함수
자기 자신을 다시 호출하는 함수

```
def factorial_interative(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result
	
def factorial_recursive(n):
	if n<=1:
		return 1
	return n*factorial_recursive(n-1)
```

재귀 함수의 장점은 소스코드가 더 간결하다는 점이다.

## DFS (깊이 우선 탐색)
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다. 노드와 간선으로 표현되며, 두 노드가 간선으로 연결되어 있다면 두 노드는 인접하다고 표현한다.

> 인접행렬 : 2차원 배열로 그래프의 연결관계를 표현하는 방식  
> 인접리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식  

  
- 인접행렬 방식  
```
INF = int(1e9)

graph = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
]
```      
- 인접 리스트 방식   
```
graph = [[] for in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
grahp[2].append((0, 5))
```  
 
[dfs 파이썬 코드](./dfs.py)

## BFS (너비 우선 탐색)

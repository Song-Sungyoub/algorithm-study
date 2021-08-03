from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
	for j in range(m):
		if graph[i][j] == 0:
			graph[i][j] = 1
			queue = deque([(i,j)])
			while queue:
				v1, v2 = queue.popleft()

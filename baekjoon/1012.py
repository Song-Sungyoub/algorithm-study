t = int(input())

def dfs(graph,m,n,x,y):
	if x <= -1 or x >= m or y <= -1 or y >= n:
		return False, graph
	if graph[x][y] == 1:
		graph[x][y] = 0
		graph = dfs(graph, m, n, x-1, y)[1]
		graph = dfs(graph, m, n, x, y-1)[1]
		graph = dfs(graph, m, n, x+1, y)[1]
		graph = dfs(graph, m, n, x, y+1)[1]
		return True, graph
	return False, graph
		

answer = []
for _ in range(t):
	m,n,k = map(int, input().split())
	graph = [[0]*n for _ in range(m)]
	for _ in range(k):
		x, y = map(int, input().split())
		graph[x][y] = 1
	
	result = 0
	for i in range(m):
		for j in range(n):
			if dfs(graph,m,n, i,j)[0] == True:
				result += 1
	answer.append(result)

for a in answer:
	print(a)

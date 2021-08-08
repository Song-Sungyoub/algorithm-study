n,m,v = map(int, input().split())

graph = [[] * n]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)

print(graph)


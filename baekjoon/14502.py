n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]!=1:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    
for i in range(n):
    for j in range(m):
        for i2 in range(i+1, n):
            for j2 in range(j+1, m):
                for i3 in range(i2+1, n):
                    for j3 in range(j2+1, m):
                        for
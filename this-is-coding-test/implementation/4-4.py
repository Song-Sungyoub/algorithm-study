n, m = map(int, input().split())
x,y,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

go = [(-1,0), (0,1), (1,0), (0,-1)]
cnt = 1
graph[x][y] = 1
while True:	
	for _ in range(4):
		dx = x+go[d][0]
		dy = y + go[d][1]
		if graph[dx][dy] == 0:
			x, y = dx, dy
			graph[dx][dy] = 1
			cnt += 1
			break
		d = (d-1)%4
	else:
		break		
print(cnt)
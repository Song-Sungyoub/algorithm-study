from collections import deque

n = int(input())
l = list(range(1, n+1))
queue = deque(l)
cnt = 0
while len(queue)>1:
	if cnt%2==0:
		queue.popleft()
	else:
		queue.append(queue.popleft())
	cnt += 1
print(queue[0])
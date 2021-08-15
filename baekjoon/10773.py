import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
	m = int(input())
	if m == 0:
		l.pop()
	else:
		l.append(m)

print(sum(l))
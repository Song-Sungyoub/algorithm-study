n = int(input())
words = []

for _ in range(n):
	words.append(input())

words = list(set(words))
long = max(list(map(len, words)))

for j in range(1, long+1):
	for ang in sorted([i for i in words if len(i) == j]):
		print(ang)

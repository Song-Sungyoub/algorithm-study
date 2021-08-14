import sys
input = sys.stdin.readline

memory = [False]*100000

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())

for i in n_list:
	memory[i]=True

for i in map(int, input().split()):
	if memory[i]:
		print(1)
	else:
		print(0)
for _ in range(int(input())):
	duo = [i for i in list(map(int, input().split())) if i%2==0]
	print(sum(duo), min(duo))
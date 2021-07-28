n = list(map(int,list(input())))
l = len(n)

if sum(n[:l//2]) == sum(n[l//2:]):
	print("LUCKY")
else:
	print("READY")
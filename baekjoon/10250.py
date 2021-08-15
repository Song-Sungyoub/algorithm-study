t = int(input())

for _ in range(t):
	h,w,n = map(int, input().split())
	ang = n%h
	ang2 = n//h+1
	if ang == 0:
		ang = h
		ang2 -= 1
	print(f'{ang}{ang2:0>2}')
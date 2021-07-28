n = input()

x, y = ord(n[0]) - ord('a') + 1, int(n[1])

moving = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
cnt = 0

for mx, my in moving:
	mx = x+mx
	my = y+my
	if 0<mx<=8 and 0<my<=8:
		cnt += 1
		
print(cnt)
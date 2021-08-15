import math
'''
a,b,v = map(int, input().split())
total = 0
day = 0
go = [-1*b, a]
while total<v:
	day+=1
	total += go[day%2]

print(math.ceil(day/2))
'''

'''
a,b,v = map(int, input().split())

ans = math.ceil(v/(a-b))
if (a-b)*(ans-1)+a<v:
	ans-=1
print(ans)
'''

a,b,v = map(int, input().split())
print(math.ceil(((v-a)/(a-b)+1)))
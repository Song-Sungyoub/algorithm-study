n, k = map(int, input().split())

count = 0

for t in range(n+1):
    for m in range(60):
        for s in range(60):
            if str(k) in f'{str(t):0>2}{str(m):0>2}{str(s):0>2}':
                count+=1
                
print(count)

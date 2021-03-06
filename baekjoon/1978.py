def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in a:
	if i in prime_list(max(a)+1):
		cnt+=1

print(cnt)
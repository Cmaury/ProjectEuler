def Answer(n):
	primes = []
	primes.append(range (2, n+1))
	for i, j in primes:
		while i < j:
			if j % i == 0:
				primes.remove [j]
			i += 1
	return max(primes)
print Answer(100)

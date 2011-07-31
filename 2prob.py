multiples = []
a = 0
b = 1
while a < 4000000:
	a, b = b, a + b
	if (a % 2) == 0:
                multiples.append(a)
print sum(multiples)

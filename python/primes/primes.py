def primesOf(i):
	p = []
	for d in range(2, i + 1):
		while i % d == 0:
			p.append(d)
			i = i / d
	return p


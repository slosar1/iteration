def gcd(a,b):
	if a > b:
		r = a % b
		if r == 0 :
			return b
		else:
			return gcd(b, r)
	if a < b:
		r = b% a
		if r == 0 :
			return a
		else:
			return gcd(a, r)
print(gcd(18,2))

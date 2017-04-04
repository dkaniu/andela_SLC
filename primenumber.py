def find_primes(n):
	#sanitize input
	is_prime = True
	if n <= 0:
		is_prime = False
	if(n == 2):
		is_prime = True
	if(isinstance(n, int)):
		for prime_num in range(2, n+1):
			if n % prime_num == 0:
				is_prime = False
		if is_prime:
			return n

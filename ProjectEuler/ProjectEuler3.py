# Python program to print the largest prime factor

import math

# A function to print the largest prime factor of number n
def primeFactors(n):
    a = 0 
	# Print the number of two's that divide n
    while n % 2 == 0:
        a = 2
        n = n / 2
		
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
		
		# while i divides n , print i ad divide n
        while n % i== 0:
            a = i
            n = n / i
			
	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		a = n
    
    print a
# Driver Program to test above function

n = 17000000000000
primeFactors(n)

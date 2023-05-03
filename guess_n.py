# guess a Number 1 =< N <= 100

import random
r = random.randint(1, 100)
while True:
	n = input('guess a Number: ')
	n = int(n)
	if n == r:
		print('Bingo!')
		break
	elif n > r:
		print('the number is smaller')
	elif n < r:
		print('the number is bigger')
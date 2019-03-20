#while Loop
# count = 10
# while count <= 20:
	# print('count is equal to: ', count)
	# if count == 15:
		# break	
	# count = count + 1
	
#peoples = ['John', 'Jane', 'Paul', 'Moses', 'Joseph', 'Kennedy', 'Steve']

# for person in peoples:
	# print('this person is called', person)

# for i in range(len(peoples)):
	# print('the person is :', peoples[i])

# for i in range(1, 20):
	# print('Multiples of 13', i * 13)
	# print('Multiples of 12', i * 12)
	# if i == 10:
		# break
		
# def greetings(name = 'John'):
	# for name in peoples:
		# print('Hello', name)
	# return	

# greetings('jane')

# def calc (num, mult):
	# multiple = num * mult
	# print (multiple)
		
	# return

# calc(30, 1300)

#str = 'I am Kennedy'	

# print (type(str))
# print(str.count('n'))
# print(str.startswith('I'))
# print(str.endswith('dy'))
# print(str.replace('Kennedy', 'John'))
# print(len(str))
# print(str.swapcase())
# print(str.capitalize())
# print(str.split())

# u, v, x, y = 0, 0, 100, 30
# while x > y:
 # u = u + y
 # x = x - y
 # if x < y + 2:
	 # v = v + x
	 # x = 0
 # else:
	 # v = v + y + 2
	 # x = x - y - 2
# print(u, v, x, y)

# def factorial (n):
	# if type(n) != type(1):
		# print ("Factorial is only defined for integers.")
		# return -1
	# elif n < 0:
		# print ("Factorial is only defined for positive integers.")
		# return -1
	# elif n == 0:
		# return 1
	# else:
		# return n * factorial(n-1)

# print(factorial(997))
#a 
# def countdown(n):
	# while n > 0:
		# print (n)
		# n = n-1
	# print ("Blastoff!")
# print(countdown(17))
# def sequence(n):
	# while n != 1:
		# print (n)
		# if n%2 == 0: # n is even
			# n = n/2
		# else: # n is odd
			# n = n*3+1
# print(sequence(6))

import math
#arithmetric sequence
# x = 1.0
# while x < 10.0:
	# print (x, '\t', math.log(x))
	# x = x + 1.0
#geometric sequence
# x = 1.0
# while x < 65536.0:
	# print (x, '\t', math.log(x)/math.log(2.0))
	# x = x * 2.0
# def printMultiples(i, high):
	# i = 1
	# while i <= high:
		# print (i*i, '\t', i*i)
		# i = i + 1
	# print()
# def printMultTable(high):
	# i = 1
	# while i <= high:
		# printMultiples(i, i)
		# i = i + 1
# print(printMultTable(7))
import random
# for i in range(662806682880, 847602496465):
	# x = random.random()
# print (x)
# def randomList(n):
	# s = [0] * n
	# for i in range(n):
		# s[i] = random.random()
	# return s
# print(randomList(5))
def inBucket(list, low, high):
	count = 0
	for num in list:
		if low < num < high:
			count = count + 1
	return count
numBuckets = 8
buckets = [0] * numBuckets
bucketWidth = 1.0 / numBuckets
for i in range(numBuckets):
	low = i * bucketWidth
	high = low + bucketWidth
	buckets[i] = inBucket(list, low, high)
	print (buckets)
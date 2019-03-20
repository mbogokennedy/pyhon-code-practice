import math
import os
import random
import re
import sys
# sock Merchant Challenge
def sockMerchant(n, ar):
    ar = sorted(ar)
    count = 0
    i = 0
    
    while i < n - 1:
        if ar[i] == ar[i + 1]:
            count += 1
            i += 2
        else:
            i += 1
    
    return count
# counting valley Challenge	
def countingValleys(n, s):
    ls = list(s)
    seeLevel = 0
    valley = 0
    for i in ls:
        if i == 'U':
            seeLevel += 1
        else:
            if seeLevel == 0:
                valley +=1
            seeLevel-= 1
    return valley 
	
# compare Triplets	
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice+=1
        elif a[i] < b[i]:
            bob+=1
    return "%d%d" % (sa, sb)
	
# simple sum
def simpleSum(ar):
    s = sum(ar)
	return s
# big sum
def aVeryBigSum(ar):
    s = sum(ar)
	return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# diagonal difference

def diagonalDifference(arr):
    diff = sum(row[i]- row[-i-1] for i, row in enumerate(arr))
    return abs(diff)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Complete plusMinus function.
def plusMinus(arr):
  arr = [0 if i is 0 else i/abs(i) for i in arr]
  for x in map(arr.count, [1, -1, 0]):
      print (round(x/n, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

# Complete jumpingOnClouds function.
def jumpingOnClouds(c):
    count = 0
    i = 0
    c.insert(n,0)
    while i < n-1:
        i += (c[i+2] == 0)+1
        count+= 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

# Complete repeatedString function.
def repeatedString(s, n):
    if len(s)==1:
        if s == "a":
                return n
        else:
            return 0
    ls = s.count("a")
    c = math.floor(n/len(s))
    res = ls *c
    res += s[:(n%len(s))].count("a")
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
# reversed array

def reverseArray(a):
    return arr[::-1]
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
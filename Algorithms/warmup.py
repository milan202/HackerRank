#Solve Me First
def solveMeFirst(a,b):
    return a+b
  

num1 = input()
num2 = input()
res = solveMeFirst(num1,num2)
print res

#Simple Array Sum
import sys
def simpleArraySum(n, ar):
    sum =0
    for i in ar:
        sum = sum+i
    return sum
        
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print result

#Compare the Triplets
import sys

def simpleArraySum(n, ar):
    sum =0
    for i in ar:
        sum = sum+i
    return sum
        
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print result

#A Very Big Sum

def aVeryBigSum(n, ar):
    sum = 0 
    for i in range(0,n):
        sum = sum+ar[i]
    return sum

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
#Question1
#Test with single input

randNum = int(raw_input("Enter a number:"))

#returning the Nth fibonacci number
def solution1(n):
    num1 = 0
    num2 = 1
    num3 = 0
    sum = 0

    if(n==0):
        return num1
    elif(n==1):
        return num2
    elif(n==2):
        return num1+num2
    else:
        for i in xrange(2,n+1):
            num3=num1+num2
            num1=num2
            num2=num3
        return num2

print(solution1(randNum))

#Sum of the even fibonacci numbers in a given range
def solution(n):
    num1 = 0
    num2 = 1
    num3 = 0
    sum = 0

    if(n==0):
        return num1
    else:
       while(randNum>(num1+num2)):
            num3=num1+num2
            num1=num2
            num2=num3
            if(num2%2==0):
                sum= sum+num2
    print sum
        

solution(randNum)

#Submission for multiple inputs

import sys

def solution(n):
    num1 = 0
    num2 = 1
    num3 = 0
    sum = 0

    if(n==0):
        return num1
    else:
       while(n>(num1+num2)):
            num3=num1+num2
            num1=num2
            num2=num3
            if(num2%2==0):
                sum= sum+num2
    print sum

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    solution(n)
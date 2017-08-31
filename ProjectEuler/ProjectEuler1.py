#Question1
#Test with single input

#this solution is more of a brute force method. It is iterative thus takes hell lot of time.
#We can convert it to a O(1) solution as follows
randNum = int(raw_input("Please enter the number: "))

def solution1(i):
    total = 0
    for n in range (1,i):
        if ((n%3 == 0) or (n%5 ==0)):
            # print n
            total = total + n
    print total

solution1(randNum)

#this is a O(1) solution and if you are using python 3
""" take i=100, the number of multiples of 3 from 0 to 100 is 33 
    (100-1)/3 gives number 33.
    the sum of mutiples are 3+6+9+ .. + 99
    you can wite this as,
    3[1+2+3+..+33] = 3[1+33]/2 """

"""if you are using puthon 3 use // operator indtead of / operator
https://stackoverflow.com/questions/183853/in-python-2-what-is-the-difference-between-and-when-used-for-division
"""
def solution2(i):
    #mX = number of mutiples of number X in the range of 0 to i
    m3 = (i-1)/3
    m5 = (i-1)/5
    m15 = (i-1)/15

    sum = 3*(m3*(m3+1)/2) + 5*(m5*(m5+1)/2) - 15*(m15*(m15+1)/2)
    print sum

solution2(randNum)

#Submission for multiple inputs

import sys
def solution(i):
    #mX = number of mutiples of number X in the range of 0 to i
    m3 = (i-1)/3
    m5 = (i-1)/5
    m15 = (i-1)/15

    sum = 3*(m3*(m3+1)/2) + 5*(m5*(m5+1)/2) - 15*(m15*(m15+1)/2)
    print sum
    
t = int(raw_input().strip())
for a in xrange(t):
    a = int(raw_input().strip())
    solution(a)

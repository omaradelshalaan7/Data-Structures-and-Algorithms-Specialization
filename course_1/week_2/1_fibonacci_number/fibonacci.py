# Uses python3
"""
Omar Adel Shalaan
"""
import math
def recursion_fib(n):
    if (n <= 1):
        return n
    return recursion_fib(n - 1) + recursion_fib(n - 2)

def for_fib(n):
    if n<=1:
        return n
    list=[0,1]
    for i in range(n-1):
        list.append(list[i]+list[i+1])
    return list.pop()
def fast_fib(n):
    return (int(((1/math.sqrt(5))*(((((1+math.sqrt(5))/2)**n))-(((1-math.sqrt(5))/2)**n)))))


n = int(input())
#print(recursion_fib(n))
#print(for_fib(n))
print(fast_fib(n))


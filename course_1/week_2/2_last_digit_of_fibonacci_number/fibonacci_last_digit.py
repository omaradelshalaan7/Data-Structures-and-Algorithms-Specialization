# Uses python3
"""
Omar Adel Shalaan
"""
import  math

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        temp=current %10
        current=(previous+current)%10
        previous=temp

    return current % 10
def fast_fib(n):
    return (int(((1/math.sqrt(5))*((((((1+math.sqrt(5)))/2)**n))-((((1-math.sqrt(5)))/2)**n))))%10)

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
    #print(fast_fib(n))

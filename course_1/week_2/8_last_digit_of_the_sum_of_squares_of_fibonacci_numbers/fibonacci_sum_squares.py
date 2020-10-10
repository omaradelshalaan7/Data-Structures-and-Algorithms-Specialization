# Uses python3
"""
Omar Adel Shalaan
"""
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    sum=1
    list=[0,1]
    count=n%60
    if count <= 1:
        return count

    for i in range(1,count):
        temp=(list[i-1]+list[i])%10
        list.append(temp)
        sum=(sum+(temp*temp)%10)%10
    return sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))

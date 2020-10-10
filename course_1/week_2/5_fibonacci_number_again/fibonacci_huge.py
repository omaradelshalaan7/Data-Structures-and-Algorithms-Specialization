# Uses python3
"""
Omar Adel Shalaan
"""
def sequences_periodic(m):
    if m<=1:
        return m
    list=[0,1]
    i=1
    while True:
        list.append((list[i-1]+list[i])%m)
        if list[i]==0 and list[i+1]==1:
            return len(list)-2
        i+=1

def for_fib(n):
    if n<=1:
        return n
    list=[0,1]
    for i in range(n-1):
        list.append(list[i]+list[i+1])
    return list.pop()

def get_fibonacci_huge_naive(n, m):
    s_p=sequences_periodic(m)
    x=n//s_p
    value=n-x*s_p
    return for_fib(value)%m


if __name__ == '__main__':
    n,m = map(int, input().split())
    print(get_fibonacci_huge_naive(n,m))

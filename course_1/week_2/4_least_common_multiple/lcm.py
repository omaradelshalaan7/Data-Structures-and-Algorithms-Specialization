# Uses python3
"""
Omar Adel Shalaan
"""
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l


def fast_lcm_naive(a, b):
    min_=min(a,b)
    for l in range(min_, a*b + 1,min_):
        if l % a == 0 and l % b == 0:
            return l

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(fast_lcm_naive(a, b))



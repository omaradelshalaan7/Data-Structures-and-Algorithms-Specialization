# Uses python3
"""
Omar Adel Shalaan
"""

def gcd_naive(a, b):
    current_gcd = 1
    n=0
    for d in range(2, min(a, b) + 1):
        n+=1
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    print(n)
    return current_gcd

def _gcd_naive(a, b):
    current_gcd = 0
    n=0
    for d in range(a+b,0,-1):
        n+=1
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
                break
    print(n)
    return current_gcd

def fast_gcd(a,b):
    if b==0:
        return a    #### Takes about Log(ab) steps
    _a= a-(a//b)*b
    return fast_gcd(b,_a)
if __name__ == "__main__":
    a, b = map(int, input().split())
    #print("*",gcd_naive(a, b))
    #print("*",_gcd_naive(a, b))
    print(fast_gcd(a,b))

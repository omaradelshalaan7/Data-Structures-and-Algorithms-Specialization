# Uses python3
"""
Omar Adel Shalaan
"""
def get_change(m):
    n_10=0
    n_5=0
    if  m>=10:
        n_10= m//10
        m   =  m-(n_10*10)
    if m>=5:
        n_5 =  m//5
        m   =  m - (n_5*5)
    return m+n_10+n_5

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

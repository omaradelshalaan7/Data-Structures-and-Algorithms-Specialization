# python3
"""
Omar Adel Shalaan
"""
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
def max_pairwise_product_fast(numbers):
    numbers.sort()
    numbers.reverse()
    return numbers[0]*numbers[1]



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    #print(max_pairwise_product(input_numbers))
    print(max_pairwise_product_fast(input_numbers))
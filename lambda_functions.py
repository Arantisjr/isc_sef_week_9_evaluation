from functools import reduce

def multy_func(arr):
    num_square = map(lambda x: x * 2, arr)  # Doubles each element
    squares = filter(lambda x: x % 2 == 0, num_square)  # Keeps even numbers 
    total = reduce(lambda x, y: x + y, squares)  # Fixed variable nam
    return total

print(multy_func([1, 2, 3, 4, 5]))  
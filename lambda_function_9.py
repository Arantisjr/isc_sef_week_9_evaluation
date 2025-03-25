from functools import reduce

def multy_func(arr):
    num_square = map(lambda x: x * 2, arr)  
    squares = filter(lambda x: x >10 , num_square) 
    total = reduce(lambda x, y: x * y, squares)  
    return total

print(multy_func([3,6,9,12,15]))  
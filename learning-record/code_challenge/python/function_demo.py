import string
import random

def calculate(int1, int2):
    return int1 + int2

def substr(str):
    return str[0:8]

def range_character():
    str = ''
    characters = string.ascii_letters + string.digits
    for _ in range(6):
       str += random.choice(characters) 
    return str    

def generate_short_code(length=6):
    """Generate a random short code."""
    characters = string.ascii_letters + string.digits
    print(characters)
    return ''.join(random.choice(characters) for _ in range(length))

# def product_of_array(arr):
#     for i in arr:
#         print(f"for i in arr: {i}")
#     n = len(arr)    
#     for i in range(n):
#         print(f"for i in range(4): {arr[i]}")    

# arr = [11, 22, 33, 44]
# product_of_array(arr)   

# print(calculate(2, 3))
# print(substr('abcdefghijk'))
# print(range_character())
# print(generate_short_code())


def operateArray(arr):
    n = len(arr)
    result = [1]*n
    # print(result)
    for i in range(n):
        print(i)
        # result[i] = 10*i
        # result[i] *= 10
        result[i] = result[i]*10
    return result

arr = [0,1,2,3]
print(operateArray(arr))
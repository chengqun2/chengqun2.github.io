import string
import random
from typing import List

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
        print(result[i])
        # result[i] = 10*i
        # result[i] *= 10
        result[i] = result[i]*10
    return result

map_demo = {}
def mapTest(key, value):
    map_demo[key] = value
    return map_demo

def isInMap(map_demo):
    if 'code' in map_demo:
      return True  
    return

# arr = [0,1,2,3]
# print(operateArray(arr))

result = mapTest('code', '001')
print(result)
# print(result['code'])
result2 = isInMap(map_demo)
print(result2)


def maxTest(num1: int, num2: int):
    return max(num1, num2)
print(maxTest(19,91))


def divisionTest(num1: int, num2: int) -> string:
    quotient = num1 // num2
    remainder = num1 % num2
    return str(quotient) + "..." + str(remainder)
print(divisionTest(31, 10))

def nodeTest(l1: List, l2: List):
    while l1 and l2:
        print(l1, l2)
        del l1[0] 
        del l2[0]
l1 = [1,2,3]
l2 = [4,5]
nodeTest(l1, l2)

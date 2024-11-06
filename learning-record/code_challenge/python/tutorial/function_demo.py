import string
import random
from typing import List

def calculate(int1, int2):
    return int1 + int2

def concatStrings():
    return " ".join(["hello","my","friend"])
print("concatStrings:", concatStrings())    

def substr(str):
    return str[0:8]
print('substr:', substr('abcdefghijklmn'))

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

def sum_of_array(arr):
    for i in arr:
        print(f"for i in arr: {i}")
    n = len(arr)    
    for i in range(n):
        print(f"for i in range(4): {arr[i]}")    
    sum = 0    
    if n > 0: 
        for i in arr:
            print(f"for i in arr: {i}")    
            sum += i
    return sum        
arr = [1, 2, 3, 4]
sum = sum_of_array(arr)   
print(f"sum: {sum}")
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
    print(f"quotient: {num1} // {num2} = {quotient}")
    float_quotient = num1 / num2
    print(f"float_quotient: {num1} / {num2} =  {float_quotient}")
    remainder = num1 % num2
    print(f"remainder: {num1} % {num2} =  {remainder}")
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

def reverseTest(list: List):
    list.reverse()
    return list
ll = [1,2,5,4,3,'s','a']
print(reverseTest(ll))


def compareTriplets(a, b):
    # Write your code here
    arr = [0, 0]
    left = 0
    right = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            left += 1
        elif a[i] < b[i]:  
            right +=1
    arr[0] = left
    arr[1] = right
    return arr    
a = [1,2,4]
b = [2,1,3]
print(compareTriplets(a, b))

# The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter
def rangeDemo(n):
    # Write your code here
    result = 1
    for i in range(n, 0, -1):
        print(f"rangeDemo: {i}")
rangeDemo(5)

def extraLongFactorials(n):
    print(f"extraLongFactorials: {n}")
    if n == 1:
        return 1
    return n * extraLongFactorials(n-1)
print(extraLongFactorials(5))


def list_map_demo():
    list = []
    map1 = {"code":"code001","name":"name001"}
    map2 = {"code":"code002","name":"name002"}
    list.append(map1)
    list.append(map2)
    # print(f"list: {list}")
    for map in list:
        map['code'] = "newcode-" + map['code']
        print(f"map: {map}")
        # print(f"map['code']: {map['code']}")
    for _ in list:
        print(f"_: {_}")
    for _ in range(len(list)):
        print(f"_: {list[_]['code']}")
list_map_demo()


def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        # print(f"fizzBuzz->i: {i}")
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0 and i%5!=0: 
            print("Fizz")
        elif i%3!=0 and i%5==0:     
            print("Buzz")
        else:
            print(i)   
fizzBuzz(15)

def reverse_words_and_swap_cases(sentence: string):
    # Step 1: Split the string into words
    words_array = sentence.split()
    # Step 2: Reverse the order of words
    reversed_words_array = words_array[::-1]
    reversed_words = " ".join(reversed_words_array)
    # Step 3: Join the words back into a single string and swap the case
    reversed_and_swapped = reversed_words.swapcase()
    return reversed_and_swapped
print(reverse_words_and_swap_cases("aWESOME is cODING"))

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(f"words: {words}")
new_word_without_the = []
new_word_without_the_lengths = []
for word in words:
      if word != "the":
          new_word_without_the.append(word)
          new_word_without_the_lengths.append(len(word))
print(new_word_without_the)
print(new_word_without_the_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
for number in numbers:
     if number > 0 :
          newlist.append(number)
print(newlist)

arr = [0, 1, 2, 3]
print(arr.pop())
print(arr)

strs = ['aa','ac','ad','abe','ab']
print(f'sorted strs: {sorted(strs)}')

strs = ["flower","flow","flight"]
first = strs[0]
last = strs[-1]
print(f"last: {strs[-1]}")

arr2 = [0, 1, 2, 3, 4]
for x in range(len(arr2)):
     if arr2[x] == 1:
          continue
     print(f"x: {x}")

nums = [-1,0,1,2,-1,-4]
print(f"nums.sort-->return None: {nums.sort}")
print(f"sorted(nums): {sorted(nums)}")
nums.append(100)
print(nums)

str = 'I, love, python'
print(f"str.split(','): {str.split(',')}")

# print(list)
# print(list())
# print(type(list))
# print(type(list()))
print(type(10))
print(type('10'))
print(type([]))
print(type({}))
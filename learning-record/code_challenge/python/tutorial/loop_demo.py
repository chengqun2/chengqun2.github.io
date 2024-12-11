for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
    print(f"n: {n}")

s = "ABCDEFG"
for a, b in zip(s, s[1:]):    
    print(f"a: {a}, b: {b}")


strs = ["flower","flow","fly"]
first = strs[0]
last = strs[-1]
print(min(len(first),len(last)))

str = 'ABCDEFG'
for i in range(len(str)):
    print(f"str: {str[i]}")

start, end = 0, 5
while start < end:
    print(f"start: {start}")
    start +=1

for i in range(5, 0, -1):
    print(f"range: {i}")

s = 'abcabcbb'
for right, c in enumerate(s):
    print(f"enumerate-> right: {right}, c: {c}")
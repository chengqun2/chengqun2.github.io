sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
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
# 4. Write a function named contain_string that takes 
# as a parameter a list of strings and the target string, 
# and returns a list of the strings from the original list 
# that contain the target string. Use a list comprehension. 

# Sample input: ['cats', 'tacks', 'scat', 'stack'], 'cat'
# Expected output: ['cats', 'scat']

input = ['cats', 'tacks', 'scat', 'stack']
word = "cat"


def contain_string(a, b):
  return [a for a in a if b in a]

# "cats" in input[range(0,len(input))]

#contain_string(input, word)
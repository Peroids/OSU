# 3. Write a function named rev_string_list that takes as a 
# parameter a list of strings and returns a list that contains 
# the reverse of each of those strings. Use a list comprehension.

# Sample input: ["Wayne", "Katie", "Daryl", "Dan"]
# Expected output: ['enyaW', 'eitaK', 'lyraD', 'naD']

input = ["Wayne", "Katie", "Daryl", "Dan"]

def rev_string_list(i):
  return [a[::-1] for a in input]
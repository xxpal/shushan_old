"""
Demo programming of Chapter 5
"""


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# More on Lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))    # Find next banana starting a position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
fruits.sort()
print(fruits)
print(fruits.pop())
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Using Lists as Queues
# Use collections.deque which was designed to have fast appends and pops from both ends.
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")   # Terry arrives
queue.append("Graham")  # Graham arrives
print(queue.popleft())  # The first to arrive now leaves
print(queue.popleft())  # The second to arrive now leaves
print(queue)            # Remaining queue in order of arrival
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# List Comprehensions
# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is the result of
# some operations applied to each member of another sequence or iterable,
# or to create a subsequence of those elements that satisfy a certain condition.
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression
# in the context of the for and if clauses which follow it.
# The following listcomp combines the elements of two lists if they are not equal.
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vec2 = [x*2 for x in vec]
print(vec2)

# filter the list to exclude negative numbers
vec3 = [x for x in vec if x >= 0]
print(vec3)

# apply a function to all the elements
vec4 = [abs(x) for x in vec]
print(vec4)

# call a method on each element
fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
vec5 = [weapon.strip() for weapon in fresh_fruit]
print(vec5)

# create a list of 2-tuples like (number, square)
vec6 = [(x, x**2) for x in range(6)]
print(vec6)

# flatten a list using a listcomp with two 'for'
vec7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec8 = [num for elem in vec7 for num in elem]
print(vec8)

# List comprehensions can contain expressions and nested functions:
from math import pi
pi_value = [str(round(pi, i)) for i in range(1, 6)]
print(pi_value)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transposed_matrix_1 = [[row[i] for row in matrix] for i in range(4)]
print(transposed_matrix_1)

# Equivalent example of the above snippets
transposed_matrix_2 = []
for i in range(4):
    transposed_matrix_2.append([row[i] for row in matrix])
print(transposed_matrix_2)

# Another equivalent example of the above snippets
transposed_matrix_3 = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix_3.append(transposed_row)
print(transposed_matrix_3)

# In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a great job for the use case above.
print(list(zip(*matrix)))
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
print(a)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Tuple
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuple may be nested
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable
# t[0] = 88888

# but Tuples can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print(v)

# Tuples with zero or one item
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Tuple packing and Sequence unpacking
t = 12345, 54321, 'hello!'
print(t)
x, y, z = t
print("x =", x, "y =", y, "z =", z)
# Sequence unpacking works for any sequence on the right-hand side
# Sequence unpacking requires there are as many variables on the left side
# of the equals sign as there are elements in the sequence
# Note: multiple assignment is really just a combination of tuple packing and sequence unpacking
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Sets
# A set is an unordered collection with no duplicate elements
# Curly braces or set() function can be used to create sets
# Use set() rather than {} to create an empty set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)    # show that duplicates have been removed

# fast membership testing
print('orange' in basket)
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)        # unique letters in a
print(b)        # unique letters in b
print(a - b)    # letters in a but not in b
print(a | b)    # letters in a or b or both
print(a & b)    # letters in both a and b
print(a ^ b)    # letters in a or b not both

# List comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# Dictionaries
# Dictionaries are indexed by keys, which can be any immutable type
# Strings and numbers can always be keys
# Tuples can be used as keys if they contain ONLY strings or numbers or tuples
# If a tuple contains any mutable object either directly or indirectly, it cannot be used as a key
# A dictionary is as a set of key:value pairs, where keys are unique (within one dictionary)
tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('sape' in tel)
print('jack' not in tel)

# The dict() constructor
tel_dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel_dict)

# dict comprehension
square_dict = {x: x**2 for x in (2, 4, 6)}
print(square_dict)

# If the keys are simple strings, it's easier to specify pairs using keyword arguments
tel_dict = dict(sape=4139, guido=4127, jack=4098)
print(tel_dict)
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''


# Looping techniques
# When looping through dictionaries,
# the key and corresponding value can be retrieved at the same time using the items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence,
# the position index and corresponding value can be retrieved at the same time using the enumerate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two sequences at the same time,
# the entries can be paired with the zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is you {0}? It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence in a forward direction,
# and then call the reversed() function
for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order,
# use the sorted() function which returns a new sorted list while leaving the source unaltered
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket):
    print(f, end=' ')
print()
for f in sorted(set(basket)):
    print(f, end=' ')
print()

# It's often simpler and safer to create a new list rather than to change it while looping over a list
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
''' ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
TO-DO
----- ----- ----- ----- ----- ----- ----- ----- ----- ----- '''
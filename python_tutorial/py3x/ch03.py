"""
Demo programming of Chapter 3
"""


# this is the first comment
spam = 1    # this is the second comment
            # ... and now a thrid!
text = "# This is not a comment because it's inside quotes."

print(2 + 2)
print(50 - 5*6)
print((50 - 5*6)/4)
print(8/5)  # division always returns a floating point number

print(17 / 3)  # classic division returns a float
print(17 // 3)  # floor division discards the fractional part
print(17 % 3)  # the % operator returns the remainder of the division
print(5 * 3 + 2)  # result * divisor + remainder

print(5 ** 2)  # 5 squared
print(2 ** 7)  # 2 to the power of 7

width = 20
length = 5 * 9
print(width * length)

print(4 * 3.75 - 1)


tax = 12.5 / 100
price = 100.5
print(price * tax)
print(price + price * tax)
print(round(price + price * tax), 2)

print('"Isn\'t", she said.')
s = 'First Line.\nSecond Line.'
print(s)

print('C:\some\name')   # here \n means new line
print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

print('py' 'thon')
print()

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

prefix = 'py'
# print(prefix 'thon')  # can't concatenate a variable and a string literal
print(prefix + 'thon')

word = 'python'
# There is no separate character type; a character is simply a string of size one
print(word[0])  # character in position 0
print(word[5])  # character in position 5

# slicing allows you to obtain substring
print(word[0:2])    # characters from position 0 (included) to 2 (excluded)
print(word[2:5])    # characters from position 2 (included) to 5 (excluded)

# Note: the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s
print(word[:2] + word[2:])
print(word[:4] + word[4:])

# An omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end

# Attempting to use an index that is too large will result in an error
# print(word[42])  # the word only has 6 characters

# However, out of range slice indexes are handled gracefully when used for slicing
print(word[4:42])
print(word[42:])

# Python strings cannot be changed — they are immutable.
# Therefore, assigning to an indexed position in the string results in an error
# word[0] = 'J'
# word[2:] = 'py'

# If you need a different string, you should create a new one
print('J' + word[1:])
print(word[:2] + 'py')

# The built-in function len() returns the length of a string
s = 'supercalifragilisticexpialidocious'
print(len(s))

squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
# List concatenation
print(squares + [36, 49, 64, 81, 100])

# List is mutable
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(cubes)
print(4 ** 3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

i = 256 * 256
print("The value of i is ", i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

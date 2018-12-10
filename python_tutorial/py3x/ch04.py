"""
Demo programming of Chapter 4
"""


''' ----- ----- ----- ----- -----
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero.')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
        print(words)

for i in range(5):
    print(i, end=' ')
print()

for i in range(5, 10):
    print(i, end=' ')
print()

for i in range(0, 10, 3):
    print(i, end=' ')
print()

for i in range(-10, -100, -30):
    print(i, end=' ')
print()
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# To iterate over the indices of a sequence, combine range() and len()
a = ['Mary', 'had', 'a', 'little', 'lamp']
for i in range(len(a)):
    print(i, a[i])
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
print(range(5))
print(list(range(5)))
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# The break statement breaks out of the innermost enclosing for or while loop.
# Loop statement may have an else clause
# It is executed when the loop terminates through exhaustion of the list (with for)
# or, when the condition becomes false (with while)
# but not when the loop is terminated by a break statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' equals ', x, ' * ', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, ' is a prime number')
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# The continue statement continues with the next iteration of the loop
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number ", num)
        continue
    print("Found a number ", num)
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# The pass statement does nothing.
# It can be used when a statement is required syntactically but the program requires no action.
while True:
    pass    # Busy-wait for keyboard interrupt (Ctrl+C)
# This is commonly used for creating minimal classes.
class MyEmptyClass:
    pass
# It is also commonly used as a place-holder for a function or conditional body when working on new code,
# allowing you to keep thinking at a more abstract level
def initlog(*args):
    pass    # Remember to implement this!
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# A function that writes the Fibonacci series to an arbitrary boundary
def fib(n):     # write Fibonacci series up to n
    """
    Print a Fibonacci series up to n.
    :param n: the boundary number
    :return: None
    """
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()


# Now, call the function we just defined
fib(2000)
# The execution of a function introduces a new symbol table used for the local variables of the function.
# More precisely, all variables assignments in a function store the value in the local symbol table,
# whereas, variable references first look in the local symbol table,
# then, in the local symbol tables of enclosing functions,
# then, in the global symbol table, and finally in the table of built-in names.
# Thus, global variables cannot be directly assigned a value within a function,
# unless named in a global statement, although they may be referenced.


# A function definition introduces the function name in the current symbol table.
# The value of the function name has a type that is recognized by the interpreter as a user-defined function.
# This value can be assigned to another name which can then also be used as a function.
# This severs as a general renaming mechanism
print(fib)
f = fib
f(100)


# Functions without a return statement return a value called None.
# Writing the value None is normally suppressed by the interpreter if it would be the only value written.
fib(0)
print(fib(0))
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
def fib2(n):    # return Fibonacci series up to n
    """
    Return a list containing the Fibonacci series up to n.
    :param n: the boundary number
    :return: a list
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # add number to the list
        a, b = b, a+b
    return result


f100 = fib2(100)    # call the function
print(f100)         # write the result
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# The most useful form is to specify a default value for one or more arguments.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response.')
        print(reminder)


# This function can be called in several ways
# 1) giving only the mandatory argument
ask_ok_return = ask_ok('Do you really want to quit?')
print(ask_ok_return)


# 2) giving one of the optional arguments
ask_ok_return = ask_ok('OK to overwrite the file?', 2)
print(ask_ok_return)


# 3) or even giving all arguments
ask_ok_return = ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
print(ask_ok_return)
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# The default values are evaluated at the point of function definition in the defining scope.
i = 5


def f(arg=i):
    print(arg)


i = 6
f()
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# The default value is evaluated only once
# This makes a difference when the default is a mutable object such as a list, dictionary, or instance of most classes
def f(a, my_list=[]):
    my_list.append(a)
    return my_list


print(f(1))
print(f(2))
print(f(3))


def f(a, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(a)
    return my_list


print(f(1))
print(f(2))
print(f(3))
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# Keyword argument
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    # accepts one required argument (voltage) and three optional arguments (state, action and type)
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# The function above can be called in any of the following ways
parrot(1000)                                            # 1 positional argument
parrot(voltage=1000)                                    # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')           # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')    # 1 positional argument, 1 keyword argument
# Invalid function call
# parrot()                                              # required argument missing
# parrot(voltage=5.0, 'dead')                           # non-keyword argument after a keyword argument
# parrot(110, voltage=220)                              # duplicate value for the same argument
# parrot(actor='John Cleese')                           # unknown keyword argument


# No argument may receive a value more than once
def function(a):
    pass


function(0, a=0)
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# When a final formal parameter of the form **name is present,
# it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter.
# This may be combined with a formal parameter of the form *name,
# which receives a tuple containing the positional arguments beyond the formal parameter list.
# Note: *name must occur before **name.
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# Arbitrary Argument List
# the least frequently used option is to specify that a function can be called with an arbitrary number of arguments.
# These arguments will be wrapped up in a tuple.
# Before the variable number of arguments, zero or more normal arguments may occur.
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# Normally, these variadic arguments will be last in the list of formal parameters.
# They scoop up all remaining input arguments that are passed to the function.
# Any formal parameters which occur after the *args parameter are 'keyword-only' arguments
# meaning that they can only be used as keywords rather than positional arguments.
def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# Unpacking Argument Lists
# If arguments are already in a list or tuple,
# but need to be unpacked for a function call requiring separate positional arguments,
# use *-operator to unpack the arguments out of a list or tuple.
print(list(range(3, 6)))    # normal call with separate arguments
args = [3, 6]
print(list(range(*args)))  # call with arguments unpacked from a list


# Use **-operator to unpack the keyword arguments out of dictionaries
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million",
     "state": "bleedin",
     "action": "VOOM"}
parrot(**d)
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# Lambda Expressions
# Use a lambda expression to return a function
def make_incrementor(n):
    return lambda x: x+n


f = make_incrementor(42)
print(f(0))
print(f(1))


# Use a lambda expression to pass a small function as an argument
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# Documentation Strings
# The first line should always be a short, concise summary of the object's purpose.
# The first line should begin with a capital letter and end with a period.
# If there are more lines in the documentation string, the second line should be blank,
# visually separating the summary from the rest of the description
# The following lines should be one or more paragraphs describing the object's calling conventions, side effects, etc.
def my_function():
    """Do nothing, but document it.

        No, really, it doesn't do anything.
    test line 2
test line 3
        test line 3
            test line 4
    """
    pass


print(my_function.__doc__)
----- ----- ----- ----- ----- '''


''' ----- ----- ----- ----- -----
# Function Annotations
# Function Annotations are completely optional metadata information about the types used by user-defined functions.
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f_return_value = f('spam')
print(f_return_value)
----- ----- ----- ----- ----- '''

def double(arg):
    print('Before:', arg)
    arg = arg * 2   # use this assignment won't change the value of arg, but if using arg *= 2 assignment, arg changes
    print('After:', arg)


def change(arg):
    print('Before:', arg)
    arg.append('More data')
    print('After:', arg)


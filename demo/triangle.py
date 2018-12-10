def print_right_triangle(row: int) -> None:
    print('---------- Right Triangle ----------')
    for i in range(row):
        print('*' * (i + 1))


def print_isosceles_triangle(row: int) -> None:
    print('---------- Isosceles Triangle ----------')
    for i in range(row):
        blanks = (row - 1) - i
        asterisks = i * 2 + 1
        print(' ' * blanks + '*' * asterisks + ' ' * blanks)


# A type cast has to be done here, due to the return value of input() is a string rather than an integer
height = int(input('Please input the height of the triangle:'))

print_right_triangle(height)
print_isosceles_triangle(height)

# Note: if no type cast here, an TypeError: 'str' object cannot be interpreted as an integer will be thrown out
# x = input('Please input the height of the triangle:')
# print_right_triangle(x)

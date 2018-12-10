# 用list或tuple作为函数参数
def calc1(numbers):
    result = 0
    for n in numbers:
        result = result + n * n
    return result


print('使用list或tuple作为函数参数')
print(calc1([1, 2, 3]))
print(calc1((1, 3, 5, 7)))


# 使用可变参数作为函数参数
def calc2(*numbers):
    result = 0
    for n in numbers:
        result = result + n * n
    return result


# 可变参数允许传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
print('使用可变参数作为函数参数')
print(calc2(1, 2, 3))
print(calc2(1, 3, 5, 7))

# 将存在的list或tuple转变成可变参数传递给函数
nums_list = [1, 2, 3]
nums_tuple = (1, 3, 5, 7)

print('将已存在的list或tuple中的元素作为参数传递给函数')
print(calc2(nums_list[0], nums_list[1], nums_list[2]))
print(calc2(nums_tuple[0], nums_tuple[1], nums_tuple[2], nums_tuple[3]))

print('将已存在的list或tuple直接转变成可变参数传递给函数')
print(calc2(*nums_list))
print(calc2(*nums_tuple))

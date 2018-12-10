def add1(a, b):
    return a + b


print(add1(5, 19))


def add2(a, b=10):
    return a + b


print(add2(1))
print(add2(a=1))
print(add2(1, 2))
print(add2(b=5, a=1))


total = 0    # 全局变量


def add3(a, b):
    total = a + b
    print('函数内的局部变量 total =', total)


# 调用add3()函数
add3(10, 20)
print('函数外的全局变量 total =', total)


# Lambda函数
add4 = lambda x, y: x + y
print('运行Lambda函数得到的值为：', add4(3, 6))


def get_info(name, age=18, gender='', hobby='成为一代大侠'):
    print('--------------------')
    print('姓名：', name)
    print('年龄：', age)
    print('性别：', gender)
    print('爱好：', hobby)
    print('--------------------')


# The function getInfo() can be called in any of the following ways
get_info('李逍遥')    # 1 positional argument
get_info(name='李逍遥')    # 1 keyword argument
get_info(name='赵灵儿', age=16)    # 2 keyword arguments
get_info(age=18, name='林月如')    # 2 keyword arguments
get_info('阿奴', 14, '女')    # 3 positional arguments
get_info(name='李逍遥', hobby='仗剑江湖为红颜')    # 1 positional argument, 1 keyword argument
# Invalid function call
# get_info()    # required argument missing
# get_info(name='李逍遥', 19)    # non-keyword argument after a keyword argument
# get_info('李逍遥', name='逍遥哥哥')    # duplicate value for the same argument
# get_info('李逍遥', sex='男')    # unknown keyword argument

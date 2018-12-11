import math
import random
import re


# ======================================================================
# 练习001：
# 水仙花数（Narcissistic number）：计算三位整数（100～999）的水仙花数。
# 水仙花数也称为自恋数、自幂数 或阿姆斯壮数（Armstrong number）。
# 它是指每一位的立方相加等于该数自己，如：153 = 1^3 + 5^3 + 3^3。
# ======================================================================
def armstrong_num() -> list:
    armstrong_nums = []     # 创建空列表用于保存所有的水仙花数

    for num in range(100, 1000):
        n3 = num // 100                 # 求百位上的数字
        n2 = (num - n3 * 100) // 10     # 求十位上的数字
        n1 = num - n3 * 100 - n2 * 10   # 求个位上的数字

        # 判断当前数字是否为水仙花数
        if (n3**3 + n2**3 + n1**3) == num:
            armstrong_nums.append(num)

    return armstrong_nums


# print(armstrong_num())


# ======================================================================
# 练习002
# 统计字符：从键盘输入一个字符串，统计该字符串中的字符。
# 该字符串当中包含几个大写字母，几个小写字母，几个数字，几个特殊符号。
# ======================================================================
def court_char(str_input: str = '') -> None:
    lower = []
    upper = []
    nums = []
    other = []

    for char in str_input:
        if char.isupper():
            upper.append(char)
        elif char.islower():
            lower.append(char)
        elif char.isnumeric():
            nums.append(char)
        else:
            other.append(char)

    print('您输入的字符串为：', str_input)
    print('该字符串共有{}个字符，包含了{}个大写字母，{}小写字母，{}个数字，{}个其它字符。'
          .format(len(str_input), len(upper), len(lower), len(nums), len(other)))
    return


# str_input = input('请输入一个字符串：')
# court_char(str_input)


# ======================================================================
# 练习003
# 组合问题：用1元纸币兑换1分，2分和5分的硬币，要求兑换总数为50枚。
# 问可以有多少种组合，每种组合对应1分，2分，5分分别是多少？
# ======================================================================
def exchange_cash(cash: int = 100, coins: int = 50) -> None:
    combs = []   # 不同兑换方式的组合保存在集合里

    for coin5 in range(cash//5 + 1, -1, -1):
        for coin2 in range(cash//2, -1, -1):
            for coin1 in range(cash, -1, -1):
                if (coin1 + coin2 + coin5 == coins) and (coin1 + 2 * coin2 + 5 * coin5 == cash):
                    combs.append({'1分': coin1, '2分': coin2, '5分': coin5})   # 将合适的兑换组合以字典的形式保存

    print('您一共有{}元现金，如需兑换{}个硬币，共有{}种兑换方案。具体如下：'.format(cash, coins, len(combs)))
    for item in combs:
        print(item)

    return


# exchange_cash()


# ======================================================================
# 练习004
# 九九乘法表：尝试用for循环完成九九乘法表输出。
# ======================================================================
def mul_table() -> None:
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{} x {} = {}\t'.format(j, i, i*j), end='')
        print()
    return

# mul_table()


# ======================================================================
# 练习005
# 数字处理：用户输入一个正整数，将该正整数倒序输出，并求各位数相加之和。
# 要求：不允许把用户输入的正整数处理为字符串，只能按照数值运算的规律完成本题。
# 扩展：完成此题后，进一步求小数的每位之和，如1234.567，并让该小数顺序按位输出。
# ======================================================================
def reverse_int(value: int = 0) -> None:
    print('您输入的正整数为：', value)

    # 首先需要判断输入的整数的位数
    flag = True         # 循环判断标志用于控制while循环
    digit = 0           # 记录输入的正整数的位数
    quotient = value    # 记录该正整除每次整除操作的商
    nums = []           # 顺序保存该正整数的每一位数字
    total = 0           # 记录改正整数每一位数字之和
    value_reverse = 0   # 记录输入的正整数所对应的倒序正整数

    # 用该整数整除10，同时计数器加一，循环此过程，直至整除的商为0。
    while flag:
        quotient //= 10
        digit += 1
        if quotient == 0:
            flag = False
            quotient = value

    # 确定整数位数后，提取每一位数字
    for i in range(digit-1, -1, -1):
        n = quotient // 10**i
        nums.append(n)
        quotient -= n * 10**i
        # print(quotient)
        # print(nums)
        total += n          # 通过累加得到所有位置上的数字之和

    # 生成输入的整数所对应的倒序正整数
    for j in range(len(nums)):
        value_reverse += nums[j] * 10**j

    print('该正整数所对应的倒序正整数为：', value_reverse)
    print('该正整数各位置上的数字之和为：', total)
    return


# value = int(input('请输入一个任意位数的正整数：'))
# reverse_int(value)


# ======================================================================
# 练习006
# 猜数字游戏：系统随机生成一个1000以内的正整数，用户每次输入一个数字，
# 如果输入数字大于系统随机生成的数字则提示"大了"，反之则提示"小了"，
# 相等则游戏结束，并提示"通关"并输出猜测的总次数。
# 提示：可以import random来生成随机数。
# ======================================================================
def guess_num() -> None:
    count = 0       # 猜数字计数器
    start = 1       # 生成随机数的最小值
    stop = 1000     # 生成随机数的最大值
    random_num = random.randint(start, stop)    # 生成并保存一个随机数

    # 猜数字判断
    while True:
        input_num = int(input('请输入一个{}以内的正整数：'.format(stop)))
        count += 1
        if input_num == random_num:
            print('通关！')
            break
        elif input_num > random_num:
            print('大了！请再试试！')
            continue
        else:
            print('小了！请再试试！')
            continue

    print('你一共猜了{}次.'.format(count))
    return


# guess_num()


# ======================================================================
# 练习007
# 字符串判断：从键盘输入一个字符串，判断该字符串是否可以被转换为一个有效的数字。
# 禁止使用Python自带方法完成
# ======================================================================
def is_numeric_str(input_str: str) -> None:
    is_numeric = False
    digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    dot = 0

    print('您输入的字符串为：{}'.format(input_str))

    for i in input_str:
        if i not in digits or dot > 1:
            print('该字符串不能转换成为一个有效数字')
            break
        elif i is '.':
            dot += 1
        else:
            is_numeric = True

    if is_numeric:
        print('该字符串可以转换成为一个有效的数字！')
    int('123')


is_numeric_str(input('请输入一串字符串：'))


# ======================================================================
# 练习008
# 定义一个列表，里面包含有20个左右的学生姓名，请实现随机点名的功能。
# ======================================================================
def call_the_roll(students: list) -> None:
    random_id = random.randint(0, len(students)-1)  # 生成并保存一个不大于学生总人数的随机数
    print('现在开始点名！==>', students[random_id])
    return


# students = ['张学友', '刘德华', '黎明', '郭富城', '周杰伦',
#             '王力宏', '蔡依林', '李宇春', '杨幂', '赵丽颖',
#             '王宝强', '谢霆锋', '李健', '沈腾', '马丽',
#             '郭德纲', '岳云鹏', '何炅', '谢娜', '蔡康永']
# call_the_roll(students)


# ======================================================================
# 练习009
# 给定一个列表，里面包含一批纯数字，按从小到大对其进行排序。
# 禁止使用Python自带的sort方法。
# ======================================================================
def bubble_sort_simple(nums: list) -> None:
    nums_len = len(nums)
    print('排序之前，列表为：', nums)

    for i in range(nums_len):
        for j in range(i+1, nums_len):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

    print('排序之后，列表为：', nums)
    return


# nums = [5, 3, 9, 11, 2, 0, 1, 1, 3, 8, 5, 5, 6, 6, 1, 7, 9, 1]
# bubble_sort_simple(nums)


# ======================================================================
# 练习010
# 请计算200以内的所有质数。
# 质数（prime number）又称素数，有无限个。
# 质数定义为在大于1的自然数中，除了1和它本身以外不再有其它因数。
# ======================================================================
def calc_prime_num(start: int = 2, stop: int = 200) -> None:
    prime_nums = []     # 用于存放每一个质数

    # 如果一个数能被2整除，则表明此数不是素数，反之是素数。
    # 改进算法：在一般领域，如果一个正整数n，不能被2到math.sqrt(n)之间的任一整数整除，则n为质数
    for num in range(start, stop):
        is_prime_num = True
        for n in range(start, num):    # for n in range(2, int(math.sqrt(num))+1)
            if num % n == 0:
                is_prime_num = False
                break
        if is_prime_num:
            prime_nums.append(num)

    print('{}到{}之间，一共有{}个质数。分别是：'.format(start, stop, len(prime_nums)))
    # 打印输出列表中所有的质数
    for i in range(len(prime_nums)):
        print(prime_nums[i], end='\t\t')
        if (i+1) % 10 == 0:
            print()

    return

# calc_prime_num()

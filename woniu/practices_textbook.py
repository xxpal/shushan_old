import random


# ================================================================================
# P289 - 练习题5
# 设定的总行数line可以随机修改，修改后仍然能够打印出line行的直角三角形和等腰三角形
# ================================================================================
# 打印直角三角形
def print_right_triangle(line: int = 0) -> None:
    # 如果未指定打印三角形的行数，则随机生成一个1~10的整数作为行数
    if line == 0:
        line = random.randint(1, 10)
    # 观察1：1行1颗星，2行2颗星，3行3颗星……以此类推，n行n颗星
    # 观察2：所有星号都左对齐就形成了一个直角三角形
    print('指定三角形的高为{}，打印该直角三角形如下：'.format(line))
    for i in range(line):
        print('*' * (i + 1))

    return


# 打印等腰三角形
def print_isosceles_triangle(line: int = 0) -> None:
    # 如果未指定打印三角形的行数，则随机生成一个1~10的整数作为行数
    if line == 0:
        line = random.randint(1, 10)
    # 观察1：1行1颗星，2行3颗星，3行5颗星……以此类推，n行2n-1颗星
    # 观察2：若共有n行，则第i行上有(n-1)-i个空格分别分布在星号的左右两边
    print('指定三角形的高为{}，打印该等腰三角形如下：'.format(line))
    for i in range(line):
        blanks = (line - 1) - i
        asterisks = i * 2 + 1
        print(' ' * blanks + '*' * asterisks + ' ' * blanks)

    return


# height = int(input('请输入需要打印的三角形的行数：'))
# print_right_triangle(height)
# print_isosceles_triangle(height)
print_right_triangle()
print_isosceles_triangle()


# ================================================================================
# P297 - 练习题
# 输入一个半径，计算出园的周长和面积
# ================================================================================
def calc_circle(radius=.0):
    pi = 3.14
    perimeter = (2 * pi * radius)
    area = pi * radius ** 2
    print('半径为{}的圆，周长是{}，面积是{}。'.format(radius, perimeter, area))

    return


# calc_circle(float(input('请输入圆的半径：')))


# ================================================================================
# P297 - 练习题2
# 输入两个数字a和b，计算出a的b次方，再除以b并取整后的值。
# ================================================================================
def calc_num(a: float = .0, b: float = .0) -> None:
    result = (a ** b)//b
    print('a = {}, b = {}, a**b//b = {}'.format(a, b, result))

    return


# a = float(input('请输入a的值：'))
# b = float(input('请输入b的值：'))
# calc_num(a, b)


# ================================================================================
# P297 - 练习题3
# 输入一个字符串，分别计算出'ab'出现的次数和'e'出现的次数。
# ================================================================================
def count_str(inputs: str) -> None:
    if len(inputs) == 0:
        inputs = 'abcdabkrajb'
        print('你输入的字符串为空，默认的字符串为：', inputs)
    ab_count = inputs.count('ab')
    e_count = inputs.count('e')
    print('"ab"在字符串{}中出现的次数为：{}'.format(inputs, ab_count))
    print('"e"在字符串{}中出现的次数为：{}'.format(inputs, e_count))

    return


# print(count_str.__doc__)
# count_str(input("请输入一个字符串："))
# print('\n' * 3)


# ================================================================================
# P297 - 练习题4
# 创建一个列表，将第三个元素更改为'third'，输出整个列表。
# ================================================================================
def print_list(list_input: list = []):
    print('修改之前，列表为：', list_input)
    list_input[2] = 'third'
    print('修改之后，列表为：', list_input)

    return


# print_list(list(input("请输入一个列表：")))


# ================================================================================
# P298 - 练习题5
# 将一个列表去重，并返回一个新的列表。
# ================================================================================
def dedup_list(list_input: list = []) ->None:

    if len(list_input) == 0:
        list_input = [44, 12, 55, 44, 12, 55, 33, 100]
        print('输入的列表为空，默认的列表为：', list_input)
    print('去重之前，列表为：', list_input)
    print('去重之后，列表为：', list(set(list_input)))   # 新生成的列表中元素顺序很可能变化，因为set()是无序的
    new_list = []
    for i in list_input:
        if i not in new_list:
            new_list.append(i)
    print('去重之后，列表为：', new_list)

    return


# dedup_list(list(input("请输入一个列表：")))


# ================================================================================
# P298 - 练习题6
# 给定一个成绩单（字典），找出最大最小值，并求出平均成绩，成绩自己定义。
# ================================================================================
def print_scores(trans: dict = {}) -> None:

    student_num = len(trans)
    student_best = set()
    student_worst = set()
    scores = list(trans.values())
    score_max = 0       # 最高分的初初始值应设为最小值
    score_min = 100     # 最低分的初始值值应设为最大值
    score_sum = 0
    score_average = 0

    # 找到最高分、最低分，计算总分、平均分
    for i in range(student_num):
        score_sum += scores[i]      # 循环累加可得总分
        # 两两循环比较，取较大值
        if scores[i] > score_max:
            score_max = scores[i]
        # 两两循环比较，取较小值
        if scores[i] < score_min:
            score_min = scores[i]
        # 所有成绩累加完成后，计算平均分
        if i == student_num - 1:
            score_average = score_sum/student_num

    # 更简便的方式：调用Python自带的max()和min()函数
    # score_max = max(transcript.values())
    # score_max = min(transcript.values())

    # 找到所有的最高分获得者和最低分获得者
    for k, v in trans.items():
        if v == score_max:
            student_best.add(k)
        if v == score_min:
            student_worst.add(k)

    print('现在公布考试成绩：')
    # 格式化打印所有学生的成绩，每行输出5个人的成绩
    count = 0
    for item in trans.items():
        print('%-16s' % str(item), end='')
        count += 1
        if count % 5 == 0:
            print()

    print('全班最高分：%.2f，获得者：%s' % (score_max, student_best))
    print('全班最低分：%.2f，获得者：%s' % (score_min, student_worst))
    print('全班平均分：%.2f' % score_average)

    return


# transcript = {'刘德华': 80, '张学友': 82, '周杰伦': 61, '王力宏': 97, '沈腾': 38,
#               '马丽': 42, '杨幂': 77, '赵丽颖': 75, '郭德纲': 66, '岳云鹏': 38,
#               '何炅': 96, '撒贝宁': 96, '谢娜': 49, '王宝强': 58, '蔡康永': 90}
# print_scores(transcript)

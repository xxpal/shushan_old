# ===============================================================================
# product: WoniuATM
# version: 1.0
# author: Leo
# updated: 12/09/2018
#
# 需求说明：
# 1、利用列表实现一个用户的注册功能。                            ==> Done
# 2、利用已注册的用户名和密码实现登录功能。                       ==> Done
#
# 基本要求：
# 利用两个列表，一个放用户名，一个放密码，下标位置对应上。           ==> Done
# 同时注册时，需要确认是否用户名已经存在，利用函数来组织代码。        ==> Done
#
# 扩展要求：
# 把两个列表减少为一个列表，完成同样的功能。列表中的列表。           ==> Todo
# 如果需要存第三个值，如：电话号码，请问怎么做比较好？              ==> Todo
# ===============================================================================


# 定义单独的列表，分别保存不同的用户属性
names = ['steve', 'bill', 'jack']
passwords = ['112233', 'abc', 'ma88']


def register() -> bool:
    """
    用户注册
    :return: 注册成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您的用户名：')
    index = check_user(name)
    status = False

    # 先判断用户名是否存在
    if index >= 0:
        print('>>> 该用户名已存在，请重新注册！')
    else:
        password = input('>>> 请输入您的密码：')
        names.append(name)  # 将姓名信息保存到用户列表
        passwords.append(password)  # 将密码信息保存到用户列表
        status = True
        print('>>> 注册成功！')

    return status


def login() -> bool:
    """
    用户登录
    :return: 登录成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您的用户名：')
    index = check_user(name)
    status = False

    # 先判断用户是否存在
    if index >= 0:
        password = input('>>> 请输入您的密码：')
        if passwords[index] == password:
            print('>>> 登录成功！')
            status = True
        else:
            print('>>> 密码错误，请重新登录！')
    else:
        print('>>> 该用户不存在，请先注册！')

    return status


def check_user(name: str) -> int:
    """
    检查用户名是否存在
    :param name: 用户名
    :return: 用户名存在则返回其所在列表中的index值，反之则返回-1
    """
    if name in names:
        return names.index(name)
    else:
        return -1


def enter() -> None:
    """
    入口程序，用于启动WoniuATM
    :return:
    """
    print('---------- 欢迎使用 WouniuATM 系统 ----------')


enter()     # 调用入口函数启动程序
register()  # 调用注册函数完成新用户注册
login()     # 调用登录函数完成系统登录

# ===============================================================================
# product: WoniuATM
# version: 1.2
# author: Leo
# updated: 12/10/2018
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
# 把两个列表减少为一个列表，完成同样的功能。列表中的列表。           ==> Done
# 如果需要存第三个值，如：电话号码，请问怎么做比较好？              ==> Todo
# ===============================================================================


# 定义单独的列表，分别保存不同的用户属性
# names = ['steve', 'bill', 'jack']
# passwords = ['112233', 'abc', 'ma88']
# tels = ['13966668888', '18899996666', '19977778888']

# 定义一个包含列表元素的列表，用于保存注册用户信息
users = [['steve', '112233', '13966668888'],
         ['bill', 'abc', '18899996666'],
         ['jack', 'ma88', '19977778888']]


def register() -> bool:
    """
    用户注册
    :return: 注册成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您的用户名：')
    index = check(name)
    status = False

    # 先判断用户名是否存在
    if index >= 0:
        print('>>> 该用户名已存在，请重新注册！')
    else:
        password = input('>>> 请输入您的密码：')
        tel = input('>>> 请输入您的电话号码：')
        user = [name, password, tel]    # 用户的属性值构成了一条用户记录
        users.append(user)              # 将用户记录加入到用户列表
        status = True
        print('>>> 注册成功！')

    return status


def login() -> bool:
    """
    用户登录
    :return: 登录成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您的用户名：')
    index = check(name)
    status = False

    if index >= 0:
        password = input('>>> 请输入您的密码：')
        if users[index][1] == password:
            print('>>> 登录成功！')
            status = True
        else:
            print('>>> 密码错误，请重新登录！')
    else:
        print('>>> 该用户不存在，请先注册！')

    return status


def check(name: str) -> int:
    """
    检查用户名是否存在
    :param name: 用户名
    :return: 用户名存在则返回其所在列表中的index值，反之则返回-1
    """
    # 法一：通过列表的[][]操作比对name值，找到其所在列表中的index
    # for i in range(len(users)):
    #     if users[i][0] == name:
    #         return i

    # 法二：通过index()函数，返回其所在列表中的index
    for user in users:
        if name in user:
            return users.index(user)

    return -1


# 查询
def query():
    print('>>> 正在进行查询操作……')


# 取款
def withdraw():
    print('>>> 正在进行取款操作……')


# 存款
def deposit():
    print('>>> 正在进行存款操作……')


# 转账
def transfer():
    print('>>> 正在进行转账操作……')


# 审计/流水清单
def audit():
    print('>>> 正在进行审计操作……')


def enter() -> None:
    """
    入口程序，启动WoniuATM
    :return:
    """
    # 构建入口程序菜单
    menu = '''
    ***************** 欢迎使用 WoniuATM **********************
    *****************   请选择操作菜单   **********************
    ************** 1、注册   2、登录   3、退出 *****************
    '''
    print(menu)

    option = input('>>> 请输入相应的“数字”选择您想进行的操作：')
    if option == '1':
        while not register():
            continue
        enter()
    elif option == '2':
        while not login():
            continue
        home()
    elif option == '3':
        exit('>>> 谢谢，欢迎下次光临。')
    else:
        print('>>> 您输入的操作选项有误，请重新输入。')
        enter()


def home() -> None:
    """
    程序主页，WoniuATM 业务菜单
    :return:
    """
    # 构建主页面的菜单
    menu = '''
    *************************** 欢迎进入 WoniuATM **********************************
    ***************************   请选择操作菜单  ***********************************
    ********** 1、查询   2、取款   3、存款   4、转账   5、流水  6、返回  7、退出 **********
    '''
    print(menu)

    option = input(">>> 请输入相应的“数字”选择您想进行的操作：")
    if option == "1":
        query()
    elif option == "2":
        withdraw()
    elif option == "3":
        deposit()
    elif option == "4":
        transfer()
    elif option == "5":
        audit()
    elif option == "6":
        enter()
    elif option == "7":
        exit('谢谢，欢迎下次光临.')


enter()     # 调用入口函数启动程序

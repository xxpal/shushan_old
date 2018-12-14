# ===============================================================================
# product: WoniuATM
# version: 1.3
# author: Leo
# updated: 12/13/2018
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
import random

# 定义单独的列表，分别保存不同的用户属性
# names = ['steve', 'bill', 'jack']
# passwords = ['112233', 'abc', 'ma88']
# tels = ['13966668888', '18899996666', '19977778888']

# 定义一个包含列表元素的列表，用于保存注册用户信息
# users = [['steve', '112233', '13966668888'],
#          ['bill', 'abc', '18899996666'],
#          ['jack', 'ma88', '19977778888']]


# 定义一个包含字典元素的列表，用于保存所有注册用户信息，其中每个用户的信息以字典形式保存
users = [{'name': 'steve', 'password': '123', 'tel': '13966668888', 'balance': 9000.00, 'history': ''},
         {'name': 'bill', 'password': 'abc', 'tel': '18899996666', 'balance': 7500.00, 'history': ''},
         {'name': 'jack', 'password': 'ma88', 'tel': '19977778888', 'balance': 5800.00, 'history': ''}]

# 定义一个全局变量，用于保存当前登录用户的在users列表中的index值，默认未登录的情况下为-1
current_user_id = -1


# 业务类函数：注册
def register() -> bool:
    name = input('>>> 请输入您期望注册的用户名：')
    index = check_user(name)
    status = False

    # 判断用户名是否存在
    if index >= 0:
        print('>>> 对不起！该用户名已被占用，请重新注册！')
    else:
        print('>>> 恭喜，该用户名可用！')
        password = input('>>> 请输入您的密码：')
        tel = input('请输入您的电话号码：')
        balance = random.randint(1000, 9999)
        user = {}
        user.update({'name': name,
                     'password': password,
                     'tel': tel,
                     'balance': balance,
                     'history': ''})
        users.append(user)
        status = True

    return status


# 业务类函数：登录
def login() -> bool:
    name = input('请输入您的用户名：')
    index = check_user(name)
    status = False

    if index >= 0:
        password = input('请输入您的密码：')
        if users[index]['password'] == password:
            print('登录成功！')
            global current_user_id
            current_user_id = index
            status = True
        else:
            print('密码错误，请重新登录！')
    else:
        print('该用户不存在，请先注册！')

    pass


# 业务类函数：查询
def query(user_id: int) -> None:
    pass


# 业务类函数：取款
def withdraw(user_id: int) ->None:
    pass


# 业务类函数：存款
def deposit(user_id: int) -> None:
    pass


# 业务类函数：转账
def transfer(user_id: int) -> None:
    pass


# 业务类函数：审计、流水、清单
def audit(user_id: int) -> None:
    pass


# 功能性函数：检查用户名是否存在
def check_user(name: str) -> int:


    # # 法1：
    # for i in range(len(users)):
    #     if users[i]['name'] == name:
    #         return i

    # 法2：
    for user in users:
        if user['name'] == name:
            return users.index(user)

    return -1


# 功能性函数：检查输入的字符串是否能被转化成一个有效的数字
def check_number(input_str: str) -> bool:
    pass


# 功能性函数：保存历史交易记录
def save_transaction(user_id: int, tran_type: str, money: float) -> None:
    pass


# 功能性函数：检查/修改账户余额
def check_balance(user_id: int, money: float) -> None:
    pass


# 流程控制函数：WoniuATM入口程序
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
        # while not register():
        #     continue
        register()
        enter()
    elif option == '2':
        count = 0
        # 登录失败3次，则返回入口程序
        while not login():
            count += 1
            if count == 3:
                print('>>> 登陆失败3次，请您稍后再试或重新注册！')
                enter()
            else:
                print('>>> 登陆失败%d次，您还可尝试%d次，请确认您的登录信息！' % (count, 3 - count))
                continue
        home()
    elif option == '3':
        exit('>>> 感谢使用WoniuATM，欢迎下次光临！')
    else:
        print('>>> 您输入的操作选项有误，请重新输入。')
        enter()

    return


# 流程控制函数：WoniuATM业务操作主程序
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
        query(current_user_id)
        home()
    elif option == "2":
        withdraw(current_user_id)
        home()
    elif option == "3":
        deposit(current_user_id)
        home()
    elif option == "4":
        transfer(current_user_id)
        home()
    elif option == "5":
        audit(current_user_id)
        home()
    elif option == "6":
        enter()
    elif option == "7":
        exit('>>> 感谢使用WoniuATM，欢迎下次光临！')

    return


# 函数调用，运行WoniuATM
enter()

# ===============================================================================
# product: WoniuATM
# version: 1.3
# author: Leo
# updated: 12/12/2018
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
# 如果需要存第三个值，如：电话号码，请问怎么做比较好？              ==> Done
# ===============================================================================
import random
import time

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
    """
    用户注册
    :return: 注册成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您期望注册的用户名：')
    index = check_user(name)
    status = False

    # 先判断用户名是否存在
    if index >= 0:
        print('>>> 对不起，该用户名已存在，请重新注册！')
    else:
        print('>>> 恭喜！您输入的用户名可用！')
        password = input('>>> 请设置您的账户密码：')
        tel = input('>>> 请输入您的电话号码：')
        balance = random.randint(1000, 9999)  # 生成一个随机数，模拟新注册的用户的初始的存款金额
        # 不同的属性值构成了用户记录，每个用户的信息以字典的形式保存
        user = {}
        user.update({'name': name, 'password': password, 'tel': tel,
                     'balance': balance, 'history': ''})
        # 将所有的用户记录以列表形式保存，并返回状态值
        users.append(user)
        status = True
        print('>>> 注册成功！')

    return status


# 业务类函数：登录
def login() -> bool:
    """
    用户登录
    :return: 登录成功则返回True，反之则返回False
    """
    name = input('>>> 请输入您的用户名：')
    index = check_user(name)
    status = False

    if index >= 0:
        password = input('>>> 请输入您的密码：')
        if users[index]['password'] == password:
            print('>>> 登录成功！')
            global current_user_id  # 要在函数中修改全局变量，则必须加global进行声明，若只读取不修改，直接读取即可
            current_user_id = index  # 将当前用户的index值赋值给全局变量current_user
            status = True
        else:
            print('>>> 密码错误，请重新登录！')
    else:
        print('>>> 该用户不存在，请先注册！')

    return status


# 业务类函数：查询
def query(user_id: int) -> None:
    print('>>> 正在进行查询操作……')
    print('>>> 尊敬的%s，您的账户余额为：%.2f元，电话号码为：%s。' %
          (users[user_id]['name'],
           users[user_id]['balance'],
           users[user_id]['tel']))

    return


# 业务类函数：取款
def withdraw(user_id):
    print('>>> 正在进行取款操作……')
    money = input(">>> 请输入您的取款金额：")
    # 先判断输入内容是否是有效的数字
    if check_number(money):
        # 取款前先要判断账户余额
        if users[user_id]['balance'] >= float(money):
            save_transaction(user_id, '取款', float(money))
            check_balance(user_id, -float(money))
        else:
            print('>>> 您的账户余额不足，请确认后重新输入！')
    else:
        print(">>> 您输入的金额有误，请确认后重新输入！")
        withdraw(user_id)

    return


# 业务类函数：存款
def deposit(user_id: int):
    print('>>> 正在进行存款操作……')
    money = input('>>> 请输入您的存款金额：')
    # 先判断输入内容是否是有效的数字
    if check_number(money):
        save_transaction(user_id, '存款', float(money))
        check_balance(user_id, float(money))
    else:
        print('>>> 您输入的金额有误，请确认后重新输入！')
        deposit(user_id)

    return


# 业务类函数：转账
def transfer(user_id: int):
    print('>>> 正在进行转账操作……')
    payee = input('>>> 请输入对方账户名称：')
    money = input('>>> 请输入您的转账金额：')
    payee_id = check_user(payee)

    # 如果收款人不存在，则提示用户重新输入对方账户信息
    if payee_id == -1:
        print('>>> 对方账户不存在，请确认后重新输入！')
        transfer(user_id)
    else:
        # 如果输入的转账金额格式不正确，则提示用户重新输入
        if check_number(money):
            # 如果转账金额大于用户的账户余额，则提示用户账户余额不足
            if float(money) > float(users[user_id]['balance']):
                print('>>> 您的账户余额不足，请确认后重新输入！')
                transfer(user_id)
            else:
                save_transaction(user_id, '取款', float(money))
                # save_transaction(payee_id, '存款', float(money))
                check_balance(user_id, float(money))
                # check_balance(payee_id, float(money))
        else:
            print('>>> 您输入的金额有误，请确认后重新输入！')

    return


# 业务类函数：审计、流水、清单
def audit(user_id: int) -> None:
    print('>>> 正在查询历史记录……')
    current_user = users[user_id]

    histories = current_user['history'].split('##')
    print('>>> 尊敬的%s，您的账户历史交易如下：' % current_user['name'])
    for history in histories:
        print('>>>\t--- ', history)

    return


# 功能性函数：保存历史交易记录
def save_transaction(user_id: int, tran_type: str, money: float) -> None:
    """

    :param user_id:
    :param tran_type:
    :param money:
    :return:
    """
    current_user = users[user_id]
    before_transaction = current_user['history']
    this_transaction = current_user['name'] + ' ' + time.strftime('%Y-%m-%d %H:%M:%S') + \
        ' ' + tran_type + ' ' + str(money)
    history = before_transaction + '##' + this_transaction
    current_user['history'] = history
    # users[user_id] = current_user
    print('>>> 尊敬的%s，您有一条新的交易记录：\n\t--- %s' % (current_user['name'], this_transaction))

    return


# 功能性函数：检查账户余额
def check_balance(user_id: int, money: float):
    current_user = users[user_id]
    current_user['balance'] = current_user['balance'] + money
    # users[current_user_id] = current_user
    if money < 0:
        print('>>> 尊敬的%s，您已成功取款：%.2f元，当前账户余额为：%.2f元。' %
              (current_user['name'], money, current_user['balance']))
    else:
        print('>>> 尊敬的%s，您已成功存款：%.2f元，当前账户余额为：%.2f元。' %
              (current_user['name'], money, current_user['balance']))

    return


# 功能性函数：检查用户名是否存在
def check_user(name: str) -> int:
    """
    检查用户名是否存在
    :param name: 用户名
    :return: 用户名存在则返回其所在列表中的index值，反之则返回-1
    """
    # 法一：通过列表和字典的[][]操作比对name值，找到其所在列表中的index
    # for i in range(len(users)):
    #     if users[i]['name'] == name:
    #         return i

    # 法二：通过index()函数，返回其所在列表中的index
    for user in users:
        if user['name'] == name:
            return users.index(user)

    return -1


# 功能性函数：检查输入的字符串是否能被转化成一个有效的数字
def check_number(input_str: str) -> bool:
    """
    对输入的字符串进行判断，确认其是否可以转换为一个有效的数字
    :param input_str:
    :return:
    """
    is_valid = False  # 标识是否是有效的字符串
    # 综合考虑实际的业务需求，存钱的金额一般为正整数
    for char in input_str:
        if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if char is '0' and input_str.index(char) == 0:
                is_valid = False
                break
            else:
                is_valid = True
        else:
            is_valid = False
            break

    return is_valid


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

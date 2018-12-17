import socket
import threading


class WoniuTalkServer:
    def __init__(self):
        self.channels = []   # [ ['张三', chanel-1], ['李四', chanel-2] ....]

    def accept_client(self):
        # 服务器接收消息：
        # 1、绑定一个确定的端口地址
        # 2、启动监听端口的进程
        # 3、准备接收信息
        # 4、当有信息时，接收它
        server = socket.socket()
        server.bind(('19.19.19.251', 8888))
        server.listen()
        print("“蜗牛聊天室”服务器启动成功，欢迎来撩！")

        while True:     # 外死循环，用于等待建立与客户端的通道，表示可以接受无数个。
            channel, address = server.accept()  # 等待新的连接通道的建立：阻塞
            channel.send(("欢迎来自" + str(address) + "的朋友，请输入你的姓名：").encode())
            user_name = channel.recv(1024).decode()
            print('来自[' + user_name + '->' + str(address) + ']的朋友加入群聊.')

            # 将当前对话的用户名和channel加入到channels中，构成一个二维列表
            self.channels.append([user_name, channel])

            for c in self.channels:
                c[1].send(('欢迎[' + user_name + ']加入群聊.').encode())

            threading.Thread(target=self.send_receive, args=(user_name, channel, address)).start()

    def send_receive(self, username, channel, address):
        try:
            while True:
                from_msg = channel.recv(1024).decode()  # 接收来自客户端的消息
                print('来自[' + username + '->' + str(address) + ']的消息：' + from_msg)

                if str(from_msg).startswith("@"):
                    msg_list = from_msg.split(' ')
                    private_name = msg_list[0][1:]
                    private_msg = msg_list[1]
                    private_chanel = self.search_for_channel(private_name)
                    if private_chanel != None:
                        private_chanel.send((username + '->单独对你说：' + private_msg).encode())
                    else:
                        channel.send(('你私聊的用户[' + private_name + ']不存在.').encode())

                else:
                    to_msg = username + '->说：' + from_msg  # 往客户端连接通道发消息

                    # 一旦收到一个客户端的消息，则群发
                    for mychanel in self.channels:
                        mychanel[1].send(to_msg.encode())
        except:
            print("好像有异常出现，服务器自行停止.")

    # 根据用户的昵称或姓名，找到对应的通信通道
    def search_for_channel(self, username):
        for mychanel in self.channels:
            if username == mychanel[0]:
                return mychanel[1]
        else:
            return None


if __name__ == '__main__':
    talk_server = WoniuTalkServer()
    try:
        talk_server.accept_client()        # 只要receive方法中有异常发生，均会进入except分支运行其代码
    except ConnectionResetError:
        print("好像有异常出现，服务器自行停止。")

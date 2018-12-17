import socket
import threading


class WoniuTalkServer:
    def __init__(self):
        self.channels = []

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
            channel.send(("欢迎来自" + str(address) + "的朋友，你的第一条消息将作为你的昵称.").encode())
            self.channels.append(channel)  # 一旦有新客户端，则将该socket对象保存到列表中)

            threading.Thread(target=self.send_receive, args=(channel, address)).start()
            print(channel)
            print(type(channel))

    def send_receive(self, channel, address):
        while True:
            msg_from = channel.recv(1024).decode()  # 接收来自客户端的消息
            print('来自' + str(address) + '的消息：' + msg_from)

            msg_to = str(address) + '说：' + msg_from     # 往客户端连接通道发消息
            # channel.send(msg_to.encode())     # 回复一个客户端

            # 一旦收到一个客户端的消息，则群发
            for c in self.channels:
                c.send(msg_to.encode())


if __name__ == '__main__':
    talk_server = WoniuTalkServer()
    try:
        talk_server.accept_client()  # 只要receive方法中有异常发生，均会进入except分支运行其代码
    except ConnectionResetError:
        print("好像有异常出现，服务器自行停止。")

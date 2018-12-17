import socket
import threading


class WoniuTalkClient:
    def __init__(self):
        self.client = socket.socket()   # 实例化socket对象

    def connect_server(self):
        # 1. 建立与服务器端的连接
        # 2. 发送数据
        # 3. 关闭连接

        self.client.connect(('19.19.19.251', 8888))
        # print("您好，欢迎进入蜗牛聊天室，请开始您的表演！")

        threading.Thread(target=self.send_message).start()
        threading.Thread(target=self.receive_message).start()

    def send_message(self):
        while True:
            msg_to = input("请输入您的消息：")
            self.client.send(msg_to.encode())   # 将一个字符串以特定的编码格式进行编码，默认是utf-8

    def receive_message(self):
        while True:
            msg_from = self.client.recv(1024).decode()  # 接收来自服务器端的消息
            print(msg_from)

    def __del__(self):
        self.client.close()


if __name__ == '__main__':
    talk_client = WoniuTalkClient()
    talk_client.connect_server()

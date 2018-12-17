import socket


class WoniuTalkClient:
    def __init__(self):
        self.client = socket.socket()   # 实例化socket对象

    def send_message(self):
        # 1、连接服务器端
        # 2、发送数据
        # 3、关闭连接

        self.client.connect(('19.19.19.251', 8888))
        while True:
            msg_to = input("请输入你的消息：")
            self.client.send(msg_to.encode())    # 将一个字符串以特定的编码格式进行编码，默认是utf-8
            msg_from = self.client.recv(1024).decode()  # 接收来自服务器端的消息
            print(msg_from)

    def __del__(self):
        self.client.close()


if __name__ == '__main__':
    tc = WoniuTalkClient()
    tc.send_message()

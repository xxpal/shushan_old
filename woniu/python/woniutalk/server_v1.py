import socket


class WoniuTalkServer:
    def __init__(self):
        pass

    def send_receive(self):
        # 服务器接收消息：
        # 1、绑定一个确定的端口地址
        # 2、启动监听端口的进程
        # 3、准备接收信息
        # 4、当有信息时，接收它
        server = socket.socket()
        server.bind(('19.19.19.251', 8888))
        server.listen()
        print("服务器启动成功，欢迎来聊...")

        while True:     # 外层死循环，用于等待建立与客户端的通道，表示可以接受无数个。
            chanel, address = server.accept()  # 等待新的连接通道的建立：阻塞

            # 内层死循环，用于接受来自于同一个连接通道的消息，
            # 但是，如果内层循环没有结束，则无法接收第二个通道。
            # 如何改进？多线程
            while True:
                msg_from = chanel.recv(1024).decode()   # 接收来自客户端的消息并解码
                print('来自' + str(address) + '的消息：' + msg_from)
                msg_to = '服务器回复：' + msg_from    # 往客户端连接通道发消息
                chanel.send(msg_to.encode())    # 将消息编码后发回客户端


if __name__ == '__main__':
    talk_server = WoniuTalkServer()
    try:
        talk_server.send_receive()  # 只要receive方法中有异常发生，均会进入except分支运行其代码
    except:
        print("好像有异常出现，服务器自行停止。")

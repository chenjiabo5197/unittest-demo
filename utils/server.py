"""
@Time:2024/11/24 12:48
@Emial:chen_wangyi666@163.com
"""
import os
import sys
import threading
import time
import grpc
from concurrent import futures

# 获取当前文件的绝对路径，并找到项目的根目录
current_file_path = os.path.abspath(__file__)
project_root_path = os.path.dirname(os.path.dirname(current_file_path))
# 将项目的根目录添加到sys.path中
sys.path.append(project_root_path)

from proto_generate import test_pb2_grpc
from proto_generate import test_pb2

global service


class StreamTest(test_pb2_grpc.StreamTestServicer):
    """注意：proto中定义的通讯接口都需要在这里继承"""

    def BothStream(self, request_iterator, context):
        """proto中定义的通讯接口"""
        for i in request_iterator:
            print("客户端发送：", i.message)

        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            time.sleep(1)
            # 注意： 由于BothStream的返回值是stream格式的，所以此处需要用yield返回，若非stream格式的，此处使用return返回
            yield test_pb2.response(message=i)


def server(port):
    """grpc服务器"""
    service = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ("grpc.max_send_message_length", 1024 * 1024 * 1024),
        ("grpc.max_receive_message_length", 1024 * 1024 * 1024),
        ("grpc.enable_retries", 1)
    ])
    test_pb2_grpc.add_StreamTestServicer_to_server(StreamTest(), service)
    service.add_insecure_port("[::]:" + port)
    service.start()


def start_serve(port):
    """"""
    th = threading.Thread(target=server, args=[port])
    th.start()


def stop_serve():
    """"""
    global service
    service.stop(0)



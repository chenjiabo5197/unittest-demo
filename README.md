# unittest测试框架case demo
#### 1、基于python的unittest测试框架的自动化case，被测对象为grpc的客户端，测试case启一个grpc的服务端与客户端通讯

#### 2、需在unittest-demo目录下执行测试case
    例：python3 cases/run_cases.py
#### 3、proto基础知识
###### （1）、proto常见关键字
    syntax      指定protobuf版本
    package     包名，可以不填
    import      导入一些插件
    message     定义传输的数据结构
    service     定义服务
    rpc         定义服务中的方法
    stream      定义方法中数据的传输方式为流传输

###### （2）、proto中message的常见数据类型
    string      默认为空白字符
    int32/int64 对应长短整型，默认0
    bool        bool类型
    float       浮点型
    repeated    python中的列表，但数据类型只能为1种
    map         python种的字典，但数据类型只能为1种
    bytes       比特类型，默认是空白字节，可能包含任何字节序列

###### （3）、生成python proto文件
    python -m grpc_tools.protoc --python_out=./ --grpc_python_out=./ -I./ test.proto


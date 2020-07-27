# -*- coding: utf-8 -*-


import pika
credentials = pika.PlainCredentials("guest", "guest")
# 建立连接到代理服务器
conn_params = pika.ConnectionParameters(
    "192.168.1.103", credentials=credentials)
conn_broker = pika.BlockingConnection(parameters=conn_params)

channel = conn_broker.channel()
# 声明一个交换器
channel.exchange_declare(exchange="hello-exchange", exchange_type="direct",
                         passive=False, durable=True, auto_delete=False)

# 声明一个队列并绑定交换器
channel.queue_declare(queue="hello-queue")
channel.queue_bind(queue="hello-queue",
                   exchange="hello-exchange", routing_key="hola")


# 用于处理消息的函数
def msg_consumer(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    #b" "前缀表示：后面字符串是bytes 类型。
    if body == b"quit":
        channel.basic_cancle(consumer_tag="hello-consumer")
        channel.stop_consumer()
    else:
        print(body)
    return


# 订阅消费者
channel.basic_consume("hello-queue", msg_consumer,
                      consumer_tag="hello-consumer")
# 开始消费，无尽的阻塞循环
channel.start_consuming()

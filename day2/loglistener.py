# -*- coding: utf-8 -*-


import pika
credentials = pika.PlainCredentials("guest", "guest")
# 建立连接到代理服务器
conn_params = pika.ConnectionParameters(
    "192.168.1.103", credentials=credentials)
conn_broker = pika.BlockingConnection(parameters=conn_params)
channel = conn_broker.channel()
# 日志队列
channel.queue_declare('errors_queue')
channel.queue_declare('warnings_queue')
channel.queue_declare('info_queue')
# 日志交换器
rabbit_exchange = 'amq.rabbitmq.log'
# 绑定队列到交换器
channel.queue_bind(queue='errors_queue',
                   exchange=rabbit_exchange, routing_key='error')
channel.queue_bind(queue='warnings_queue',
                   exchange=rabbit_exchange, routing_key='warn')
channel.queue_bind(queue='info_queue',
                   exchange=rabbit_exchange, routing_key='info')

# 创建回调函数


def errror_callback(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print('error  %s' % body)


def warn_callback(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print('warn  %s' % body)


def info_callback(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print('info %s' % body)


# 订阅消费者
channel.basic_consume("errors_queue", errror_callback)
channel.basic_consume("warnings_queue", warn_callback)
channel.basic_consume("info_queue", info_callback)
# 开始消费，无尽的阻塞循环
channel.start_consuming()

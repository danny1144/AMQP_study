# -*- coding: utf-8 -*-

import pika
import sys
# 认证
credentials = pika.PlainCredentials('guest', 'guest')
#
conn_params = pika.ConnectionParameters(
    '192.168.1.103', credentials=credentials)
# 建立到代理服务器的连接
conn_broker = pika.BlockingConnection(conn_params)
# 信道
channnel = conn_broker.channel()
# 声明交换器
channnel.exchange_declare("hello-exchange", exchange_type="direct",
                          passive=False, durable=True, auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
# 发布消息
channnel.basic_publish(body=msg, exchange="hello-exchange",
                       properties=msg_props, routing_key="hola")

# -*- coding: utf-8 -*-

import pika
import pika.spec as spec
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
# 确认回调


def confirm_handler(frame):
    # 判断信道已经准备就绪来接受发送方确认消息
    if type(frame.method) == spec.Confirm.SelectOk:
        print("channel in confirm mode")
    # 内部错误丢失
    elif type(frame.method) == spec.Basic.Nack:
        if frame.method.delivery_tag in msg_ids:
            print("message lost")
    elif type(frame.method) == spec.Basic.Ack:
        if frame.method.delivery_tag in msg_ids:
            print("confirm recieved")
            msg_ids.remove(frame.method.delivery_tag)


# confirm_deliveries只表示当RabbitMQ收到消息时,将返回basic.ack(收到消息)或basic.nack(未收到消息).
channnel.confirm_delivery()
# 声明交换器
channnel.exchange_declare("hello-exchange", exchange_type="direct",
                          passive=False, durable=True, auto_delete=False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
msg_ids = []
# 发布消息
ack = channnel.basic_publish(body=msg, exchange="hello-exchange",
                             properties=msg_props, routing_key="hola")

print(ack)
if ack is True:
    print("put message to rabbitmq successed!")
else:
    print("put message to rabbitmq failed")

msg_ids.append(len(msg_ids)+1)
channnel.close()

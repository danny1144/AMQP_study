# -*- coding: utf-8 -*-

import pika
import json
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
channnel.exchange_declare("rpc", exchange_type="direct",
                          passive=False, durable=True, auto_delete=False)


channnel.queue_declare(queue='ping')
channnel.queue_bind(queue='ping', exchange='rpc', routing_key='ping')


def api_ping(channnel, method, header, body):
    channnel.basic_ack(delivery_tag=method.delivery_tag)
    msg_dict = json.loads(body)
    print(msg_dict)
    print('recieveed api call ..replying..')
    channnel.basic_publish(
        body='pong %s' % str(msg_dict['time']), exchange='', routing_key=header.reply_to)


channnel.basic_consume(on_message_callback=api_ping,
                       queue='ping', consumer_tag='ping')
print('wainting for rpc calls...')
channnel.start_consuming()

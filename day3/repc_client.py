import time
import json
import pika


# 认证
credentials = pika.PlainCredentials('guest', 'guest')
#
conn_params = pika.ConnectionParameters(
    '192.168.1.103', credentials=credentials)
# 建立到代理服务器的连接
conn_broker = pika.BlockingConnection(conn_params)
# 信道
channnel = conn_broker.channel()
msg = json.dumps({
    "client_name": "RPC client 1.0",
    "time": time.time()
})
result = channnel.queue_declare(queue='', exclusive=True, auto_delete=True)

msg_props = pika.BasicProperties()
msg_props.reply_to = result.method.queue

channnel.basic_publish(body=msg, exchange='rpc',
                       properties=msg_props, routing_key='ping')

print('sent ping repc call , waingting for reply ...')


def reply(channnel, method, header, body):
    print(body)
    channnel.stop_consuming()


channnel.basic_consume(on_message_callback=reply,
                       queue=result.method.queue, consumer_tag=result.method.queue)
channnel.start_consuming()

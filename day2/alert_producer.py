# -*- coding: utf-8 -*-

import pika
import sys
from optparse import OptionParser

AMQP_HOST = 'localhost'
AMQP_USER = 'admin'
AMQP_PASSWORD = 'puhuijia'
AMQP_VHOST = '/'
AMQP_EXCHANGE = 'alerts'
CRITICAL_QUEUE = 'critical_queue'
LIMIT_QUEUE = 'rate_limit_queue'
# 认证
credits_broker = pika.PlainCredentials(AMQP_USER, AMQP_PASSWORD)
conn_params = pika.ConnectionParameters(
    AMQP_HOST, credentials=credits_broker)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
opt_parser = OptionParser()
opt_parser.add_option('-r', '--routing_key', dest="message",
                      help='Routing key for message')
opt_parser.add_option('-m', '--routing_key', dest="message",
                      help='Routing key for message')
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
# 发布消息
channel.basic_publish(body=msg, exchange=AMQP_EXCHANGE,
                      properties=msg_props, routing_key="critical.hello")

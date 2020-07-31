import pika

if __name__ == '__main__':

    AMQP_HOST = 'localhost'
    AMQP_PORT = '15672'
    AMQP_USER = 'admin'
    AMQP_PASSWORD = 'puhuijia'
    AMQP_VHOST = '/'
    AMQP_EXCHANGE = 'alerts'

    CRITICAL_QUEUE = 'critical_queue'
    LIMIT_QUEUE = 'rate_limit_queue'
    # 认证
    credits_broker = pika.PlainCredentials(AMQP_USER, AMQP_PASSWORD)
    conn_params = pika.ConnectionParameters(
        AMQP_HOST, AMQP_PORT, AMQP_VHOST, credits_broker=credits_broker)
    conn_broker = pika.BlockingConnection(conn_params)
    channel = conn_broker.channel()

    channel.exchange_declare(AMQP_EXCHANGE, exchange_type='topic')
    channel.queue_declare(CRITICAL_QUEUE)
    channel.queue_declare(LIMIT_QUEUE)

    channel.queue_bind(CRITICAL_QUEUE, exchange=AMQP_EXCHANGE,
                       routing_key='critical.*')
    channel.queue_bind(LIMIT_QUEUE, exchange=AMQP_EXCHANGE,
                       routing_key='*.rate_limie')
    # 用于处理消息的函数

    def msg_consumer(channel, method, header, body):
        channel.basic_ack(delivery_tag=method.delivery_tag)
        # b" "前缀表示：后面字符串是bytes 类型。
        print(body)

    # 订阅消费者
    channel.basic_consume(CRITICAL_QUEUE, msg_consumer,
                          consumer_tag="critical")
    channel.basic_consume(LIMIT_QUEUE, msg_consumer,
                          consumer_tag="rate_limie")
    print('开始消费告警信息了')
    # 开始消费，无尽的阻塞循环
    channel.start_consuming()

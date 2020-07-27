# 生产者
- 连接到rabbitMQ
- 获取信道
- 声明交换器
- 创建消息
- 发布消息
- 关闭信道
- 关闭连接

# 消费者

- 连接到rabbitMQ
- 获取信道
- 声明交换器
- 声明队列
- 把队列和交换器绑定起来
- 消费消息
- 关闭信道
- 关闭连接

```
开始生产
 python helloword_producer.py "hello_world"

停止生产
python helloword_producer.py "quit" 


python 
```
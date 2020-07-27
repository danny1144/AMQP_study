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
```

-  交换器
***
用来接收生产者发送的消息并将这些消息路由给服务器中的队列。
***
三种常用的交换器类型：

- direct(发布与订阅 完全匹配)
- topic(主题， 规则匹配)
- fanout(广播)
## 使用发送方确认模式来确认投递

*** 
由于事务会影响性能，因此我们专注于使用publish confirm作为消息投递保障的首选方案 
***



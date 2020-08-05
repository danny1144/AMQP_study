
## 启动节点

```
守护进程启动
 rabbitmqserver -server -detached

 不加参数默认默认使用
 节点名称  rabbit 
 监听端口 - 5672

 集群启动

 RABBITMQ_NODE_PORT =5672 RABBITMQ_NODENAME=rabbit
```
## 内存节点
内存节点保存所有的队列，绑定，交换器，用户、权限、和vhost的元数据读写性能好，不能持久化

## 磁盘节点
元数据存储在磁盘，可以持久化。性能差些
## 配置 Cookie

Erlang节点间通过认证 Erlang cookie的方式完成相互之间的通信
rabbitmqctl 使用 erlang otp通信机制来和rabbit通信
因此集群直接需要拷贝同一份 cookie 路径为/root/.erlang.cookie
## 停止节点

break： abort continue proc info info  loaded  version kill db-table distribution

```
rabbitmqserver stop -n rabbit@[hostname]
```
关闭信息： rabbit mnesia os_mon

mnesia 数据库配置选项

- dump_log_write_threshold 转存数据到真实数据库文件的频率
- tcp_listenners rabbitmq监听的IP地址和端口
- ssl_listenners SSL加通信的地址和端口
- ssl_option SSL选项
- vm_memory_high_watermark  内存安装百分比
- queue_index_max_journal_entries 消息存储最大条目
- msg_store_file_size_limit 消息存储数据库的最大大小
## 请求许可
RabbitMQ权限系统可以跨越多管vhost进行授权。当应用程序需要跨越多个安全域进行通信时，（使用虚拟机进行隔离）。这会极大方便访问控制的管理、、

## 管理用户
```
创建用户
rabbitmqctl add_user zxp 123456
删除用户,同时删除与用户相关的访问控制条目
rabbitmqctl delete_user zxp
```

 ## 权限系统

**ACL风格的权限系统  **


- 读 有关消息的任何操作，包括清除整个队列 绑定
- 写 发布消息 绑定
- 配置 队列和交换器的创建和删除

![img](https://upload-images.jianshu.io/upload_images/12016719-40a096f93e1fe19b.png!web?imageMogr2/auto-orient/strip|imageView2/2/w/550/format/webp)

***访问控制条目是无法跨越vhost的***

每一条访问控制条目由以下四部分组成

- 被授予访问权限的用户
- 权限控制应用的vhost
- 需要授予的读/写/配置权限的组合
- 权限范围- 客户端命名的队列交换器、服务端命名的队列/交换器

查看rabbitmqctl工具相关命令

查看所有虚拟主机

```
 rabbitmqctl list_vhosts
```

### 添加vhost 

```
rabbitmqctl add_vhost test_vhost
rabbitmqctl list_vhosts
```

## 给用户授权

```
赋予用户读写配置访问权限
rabbitmqctl set_permissions -p test_vhost zxp ".*" ".*" ".*"
```

## 移除权限

```
rabbitmqctl clear_permissions -p test_vhost zxp 
```

## 查看权限

```

查看vhost权限
rabbitmqctl list_permissions -p test_vhost
查看用户权限

rabbitmqctl list_user_permissions zxp

查看交换器的名称、类型、是否持久化、是否自动删除
rabbitmqctl list_exchanges  name type durable auto_delete

查看绑定列表、
rabbitmqctl list_bindings

查看erlang令牌，通过令牌交换获取认证
cat .erlang.cookie 
VLCXLMJNFFXQLQSHNSXS
erlang 函数

erl -sname test
用短名称启动RabbitMQ 

node(). 查找出节点名称

net_adm:names().
{ok,[{"rabbit",25672},{"test",46123}]}

建立连接

54*/
pang



```

## Mnesia 和主机名

Mnesia 作为erlang数据库，存储队列，交换器绑定等信息
Mnesia 会根据主机名 创建数据库的schema。如果由于网路重新配置的原因，主机名修改了。那么mnesia 会无法载入旧的schema


消息队列应用场景
- topic  在应用程序中，存在一个动作触发其他动作，然后并行运行
- 匿名队列，秘密监控一段消息流，然后不留痕迹的离开。并设置自动删除。

- 拓展应用程序的计算能力。不改变原有代码，可以启动更多的消费者进程，使得rabbitmq对消息进行分发给不同的机器上。
- 私有队列和发送确认
- 由于AMQP消息是单向的，RPC服务不知道客户端调用者的身份，所以消息的生产者可以通过reply_to 字段来确认队列名称，并监听队列等待应答。然后接受消息的RPC服务器能检查reply_to字段，并创建包含应答内容的新的消息，并以对列名称作为路由键。

- 阻止其他客户端读取到应答信息

 在声明队列的时候指定exclusive参数，确保只有你可以读取到队列名称包含RPC消息的reply_to 头中，于是服务器端就知道消息应该发往哪里了。此时我们不用讲队列绑定到交换器上，rabbitmq会知道消息的目的地是应答队列，路由键就是队列名称


 
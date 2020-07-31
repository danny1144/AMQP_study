## 启动节点

```
守护进程启动
 rabbitmqserver -server -detached
```


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



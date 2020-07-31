虽然还有http 接口、web admin组件可以进行管理，但是rabbitmqctl 基本包含了 rabbitmq 的全部管理功能，更为全面。 所以将其使用方法总结于此。

一，命令格式
rabbitmqctl [-n ] [-q] []

-n node #默认node名称是"rabbit@server"，如果你的主机名是'server.example.com'，那么node名称是'rabbit@server'
-q #安静输出模式，信息会被禁止输出

二， 基础命令
停止在erlang node上运行的rabbitmq，会使rabbitmq停止
stop

停止erlang node上的rabbitmq的应用，但是erlangnode还是会继续运行的
stop_app

启动erlan node上的rabbitmq的应用
start_app

等待rabbitmq服务启动
wait <pid_file>

初始化node状态，会从集群中删除该节点，从管理数据库中删除所有数据，例如vhosts等等。在初始化之前rabbitmq的应用必须先停止
reset

无条件的初始化node状态
force_reset

轮转日志文件
rotate_logs

三，集群管理
clusternode表示node名称，--ram表示node以ram node加入集群中。默认node以disc node加入集群，在一个node加入cluster之前，必须先停止该node的rabbitmq应用，即先执行stop_app
join_cluster [--ram]

显示cluster中的所有node
cluster_status

改变一个cluster中节点的模式，该节点在转换前必须先停止，不能把一个集群中唯一的disk node转化为ram node
stop_app
change_cluster_node_type disc | ram
start_app

远程移除cluster中的一个node，前提是该node必须处于offline状态，如果是online状态，则需要加--offline参数
forget_cluster_node [--offline]

更新集群节点
update_cluster_nodes clusternode

同步镜像队列
sync_queue queue

取消同步镜像队列
cancel_sync_queue queue

四， 用户管理命令
在rabbitmq的内部数据库添加用户
add_user

删除一个用户
delete_user

改变用户密码（也是改变web管理登陆密码）
change_password

清除用户的密码，该用户将不能使用密码登陆，但是可以通过SASL登陆如果配置了SASL认证
clear_password

设置用户tags
set_user_tags ...

列出用户
list_users

创建一个vhosts
add_vhost

删除一个vhosts
delete_vhost

列出vhosts
list_vhosts [ ...]

针对一个vhosts给用户赋予相关权限
set_permissions [-p ]

清除一个用户对vhosts的权限
clear_permissions [-p ]

列出哪些用户可以访问该vhosts
list_permissions [-p ]

列出该用户的访问权限
list_user_permissions

五，策略管理
策略用来控制和修改queues和exchange在集群中的行为，策略可以应用到vhost。

设置一个policy，"name"为该policy的名字，"pattern"为一个正则表达式，所有匹配该正则表达式的资源都会应用该policy，"definition"是policy的定义，为json格式。"priority"为优先权，整数值。
set_policy [-p vhostpath] {name} {pattern} {definition} [priority]

清除一个策略
clear_policy [-p ]

列出已有的策略
list_policies [-p ]

六，queues && exchange状态信息
返回queue的信息，如果省略了-p参数，则默认显示的是"/"vhosts的信息
list_queues [-p ] [ ...]

返回exchange的信息
list_exchanges [-p ] [ ...]

返回绑定信息
list_bindings [-p ] [ ...]

返回链接信息
list_connections [ ...]

返回目前所有的channels
list_channels [ ...]

返回consumers
list_consumers [-p ]

显示broker的状态
status

显示环境参数的信息
environment

返回一个服务状态report
report

七，插件的开启和关闭方法
rabbitmq-plugins []
Commands:
list [-v] [-m] [-E] [-e] []
显示所有的的插件，-v显示版本、-m显示名称、-E显示明确已经开启的、-e显示明确的和暗中开启的
enable ... #开启一个插件
disable ... #关闭一个插件

eg: rabbitmq-plugins enable rabbitmq_management (prot : 15672)

八，设置参数
set_parameter [-p ] <component_name>

clear_parameter [-p ] <component_name>

list_parameters [-p ]
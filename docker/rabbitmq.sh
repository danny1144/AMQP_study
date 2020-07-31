#!/bin/bash

HOSTNAME=`env hostname`

/usr/sbin/rabbitmq-server &
rabbitmqctl wait /var/lib/rabbitmq/mnesia/rabbit\@$HOSTNAME.pid

                rabbitmqctl delete_user guest
                rabbitmqctl add_user admin puhuijia
                rabbitmqctl set_user_tags admin administrator
                rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

tail -f /var/log/rabbitmq/rabbit\@$HOSTNAME.log
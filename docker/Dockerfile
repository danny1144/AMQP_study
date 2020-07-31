#次镜像用于rabbitmq

FROM      centos:7.2.1511
MAINTAINER  zxp <"1490284462@qq.com">
RUN yum install -y wget unzip tar  \
 &&  wget https://github.com/rabbitmq/erlang-rpm/releases/download/v19.3.6.5/erlang-19.3.6.5-1.el7.centos.x86_64.rpm \
 && yum install -y  erlang-19.3.6.5-1.el7.centos.x86_64.rpm \
&& yum install -y erlang \
&& rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc \
&& yum install -y  https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.0/rabbitmq-server-3.7.0-1.el7.noarch.rpm \
&& /usr/sbin/rabbitmq-plugins list <<<'y' \
&& /usr/sbin/rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_stomp rabbitmq_management  rabbitmq_management_agent rabbitmq_federation <<<'y'

ADD rabbitmq.sh /etc/rabbitmq/
RUN  chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie \
&& chmod 400 /var/lib/rabbitmq/.erlang.cookie \
&& chmod +x /etc/rabbitmq/rabbitmq.sh

EXPOSE 5672
EXPOSE 15672
EXPOSE 25672
EXPOSE 4369
EXPOSE 9100
EXPOSE 9101
EXPOSE 9102
EXPOSE 9103
EXPOSE 9104
EXPOSE 9105

ENTRYPOINT ["/etc/rabbitmq/rabbitmq.sh"]
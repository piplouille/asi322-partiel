./apache-zookeeper-3.6.2-bin/bin/zkServer.sh start
cd kafka_2.12-2.2.0/bin
gnome-terminal -e "./kafka-server-start.sh ../config/server.properties" --

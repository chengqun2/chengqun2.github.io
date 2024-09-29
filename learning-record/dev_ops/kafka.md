### list topics
`kafka-topics.sh --bootstrap-server localhost:9092 --list`

### create topoc 
`kafka-topics.sh --bootstrap-server localhost:9092 --topic first_topic --create --partitions 3 --replication-factor 1`

### produce data into a topic
`kafka-console-producer.sh --broker-list localhost:9092 --topic first_topic`

### consume data from a topic
`kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --from-beginning`
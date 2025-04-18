### https://www.notion.com/product/ai
Notion AI 是一款集成于 Notion 工作空间的一体化人工智能工具，具备搜索、生成、分析、聊天等功能，能连接多种应用获取知识，支持多语言写作与内容编辑，安全性高且有免费试用，付费后可无限使用 。

### Fathom - AI 会议记录工具
Fathom - AI 会议记录工具：
专为提升会议效率设计，能自动录制会议，实时生成精准转录和智能总结 。支持与 Zoom、Google Meet、Microsoft Teams 等主流会议平台无缝集成 ，还可与 CRM 系统同步。具备标注与高亮、搜索与回放、实时提醒与通知等功能 ，能帮助销售、客户成功、产品、市场等团队及个人提升会议相关工作效率。

### npm 和 npx 都是与 Node.js 生态系统紧密相关的工具
npm
包管理：npm（Node Package Manager）是 Node.js 的默认包管理器，核心功能是对 Node.js 包进行管理，包括安装、卸载、更新和查看依赖等操作。例如，使用 npm install lodash 可以将 lodash 包安装到项目中。
脚本执行：npm 允许在 package.json 文件中定义脚本，通过 npm run 命令来执行这些脚本。比如，在 package.json 中定义 "start": "node app.js"，然后使用 npm run start 就可以启动应用。
npx
命令执行：npx 是一个 npm 附带的工具，主要用于执行 npm 包中的可执行文件。它可以直接运行某个包的命令，而不需要事先全局安装该包。例如，使用 npx create-react-app my-app 可以直接创建一个新的 React 应用，无需全局安装 create-react-app。



### 1. nextjs怎么设计路由


2. 前端怎么缓存
3. redis的经验
4. 怎么处理高并发
5. 架构



Pug template:
Pug is a clean, whitespace sensitive syntax for writing HTML.


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/chengqun2/node-connect-linux.git
git push -u origin main



Two different strings sometimes could generate the same hash codes.



Trello 看板和卡片
https://www.freecodecamp.org/news/create-full-stack-app-with-nextjs13-and-firebase/
https://firebase.google.com/codelabs/firebase-emulator#0

## Java多线程：
### Java线程池七个参数详解：
corePoolSize 线程池核心线程大小
maximumPoolSize 线程池最大线程数量
keepAliveTime 空闲线程存活时间
unit 空闲线程存活时间单位
workQueue 工作队列
threadFactory 线程工厂
handler 拒绝策略

ThreadPoolExecutor 提供了四个拒绝策略，分别是:
	CallerRunsPolicy, AbortPolicy, DiscardPolicy, DiscardOldestPolicy

#### 线程池 线程队列满了，后续任务怎么处理?
ThreadPoolExecutor(int corePoolSize, int maximumPoolSize, long keepAliveTime, TimeUnit unit, BlockingQueue<Runnable> workQueue)
当调用 execute() 方法添加一个任务时，线程池会做如下判断：
a. 如果正在运行的线程数量小于 corePoolSize，那么马上创建线程运行这个任务；
b. 如果正在运行的线程数量大于或等于 corePoolSize，那么将这个任务放入队列。
c. 如果这时候队列满了，而且正在运行的线程数量小于 maximumPoolSize，那么还是要创建线程运行这个任务；
d. 如果队列满了，而且正在运行的线程数量大于或等于 maximumPoolSize，那么线程池会抛出异常，告诉调用者“我不能再接受任务了”。


### 在多线程环境下，要使用线程安全的集合，比如，
ConcurrentHashMap是线程安全的HashMap，
CopyOnWriteArrayList是线程安全的ArrayList.
CopyOnWriteArraySet是线程安全的HashSet.

### 线程按顺序执行的方法：
线程 join();


## 消息队列相关：
### 消息队列（Kafka、ActiveMQ、RabbitMQ、RocketMQ ）常见的使用场景：解耦、异步、削峰
解耦：发布端 只管生产数据，消费端 自己订阅或者取消订阅
消息队列的缺点：系统复杂度上升、一致性问题。
kafka高可用：replica（复制品） 副本机制。每个 partition 的数据都会同步到其它机器上，
形成自己的多个 replica 副本。所有 replica 会选举一个 leader 出来，
那么生产和消费都跟这个 leader 打交道，然后其他 replica 就是 follower
防止重复消费：增加唯一性校验
#### 如何解决消息丢失的问题：
1. 生产端： 
   1). producer.send(msg, callback)。带有回调通知的 send 方法可以针对发送失败的消息进行重试处理。
   2). 设置 acks = all
   3). 设置 retries = 3
2. Broker端:
   1).  unclean.leader.election.enable = false
   2). replication.factor >= 3
   3). 设置 min.insync.replicas > 1。这控制的是消息至少要被写入到多少个副本才算是“已提交”。设置成大于 1 可以提升消息持久性。
3. 消费端:
   Kafka关闭自动提交 offset，在处理完之后自己手动提交 offset， 再自己保证幂等性就好了。
#### 如何保证消息的顺序性：一个 topic，有三个 partition。
生产者在写的时候，其实可以指定一个 key，比如说我们指定了某个订单 id 作为 key，
那么这个订单相关的数据，一定会被分发到同一个 partition 中去，
而且这个 partition 中的数据一定是有顺序的。
一个 topic，一个 partition，一个 consumer，内部单线程消费，单线程吞吐量太低，一般不会用这个。
写 N 个内存 queue，具有相同 key 的数据都到同一个内存 queue；然后对于 N 个线程，
每个线程分别消费一个内存 queue 即可，这样就能保证顺序性。

### 死信队列：没有被及时消费的消息存放的队列
a.消息被拒绝（basic.reject/ basic.nack）并且不再重新投递 requeue=false
b.TTL(time-to-live) 消息超时未消费
c.达到最大队列长度
消息变成死信后，会被重新投递（publish）到另一个交换机上（Exchange）,
这个交换机往往被称为DLX(dead-letter-exchange)“死信交换机”，
然后交换机根据绑定规则转发到对应的队列上，监听该队列就可以被重新消费
场景：
超时的订单 可以用死信队列来变通处理

### 消息队列MQ实现过期订单关闭：
RabbitMQ插件、kafka时间轮、RocketMQ延迟消息

### Redission实现过期订单关闭：
RDelayedQueue

### kafka为什么依赖zookeeper?
1、通过使用 ZooKeeper 协调服务，Kafka 就能将 Producer，Consumer，Broker 等结合在一起
2、借助 ZooKeeper，Kafka 就能够将所有组件在无状态的条件下建立起生产者和消费者的订阅关系，实现负载均衡

### kafka分区(partition)的原因：
水平扩展：磁盘写入速度就是kafka处理速度的极限，处理不过来就要加机器。
每台机器持有不同的partition。生产者爱发哪台发哪台，并行处理


## 高并发下的限流：
1、前端 random频闭掉一部分（过于粗暴）
2、消息队列ActiveMQ/RabbitMQ/RocketMQ/kafka等流量削峰、异步处理
3、Redis，库存数量存在redis中，使用String类型的decr(转化成int类型再 减1)、incr(加1)
4、Tomcat 限流: conf/server.xml中的maxThreads
	<Connector port="8080" protocol="HTTP/1.1"
	connectionTimeout="20000"
	maxThreads="150"
	redirectPort="8443" />
5、nginx 限流
	location / {
		limit_req zone=mylimit burst=20 nodelay;  //每秒可以处理20个请求，超出的请求全部返回503
		proxy_pass http://real_server;
	}
limit_req和limit_conn两个模块都是为了来限流的：
request是指请求，即http请求，（注意，tcp连接是有状态的，而构建在tcp之上的http却是无状态的协议
connection是连接，即常说的tcp连接，通过三次握手而建立的一个完整状态机。建立一个连接，必须得要三次握手。

limit_req_zone  $binary_remote_addr zone=req10k:30m rate=100000000r/s;
limit_req  zone=req10k burst=100000000;
rate：每秒可以处理的请求数。
burst：等待处理的请求队列长度。
delay：等待队列中，不需要等待，可以立刻处理的请求数目。
nodelay：一旦设置，相当于delay设置为max int，rate+burst数量的请求全部可以瞬时处理。
例如：rate=10，burst=10，nodelay，每秒可以处理20个请求，超出的请求全部返回503。
rate=10，burst=10，delay=2，一秒钟，来20个请求，可以瞬时处理12个请求，后8个设置定时器，延时处理。



6、Sentinel限流:
	Sentinel 的限流原理主要是通过统计系统的 QPS （即每秒请求数量）和并发量来控制系统的流量，从而达到限流的目的。 
	当并发请求数量超过预设的阈值时， Sentinel 会拒绝该请求，并返回一个 FlowException 的错误响应。 
	限流过滤的实现主要在 FlowSlot 的 entry 方法进行

## nginx负载均衡的5种策略
1、轮询（默认）:每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。
2、权重（weight）:指定轮询几率，weight和访问比率成正比，用于后端服务器性能不均的情况。
3、IP绑定 ip_hash:每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。
4、fair（第三方）:按后端服务器的响应时间来分配请求，响应时间短的优先分配。
5、url_hash（第三方）:按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。



## 分布式事务：
一、消息队列MQ实现分布式事务，最简单的原理框架：
借助消息队列MQ的消息可靠传递，实现业务间解耦、事务强一致
1、>> 生产者发送消息做可靠性检查，确保消息真正投递出去；
（例如生产者 发送消息时先把 1).业务数据入库、
2).然后消息记录(messageId,message:序列化的业务数据,status=0)入库、
3).最后再发送消息;
confirmCallback收到ack之后，消息记录status改为1
定时任务查询status=0的消息记录，再次进行发送，确保消费成功。
）
2、>> 消费者做幂等，确保业务没有重复执行；
3、>> 消费者做异常重试，反复出错时需要捕捉异常并记录，以便手工干预；
二、Seata如何实现分布式事务
Seata针对不同的业务场景提供了四种不同的事务模式，具体如下
AT模式： AT 模式的一阶段、二阶段提交和回滚（借助undo_log表来实现）均由 Seata 框架自动生成，用户只需编写“业务SQL”，便能轻松接入分布式事务，
AT 模式是一种对业务无任何侵入的分布式事务解决方案。
AT模式，分为两个阶段
一阶段：业务数据和回滚日志记录在同一个本地事务中提交，释放本地锁和连接资源
二阶段：提交异步化 （ 或者事务执行失败，回滚通过一阶段的回滚日志进行反向补偿）
三、Redis键通知功能 notify-keyspace-events实现分布式事务

## elasticsarch:
1. es 7、8  一个大区别：8默认需要安全认证
2. String类型:
		text: 会分词
		keyword: 不会分词
3. 中文分词器：
   ik_max_word：最细粒度的拆分;
   ik_smart: 最粗粒度的拆分

## Redis：
### Redis支持三种集群方案
1. 主从复制模式：
   主要目的：读写分离、备份数据。主节点进行`读写`操作，从节点负责`读`操作(读写分离，分担master的读压力)
   缺点： 不具备自动容错与恢复功能、Redis的容量受限于单机配置。Master挂了，需要人工切到Slave
2. Sentinel（哨兵）模式:
   每隔2秒，每个哨兵会通过它所监控的主节点、从节点向__sentinel__:hello通道发布一条hello消息。
   每个哨兵会通过它所监控的主节点、从节点订阅__sentinel__:hello通道的消息，以此接收其他哨兵发布的信息。
   主要目的：高可用、故障自动转移。哨兵模式下故障转移后，从节点会全量复制新的主节点数据。
   缺点： 同样也继承了主从模式难以在线扩容的缺点，Redis的容量受限于单机配置。
   		需要额外的资源来启动sentinel进程，实现相对复杂一点，同时slave节点作为备份节点不提供服务
3. Cluster(集群)模式：
   主要目的：解决单机Redis容量有限的问题，将数据按一定的规则分配到多台机器，内存/QPS不受限于单机。
   			无中心架构、集群中的每个节点都是平等的关系。
   			搭建Redis集群至少需要6台机器。分成3组，每组1台master、 1台slave。某个Master挂了，相应的slave接上。
   缺点：不支持多数据库空间，集群模式下只能使用一个，即db 0。数据通过异步复制，不保证数据的强一致性。

### Redis 持久化机制
1、快照（snapshotting）
save 900 1      #在900秒(15分钟)之后，如果至少有1个key发生变化，Redis就会自动触发BGSAVE命令创建快照。
save 300 10     #在300秒(5分钟)之后，如果至少有10个key发生变化，Redis就会自动触发BGSAVE命令创建快照。
save 60 10000   #在60秒(1分钟)之后，如果至少有10000个key发生变化，Redis就会自动触发BGSAVE命令创建快照。
2、AOF（append-only file）持久化；appendonly yes开启AOF
	appendfsync always
	appendfsync everysec
	appendfsync no

## Mysql
### shardingsphere JDBC分表：
1、广播表（字典表），同时插入到多个数据表中，保证了字典表的一致性
broadcast-tables:
例：Actual SQL:  db1::: insert into t_dict
Actual SQL:  db2::: insert into t_dict
Logic SQL:  insert into t_dict
2、绑定表：join时避免笛卡尔积：
binding-tables:
- cpac_room_gather_police,cpac_person_gather_police

### Mysql主从复制：
#### Mysql开启binlog
log-bin=mysql-bin
masterslave:
load-balance-algorithm-type: round_robin   或者 random
#### Mysql主从复制的原理：
1、当Master节点进行insert、update、delete操作时，会按顺序写入到binlog中。
2、slave从库连接master主库，Master有多少个slave就会创建多少个binlog dump线程。
3、当Master节点的binlog发生变化时，binlog dump 线程会通知所有的salve节点，并将相应的binlog内容推送给slave节点。
4、I/O线程接收到 binlog 内容后，将内容写入到本地的 relay-log。
5、SQL线程读取I/O线程写入的relay-log，并且根据 relay-log 的内容对从数据库做对应的操作。


spring boot 启动流程:
1、@SpringBootApplication







Java参数传递中，不管传递的是基本数据类型还是引用类型，都是值传递。

BaseController：
	1、通用返回list;
	2、设置请求分页数据;
	3、通用响应返回结果:成功、失败等
	


	

SOLR 、 ElasticSearch分词：
	中文分词器：
		ik_max_word：最细粒度的拆分;
		ik_smart: 最粗粒度的拆分
ElasticSearch	Java API:	
	//构造类型查询条件
	BoolQueryBuilder boolQueryBuilder = new BoolQueryBuilder();
	// .must(QueryBuilder) 		相当于  与   &    =
	//exists表示字段存在，过滤掉null
	boolQueryBuilder.must(QueryBuilders.existsQuery("plateNo"));
	
	// .must not(QueryBuilder) 	相当于  非   ~   !=
	//查询plateNo不为空
	boolQueryBuilder.mustNot(QueryBuilders.termQuery("plateNo",""));
	
	// .should(QueryBuilder) 	相当于  或   |   or	
	BoolQueryBuilder typeQueryBuilder = new BoolQueryBuilder();
	//must连接其他条件，相当于and；should相当于or
	boolQueryBuilder.must(
		typeQueryBuilder.should(QueryBuilders.termQuery("type", 0))
        .should(QueryBuilders.termQuery("type", 1)));
	
	// .filter(QueryBuilder)  	过滤	
	boolQueryBuilder.filter(QueryBuilders.rangeQuery("create_time").gte(startTime));
	boolQueryBuilder.filter(QueryBuilders.rangeQuery("create_time").lte(endTime));




amqp: Advanced Message Queuing Protocol


	
		
		
消息队列MQ主要包含两种模型：点对点（队列）与发布订阅两种模型。		
	队列queue: 先进先出
		消息队列（Queue）
		发送者(Sender)
		接收者(Receiver)
		每个消息只有一个消费者（Consumer）(即一旦被消费，消息就不再在消息队列中)	
	主题topic: 发布-订阅
		主题（Topic）
		发布者（Publisher）
		订阅者（Subscriber）
		每个消息可以有多个消费者：和点对点方式不同，发布消息可以被所有订阅者消费



curl --location --request GET 'http://127.0.0.1:15002/lgi/icons' 
curl --location --request GET 'http://127.0.0.1:15002/lgi/point?oid=330681'


Java多线程(CompletableFuture)：
CompletableFuture<Void> f1 = CompletableFuture.runAsync((() -> {
	//task1
	getApply1(spatialDataList, spatialDataQuery.getBizType(),mht);
}));
CompletableFuture<Void> f2 = CompletableFuture.runAsync((() -> {
	//task2
	getApply2(spatialDataList, spatialDataQuery.getBizType(),mht);
}));
CompletableFuture<Void> f3 = CompletableFuture.runAsync((() -> {
	//task3
	getApply3(spatialDataList, spatialDataQuery.getBizType(),mht);
}));
CompletableFuture<Void> all = CompletableFuture.allOf(f1,f2,f3);
//阻塞，直到所有任务结束。
all.join();
log.info("任务结束");

elasticsearch、kibana(es的web界面)

容器重启、镜像部署

https://github.com/issues?q=is:open language:java label:"good first issue" 

Fork this repository to your own GitHub account.
Clone your fork to your local machine.
Make changes to the code on your local machine.
Test your changes thoroughly.
Commit your changes and push them to your fork.
Create a pull request to merge your changes back into the main repository.


if (null == cardType){
	return "";
}
switch (cardType){}

vscode: 快捷键：rfce 快速新建react function 表示react-function-components-export

idea自动补全等号左边：
光标移动至代码最右边，Ctrl+Alt+V

IDEA接口文档生成插件：Apifox Helper 

mysql面试题：
1、主键的作用：
	1）保证实体的完整性;
	2）加快数据库的操作速度
	3）在表中添加新记录时，ACCESS会自动检查新记录的主键值，不允许该值与其他记录的主键值重复。
	4) ACCESS自动按主键值的顺序显示表中的记录。如果没有定义主键，则按输入记录的顺序显示表中的记录。
2、索引的作用： 
	优点：
	大大提高数据查询速度。
	可以提高数据检索的效率，降低数据库的IO成本，类似于书的目录。
	通过索引列对数据进行排序，降低数据的排序成本降低了CPU的消耗。
	被索引的列会自动进行排序，包括【单例索引】和【组合索引】，只是组合索引的排序需要复杂一些。
	如果按照索引列的顺序进行排序，对order 不用语句来说，效率就会提高很多。
	缺点：
	索引会占据磁盘空间。
	索引虽然会提高查询效率，但是会降低更新表的效率。比如每次对表进行增删改查操作，MySQL不仅要保存数据，还有保存或者更新对应的索引文件。
	维护索引需要消耗数据库资源。
	
	MySQL索引使用的数据结构主要有BTree索引和hash索引。
	对于hash索引来说，底层的数据结构就是哈希表，因此在绝大多数需求为单条记录查询的时候，可以选择哈希索引，查询性能最快；其余大部分场景建议选择BTree索引。
	
	创建索引时需要注意什么？
	非空字段（用0等代替）、索引字段越小越好

	什么情况下不走索引（索引失效）？
	1、使用!= 或者 <> 导致索引失效
	2、类型不一致导致的索引失效
	3、函数导致的索引失效
	4、运算符导致的索引失效
	5、OR引起的索引失效
	6、模糊搜索导致的索引失效
	7、NOT IN、NOT EXISTS导致索引失效
3、explain的作用：
	Type：
	 1、system：系统表，少量数据，往往不需要进行磁盘IO；
	 2、const：常量连接；
	 3、eq_ref：主键索引(primary key)或者非空唯一索引(unique not null)等值扫描；
	 4、ref：非主键非唯一索引等值扫描；
	 5、range：范围扫描；
	 6、index：索引树扫描；
	 7、ALL：全表扫描(full table scan)；
	key:
	 显示mysql实际采用哪个索引来优化对该表的访问	
	 
Redis面试题：
	Redis常见数据类型和应用场景：
	String（字符串）..
	Hash（哈希）
		  Map<String, String> bike1 = new HashMap<>();
		  bike1.put("model", "Deimos");
		  bike1.put("brand", "Ergonom");
		  bike1.put("type", "Enduro bikes");
		  bike1.put("price", "4972");

		  Long res1 = jedis.hset("bike:1", bike1);
		  System.out.println(res1); // 4

		  String res2 = jedis.hget("bike:1", "model");
		  System.out.println(res2); // Deimos

		  String res3 = jedis.hget("bike:1", "price");
		  System.out.println(res3); // 4972

		  Map<String, String> res4 = jedis.hgetAll("bike:1");
		  System.out.println(res4); // {type=Enduro bikes, brand=Ergonom, price=4972, model=Deimos}
	List（列表） lpush  lrange  rpush
		Long count = redisTemplate.opsForList().rightPushAll(key, dataList);
		List<V> list = redisTemplate.opsForList().range(key, 0, -1);
	Set（集合）
	zset（有序集合）
		//kkbm 根据卡口编码 人流量排序
		//插入数据
		Double score = redisTemplate.opsForZSet().score(key,kkbm);
		if(null!=score){
			redisTemplate.opsForZSet().incrementScore(key,kkbm,1);
		}else{
			redisTemplate.opsForZSet().add(key,kkbm,1);
		}
		//获取排行,倒排序
		redisTemplate.opsForZSet().reverseRangeWithScores(key,0,-1);
		
	Redis提供的zset数据类型能够实现这些复杂的排行榜
	Redis分布式锁：利用setnx的互斥性；利用ex避免死锁；释放锁时判断线程标示
	set key value, expire key 100, ttl key 返回剩余秒数
	SETNX 是SET if Not exists的简写: 
		key已经存着，则不会覆盖旧值，并返回0,
		key之前没有，则可以设置成功，并返回1.
	


MyBatis的mapper接口调用时有哪些要求？
1.Mapper接口方法名和mapper.xml中定义的每个sql的id相同；
2.Mapper接口方法的输入参数类型和mapper.xml中定义的每个sql 的parameterType的类型相同；
3.Mapper接口方法的输出参数类型和mapper.xml中定义的每个sql的resultType的类型相同；
4.Mapper.xml文件中的namespace即是mapper接口的类路径


vue 姓名改为不可编辑：
<el-input :disabled="formPerson.rid != null" v-model="formPerson.xm" placeholder="请输入姓名" />





List<Map> list = new ArrayList<>();
Map<String, String> m0 = new HashMap<>();
m0.put("mlphxx", "信息1");
m0.put("mlphbm", "code1");
list.add(m0);
Map<String, String> m1 = new HashMap<>();
m1.put("mlphxx", "信息2");
m1.put("mlphbm", "code2");
list.add(m1);
// .map() 对象转换
List<String> mlphxxList = list.stream().map(x->x.get("mlphbm").toString())
		.collect(Collectors.toList());
String mlphxxs = mlphxxList.stream()
		.collect(Collectors.joining(","));
System.out.println(mlphxxs);

idea --spring.cloud.nacos.discovery.server-addr=114.67.79.57:8848 --spring.cloud.nacos.config.server-addr=114.67.79.57:8848 --spring.cloud.nacos.config.namespace=cq --spring.cloud.nacos.discovery.namespace=cq

18:38:02.455 [main] INFO  c.a.n.c.r.client - [printIfInfoEnabled,60] - 
[1053851c-cc0f-4829-83c1-549b7bc2237a_config-0] 
Try to connect to server on start up, server: 
{serverIp = '114.67.79.57', server main port = 8848}
public static void main(String[] args){
	try (Connection conn = DriverManager.getConnection(
			"jdbc:mysql://localhost:3306/pudong-fangyi", "root", "123456")) {
		if (conn != null) {
			System.out.println("Connected to the database!");
		} else {
			System.out.println("Failed to make connection!");
		}
	} catch (SQLException e) {
		System.err.format("SQL State: %s\n%s", e.getSQLState(), e.getMessage());
	} catch (Exception e) {
		e.printStackTrace();
	}
}


harbor 镜像管理
Jenkins 服务启动
portainer: docker容器web页面展示、日志监控


Typora: markdown编辑器


-- mysql字段拼接
SELECT CONCAT_WS('-',xm,zjhm,mobile) xm ,xm,zjhm,mobile FROM pudong_cpac.cpac_person_gather;


SELECT
	table_rows 
FROM
	information_schema.TABLES 
WHERE
	TABLES.TABLE_NAME = 'cpac_person_gather'


覆盖mybatis pagehelper分页插件：
selectCpacPersonGatherList_COUNT

List<CpacRoomGather> list = cpacRoomGatherMapper.getRoomListByBuildingId(roadNongCode,buildingCode);
List<CpacPersonGather> personList = null;
List<String> houseIds = new ArrayList<String>();
list.stream().forEach(room -> houseIds.add(room.getHouseId()));
personList = cpacPersonGatherService.getListByHouseIds(houseIds.toArray());
Map<String, List<CpacPersonGather>> roomPersonListMap =
personList.stream().collect(Collectors.groupingBy(person -> person.getJzfwid()));


import org.apache.ibatis.annotations.Param;
List<CpacRoomGather> getRoomListByBuildingId(@Param("roadNongCode")String roadNongCode, @Param("buildingCode")String buildingCode);

	
	
接口返回时去掉空值的字段
@JsonInclude(JsonInclude.Include.NON_EMPTY)
public class CpacPersonGather extends BaseEntity{}

事务失效的场景：其实发生最多就是自身调用、异常被吃、异常抛出类型不对这三个了。

ALTER table cpac_person_gather modify person_id VARCHAR(200) first

ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar", "wayz-cpac.jar"]
在启动应用时配置 -Djava.security.egd=file:/dev/./urandom 可以一定程度上加快应用启动。

linux 查看文件
cat filename	(适用于查看内容较少的文件)
more filename  
apt install less
less filename
Linux touch命令用于修改文件或者目录的时间属性，包括存取时间和更改时间。若文件不存在，系统会建立一个新的文件。
Linux pwd（英文全拼：print work directory） 命令用于显示当前工作目录。

Flyway is a version control application to evolve your Database schema easily 
and reliably across all your instances.

# 构建镜像
docker-compose build 
docker-compose build --no-cache
# 创建并启动所有服务：
docker-compose up -d
docker-compose up --build
# docker-compose down可以停止并删除容器、网络(镜像还在)
docker-compose down
# 停止工程中所有服务的容器
docker-compose stop
# 停止工程中指定服务的容器
docker-compose stop nginx
# 显示工程中所有服务的容器正在运行的进程
docker-compose top
# 显示工程中指定服务的容器正在运行的进程
docker-compose top nginx

# 关闭所有环境/模块
./deploy.sh stop

#根据镜像反查dockerfile
docker history --format {{.CreatedBy}} --no-trunc=true 镜像id

Volume 数据卷,冒号”:”前面的目录是宿主机目录(./mysql/conf)，后面的目录是容器内目录(/etc/mysql/conf.d)
volumes:
      - ./mysql/conf:/etc/mysql/conf.d
	  - ./mysql/logs:/logs
      - ./mysql/data:/var/lib/mysql
目录挂载
我们可以在创建容器的时候，将宿主机的目录与容器内的目录进行映射，
这样我们就可以通过修改宿主机某个目录的文件从而去影响容器，
而且这个操作是双向绑定的，也就是说容器内的操作也会影响到宿主机，实现备份功能。
但是容器被删除的时候，宿主机的内容并不会被删除。
如果多个容器挂载同一个目录，其中一个容器被删除，其他容器的内容也不会受到影响。	  

进入容器: docker exec -it container_id sh
	或 docker exec -it -u root container_id(输入容器id的前三位即可) sh
进入容器/执行命令：docker exec -it mysql bash



shardingsphere(sharding-jdbc-spring-boot-starter) 实现数据库读写分离



sass:
Sass Live Compiler install to VsCode (Live Sass compiler)
Create scss(sass) file
Variables: $primaryColor: red;  header {background: $primaryColor;}
Nesting: 
	header {
		background: $primaryColor; 
		button{
			color:blue;
			&:hover{
				background: black;
			}
		}
	}
@import './header' 可以引入其他.scss样式文件
Mixins with custom parametres:
@mixin flexCenter($direction){
	background: blue; 
	flex-direction: $direction;
}
header{
	@include flexCenter(row);
	color: red;
}
.contact{
	@extend header;
	background: yellow; 
}
Calculations(可以加减乘除+-*/):
.contact{
	width: 100vw - 20vw;
}

.parent{
	&.son{
        color: yellow;
    }
    .kids{
    }  
}
在jQuery或者css中，加不加这个空格是有明显的区别哦，两个类之间加空格和不加空格的区别
&.son -> .parent.son
1.当一个标签有两个类的时候，（也就是说这两个了类是同级的）则，在两个类之间不加空格。
.kids -> .parent .kids
2.当这两个类的标签是父子关系，（也可以说是上下级关系）则，在两个类之间必须加空格。





Vault是用来安全的存储秘密信息的工具，
提供了对Token，密码，证书，API key等的安全存储(key/value)和控制功能。
它能处理key的续租、撤销、审计等功能。通过API访问可以获取到加密保存的密码、SSH key、证书等。

Spring Cloud Sleuth
请求一个微服务系统的API接口，这个API接口，
需要调用多个微服务，调用每个微服务都会产生一个新的Span，
所有由这个请求产生的Span组成了这个Trace。 
Annotation：用来及时记录一个事件的，一些核心注解用来定义一个请求的开始和结束。

进入docker容器：
docker exec -it containerId /bin/sh
ls
cat xx.txt
exit

react,redux
dispatch({
  type: "expenses/deleteFinanceCost",
  payload: {
	ids: ids
  },
  callback: (response: ResponseType) => {
  }
});
dispatch触发， type:"expenses/deleteFinanceCost"中
expenses是model.ts中的namespace: 'expenses',
deleteFinanceCost是serice.ts中的function,
payload就是传参

react hook：useState
import React, { useState } from 'react';
count: 变量名
setCount：返回函数setCount
0: 设置初始值为 0
const [count, setCount] = useState(0);
<button onClick={() => setCount(count + 1)}>Click me</button>

react hook：useEffect
useEffect(() => {
	exhibitionInfo()
}, [userData])
当数组中的userData变化时就会调用 useEffect的中的方法：exhibitionInfo()
当useEffect中的数组为空数组[]时，只会在页面加载完时执行一次这个useEffect

 <el-select
	v-model="scope.row.channel_sku"
	filterable
	clearable
	placeholder="请选择"
	class="p5_input"
	allow-create
	default-first-option
  >
	<el-option
	  v-for="(item, key) in scope.row.sku_confusion"
	  :key="key"
	  :label="item"
	  :value="String(item)"
	/>
  </el-select>



CREATE SEQUENCE menu_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
CREATE TABLE "public"."sys_menu" (
  "menu_id" int8 NOT NULL DEFAULT nextval('menu_id_seq'::regclass)
)

<el-select filterable allow-create v-model="ruleForm.usePeriod" placeholder="请选择使用期限" 
	@change="changeUseTime">
	<el-option v-for="dict in dict.type.yzt_use_time"  :key="dict.value" :label="dict.label"
	  :value="dict.value"></el-option>
	  :value="{ value: dict.value, label: dict.label}">
	</el-option>
</el-select>
if (typeof data.roleId=='object'){
	data.roleId = data.roleId.value
}
changeUseTime(e) {
  switch (e.label) {
	case '7天':
	  this.applyForm.usePeriod= 7;
	  break;
	case '1个月':
	  this.applyForm.usePeriod = 30;
	  break;
	case '3个月':
	  this.applyForm.usePeriod = 90;
	  break;
	case '6个月':
	  this.applyForm.usePeriod = 180;
	  break;
	case '1年':
	  this.applyForm.usePeriod = 365;
	  break;
	case '2年':
	  this.applyForm.usePeriod = 730;
	  break;
	case '3年':
	  this.applyForm.usePeriod = 1095;
	  break;
  }
},  


vue父组件监听调用子组件的值：
父vue(index.vue): 
<Button btn-text="Hi from Parent" />
<!-- @updateValue 必须写在引用子组件的同一行才生效 -->
<headerSort @updateValue="onChildUpdate" />
onChildUpdate (newValue) {
  this.descs = newValue;
  console.log('descs======',this.descs);
},
子vue(matrix-lightning-web\src\views\portal\serve\statisticsmap
\components\statisRight\components\headerSort.vue):
this.$emit('updateValue', this.descs);

子vue接收父组件的值
<button>{{btnText}}</button>
--驼峰命名对应父vue中的：btn-text
props:['btnText']
或者
props:{
	btnText{
		type: String,
		required: true,
		default: "DEFAULT BUTTON"
	}
}


this.$nextTick(function() {
	// DOM 更新了
	console.log('finished tick3 ' + new Date().toString(),document.querySelectorAll('.example').length)
})



将本地的冲突文件冲掉，不仅需要reset到MERGE-HEAD或者HEAD,还需要–hard。
没有后面的hard，不会冲掉本地工作区。只会冲掉stage区。
git reset --hard FETCH_HEAD   慎用！会冲掉本地修改的代码
git pull

Git 更新本地冲突：commit your changes or stash them before you can merge
git stash
git pull
git stash pop

warning: LF will be replaced by CRLF in ** 的原因及解决办法
git config core.autocrlf false

git clone -b <branchname> <remote-repo-url>

git切换分支
git checkout branch-name

git pull --rebase, 这里表示把你的本地当前分支里的每个提交(commit)取消掉，并且把它们临时 保存为补丁(patch)(这些补丁放到".git/rebase"目录中)
git rebase 和 git merge 作用基本是相同的，二者的一个重要的区别是：历史提交本版的区别。git rebase可以使得你的分支看起来像是没有经历过合并一样。

Sentinel 对这个问题采取了两种手段:
  1).通过并发线程数进行限制
  2).通过响应时间对资源进行降级(当依赖的资源出现响应时间过长后，
    所有对该资源的访问都会被直接拒绝，直到过了指定的时间窗口之后才重新恢复。)


geometry构建示例：
1、安装postgresql数据库之后，需要安装postgis扩展
2、添加postgis扩展，使之成为支持空间类型的空间数据库
   create extension postgis
3、create table test_map(id int,wkb_geometry geometry)
4、insert into test_map(id,wkb_geometry) values(1,point(121.36232442,31.02324535)::geometry)
5、SELECT t.wkb_geometry,st_asgeojson(wkb_geometry) from test_map t limit 10


--- 指定 srid 为 4326
CREATE TABLE testgeomobj (id serial, geom geometry NOT NULL);

--- Point 对象，如下图id=1
insert into testgeomobj (geom) VALUES ('SRID=4326;POINT(-95.363151 29.763374)');

--- MultiPoint 对象，如下图id=2
insert into testgeomobj (geom) VALUES ('SRID=4326;MULTIPOINT(-95.4 29.8,-96 30)');

--- LineString 对象，如下图id=3
insert into testgeomobj (geom) values ('SRID=4326;LINESTRING(-71.1031880899493 42.3152774590236,-71.1031627617667 42.3152960829043,-71.102923838298 42.3149156848307,-71.1023097974109 42.3151969047397,-71.1019285062273 42.3147384934248)');

--- MultiLineString 对象，如下图id=4
insert into testgeomobj (geom) values ('SRID=4326;MultiLineString (
(-71.1031880899493 42.3152774590236,-71.1031627617667 42.3152960829043,-71.102923838298 42.3149156848307,-71.1023097974109 42.3151969047397,-71.1019285062273 42.3147384934248),
(-71.1766585052917 42.3912909739571, -71.1766820268866 42.391370174323896, -71.1766063012595 42.3913825660754, -71.17658265830809 42.391303365353096)
)');

--- Polygon 对象，如下图id=8
insert into testgeomobj(geom) values ('SRID=4326;POLYGON (
(-71.1776585052917 42.3902909739571, -71.1776820268866 42.3903701743239, -71.1776063012595 42.3903825660754, -71.1775826583081 42.3903033653531,-71.1776585052917 42.3902909739571)
)');

--- MultiPolygon 对象，如下图id=9
insert into testgeomobj(geom) values ('SRID=4326; MultiPolygon (
((-71.1776585052917 42.3902909739571, -71.1776820268866 42.3903701743239, -71.1776063012595 42.3903825660754, -71.1775826583081 42.3903033653531,-71.1776585052917 42.3902909739571)),
((-71.1766585052917 42.3912909739571, -71.1766820268866 42.391370174323896, -71.1766063012595 42.3913825660754, -71.17658265830809 42.391303365353096, -71.1766585052917 42.3912909739571))
)');



坐标系：EPSG:4326(WGS84)
投影：EPSG:3857



nacos集群搭建：
1、分别配置3个nacos服务，\nacos\conf\application.properties 配置端口、外部数据源
2、3个nacos服务中的\nacos\conf\cluster.conf 中配置3个服务的ip:port
3、nginx中配置
   upstream nacoscluster{
     server nacos服务1的ip:port
	 server nacos服务2的ip:port
	 server nacos服务3的ip:port
   }
   server{
     listen  8847;
	 server_name  localhost;
	 location /nacos/{
	   proxy_pass http://nacoscluster/nacos/;
	 }
   }
4、浏览器访问：localhost:8847/nacos/


浦东防疫项目小结：
前端：
node 版本 v14
npm i 安装依赖
yarn dev

池州项目小结：
前端：
npm install -g yarn
yarn install
yarn dev
后端：
确保nacos改成自己的，具体代码在 LauncherConstant 文件中的 NACOS_DISCOVERY_NAME_SPACE_DEV



target: `http://114.67.78.94:8882/yzt-cloud`,

若依使用小结：
1、配置F:\soft\nacos-server-2.0.2\nacos\conf\application.properties 中的mysql数据源
2、启动nacos之后，在 http://127.0.0.1:8848/nacos  配置管理-配置列表 
	导入nacos配置（新建命名空间）
	编辑 ruoyi-gateway-dev.yml 等文件 修改 redis 等配置
spring:
  cloud:
    nacos:
	   config:
	     namespace: public | dev
		 ephemeral: false #永久实例，即使宕机也不会删除实例
		 
打开运行基础模块（启动没有先后顺序）
RuoYiGatewayApplication （网关模块 必须）
RuoYiAuthApplication （认证模块 必须）
RuoYiSystemApplication （系统模块 必须）
RuoYiMonitorApplication （监控中心 可选）
RuoYiGenApplication （代码生成 可选）
RuoYiJobApplication （定时任务 可选）
RuoYFileApplication （文件服务 可选）
若依微服务版打包部署：		 
1、双击 idea->maven->ruoyi(root)->package 打包	 
2、java -Dfile.encoding=utf-8 -jar ruoyi-gateway.jar   (cmd中运行,设置encoding修复启动报错malformed)
   java -Dfile.encoding=utf-8 -jar ruoyi-auth.jar 	
   java -Dfile.encoding=utf-8 -jar ruoyi-modules-system.jar   
   java -Dfile.encoding=utf-8 -jar wayz-beiwaitan.jar  
3、前端打包部署(npm run build:prod)：
	Nginx中配置：
		location /stage-api/ {
			proxy_set_header Host $http_host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header REMOTE-HOST $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_pass http://localhost:8080/;
		}
		
		location /prod-api/ {
			proxy_set_header Host $http_host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header REMOTE-HOST $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_pass http://localhost:8080/;
		}		 
	nginx -s reload	
	nginx -s stop	
	start nginx
	tasklist /fi "imagename eq nginx.exe"
		 
systemctl start mysql


怎么查看MySQL语句有没有用到索引？
EXPLAIN SELECT * FROM table;
type：type 字段比较重要, 它提供了判断查询是否高效的重要依据依据. 
通过 type 字段, 我们判断此次查询是 全表扫描 还是 索引扫描 等。
如const(主键索引或者唯一二级索引进行等值匹配的情况下),
ref(普通的⼆级索引列与常量进⾏等值匹配),index(扫描全表索引的覆盖索引) 。
通常来说, 不同的 type 类型的性能关系如下:
ALL < index < range ~ index_merge < ref < eq_ref < const < system
ALL 类型因为是全表扫描, 因此在相同的查询条件下, 它是速度最慢的.




docker: 
  volumes : 容器可以通过volumes访问主机的数据


cls ：clear the terminal screen 

Metrics：是一个给Java提供度量工具的包，在JAVA代码中嵌入Metrics代码，可以方便的对业务代码的各个指标进行监控。
Influxdb： 是Go语言写的一个时序型数据库。这里我们可以用来存储上报的监控数据。
Grafana： 是一个非常好看的监控界面。它可以去数据源（influxdb）中load数据进行实时的展示。


docker 提供了数据持久化的机制为 volumes，即为 挂载。
volumes：提供了将容器的特定文件系统路径连接回主机的能力

事务的实现：本地有日志记录表，undo insert ->do delete


nacos、ribbon

springcloud:
  Eureka: 服务注册发现(改为：nacos)
    #指定服务名称
	  spring:
	    application:
		  name: hello-service-provider
  Ribbon: 负载均衡(可以配置多个ip:端口，接口调用就通过服务名称访问)
  Feign: 
    使用接口方式调用服务，替代 restTemplate.exchage(...)
	服务提供方:
	  还是一样。@RequestMapping("/demo/getHost")
    服务使用方：
	  接口@FeignClient注解指定服务名来绑定服务（底层通过ribbon来将应用服务名称解析成ip:port调用请求）
      @FeignClient(value = "hello-service-provider")
	  public interface HelloServiceFeign {
	    // /demo/getHost就是服务提供方的实际uri
	    @RequestMapping(value = "/demo/getHost", method = RequestMethod.GET)
		public String getHost(String name);
	  }
	  @Autowired直接注入上面定义的HelloServiceFeign service实例
	  service.getHost(name); 
	  然后就能调用到HelloServiceFeign中的getHost对应的value中的接口路径：/demo/getHost
	  
	  
	sentinel：熔断、降级
	seata:分布式事务(性能不太高，常用于支付场景)



typescript:
  interface Person{
	firstName:string;
	lastName:string;
	gender?:string;  //?号表示 可选，即这个参数可以不传。
  }
const 花括号简写方式
如果需要声明多个const变量的时候，很多时候我们都是变量一个个声明的，
这样的话，我们的代码显的非常难看。下面这种方式可以进行简写
简写前：
const name = app.name;
const version = app.version;
const type = app.type;
简写后：
const { name, version, type } = app;

let input = [1, 2];
let [first, second] = input;
console.log(first); // outputs 1
console.log(second); // outputs 2


npm install --cache /tmp/empty-cache

npm install --legacy-peer-deps

JpaRepository extends PagingAndSortingRepository 
which in turn extends CrudRepository.
JpaRepository 扩展了 PagingAndSortingRepository，后者又扩展了 CrudRepository。
Their main functions are:
CrudRepository mainly provides CRUD functions.
PagingAndSortingRepository provides methods to do pagination and sorting records.
JpaRepository provides some JPA-related methods such as flushing the persistence context and deleting records in a batch.


IntelliJ IDEA: StackOverflowError on Build Project
Adding -Xss4m to the build process VM options should help
：setting -> Build,Execution -> compiler -> shared..

JSP中使用ES6模板字符串
必须在jsp中将模板字符串的${}进行转义，前面加个斜杠写成\${}，
跟EL表达式区分开来就可以了。

$('#exportForm').submit(function(e){
    e.preventDefault();
    e.stopImmediatePropagation();
    $.ajax({
        type: "POST",
        url: $(this).attr( 'action' ),
        data: $(this).serialize(),
        success: function( response ) {
            console.log( response );
        }
    });
    return false;
});

排行版的实现，一般使用redis的zset数据类型。

索引失效的场景：
1. 查询条件包含or，可能导致索引失效
2. 如何字段类型是字符串，where时一定用引号括起来，否则索引失效
3. like通配符可能导致索引失效。
4. 联合索引，查询时的条件列不是联合索引中的第一个列，索引失效。
5. 在索引列上使用mysql的内置函数，索引失效。
6. 对索引列运算（如，+、-、*、/），索引失效。
7. 索引字段上使用（！= 或者 < >，not in）时，可能会导致索引失效。
8. 索引字段上使用is null， is not null，可能导致索引失效。
9. 左连接查询或者右连接查询查询关联的字段编码格式不一样，可能导致索引失效。
10. mysql估计使用全表扫描要比使用索引快,则不使用索引。

现代操作系统使用虚拟内存，即虚拟地址取代物理地址，使用虚拟内存可以有2个好处：
虚拟内存空间可以远远大于物理内存空间
多个虚拟内存可以指向同一个物理地址
零拷贝实现思想，就利用了虚拟内存这个点：
多个虚拟内存可以指向同一个物理地址，
可以把内核空间和用户空间的虚拟地址映射到同一个物理地址，
这样的话，就可以减少IO的数据拷贝次数啦

$(document).on('mousemove',".className",function(){
	...
})
The mousemove event is sent to an element when the mouse pointer 
moves inside the element. 
Any HTML element can receive this event.
当鼠标指针在元素内移动时，mousemove 事件被发送到元素。
任何 HTML 元素都可以接收此事件。



How to empty a redis database?
FLUSHDB - clears currently active database
FLUSHALL - clears all the existing databases

feign  header中传token (自定义拦截器)

feign调用多个服务 传参、异常处理（fallbackFactory）
索引类型
ExecutorService 异常处理（如何处理数据丢失）

What is Overloading and Overriding?
When two or more methods in the same class have the same name 
but different parameters, it’s called Overloading.
When the method signature (name and parameters) are the same in the superclass 
and the child class, it’s called Overriding.

ArrayList  VS  LinkedList
1) ArrayList internally uses a dynamic array to store the elements.	
LinkedList internally uses a doubly linked list to store the elements.
2) Manipulation with ArrayList is slow because it internally uses an array. 
If any element is removed from the array, all the bits are shifted(位移) in memory.	
Manipulation with LinkedList is faster than ArrayList 
because it uses a doubly linked list, so no bit shifting is required in memory.
3) An ArrayList class can act as a list only because it implements List only.	
LinkedList class can act as a list and queue both 
because it implements List and Deque interfaces.
4) ArrayList is better for storing and accessing data.	
LinkedList is better for manipulating data.


Spring有如下优点：
1.低侵入式设计，代码污染极低
2.独立于各种应用服务器，基于Spring框架的应用，可以真正实现Write Once,Run Anywhere的
承诺
3.Spring的DI机制降低了业务对象替换的复杂性，提高了组件之间的解耦
4.Spring的AOP支持允许将一些通用任务如安全、事务、日志等进行集中式管理，从而提供了更好
的复用
5.Spring的ORM和DAO提供了与第三方持久层框架的良好整合，并简化了底层的数据库访问
6.Spring并不强制应用完全依赖于Spring，开发者可自由选用Spring框架的部分或全部    


请求统一通过 API 网关（Zuul）来访问内部服务。
网关接收到请求后，从注册中心（Eureka）获取可用服务。
由 Ribbon 进行均衡负载后，分发到后端具体实例。
微服务之间通过 Feign 进行通信处理业务。
Hystrix 负责处理服务超时熔断。
Turbine 监控服务间的调用和熔断相关指标。


ExecutorService executorService = Executors.newFixedThreadPool(1);
Future future = executorService.submit(new Callable(){
	public Object call() throws Exception {
		Map map = new HashMap();
		map.put("code","000");
		System.out.println("Asynchronous Callable ..");
		return map;
	}
});
Map result = (Map)future.get();

云服务器mysql:
username: cq
password: Cq@Passw0rd
云服务器redis:
password: cq123456

# 安装yarn
npm install -g yarn
# 下载依赖
yarn install
# 启动
yarn run serve
# 编译项目
yarn run build
# Lints and fixes files
yarn run lint

search in Vim:
Press /.
Type the search pattern.
Press Enter to perform the search.
Press n to find the next occurrence or N to find the previous occurrence.

free -g
cat /etc/*elease

$2a$10$ZLhnHxdpHETcxmtEStgpI./Ri1mksgJ9iDP36FmfMdYyVg9g0b2dq
There are three fields separated by $:
The “2a” represents the BCrypt algorithm version
The “10” represents the strength of the algorithm
The “ZLhnHxdpHETcxmtEStgpI.” part is actually the randomly generated salt. Basically, the first 22 characters are salt. The remaining part of the last field is the actual hashed version of the plain text
Also, be aware that the BCrypt algorithm generates a String of length 60

$.ajax{
	async: false   //Other code waiting for this to finish
}
var phpData = (function get_php_data() {
  var php_data;
  $.ajax({
    url: "http://somesite/v1/api/get_php_data",
    async: false, 
    //very important: else php_data will be returned even before we get Json from the url
    dataType: 'json',
    success: function (json) {
      php_data = json;
    }
  });
  return php_data;
})();



//生成自签名证书
keytool -genkeypair -alias baeldung -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore baeldung.p12 -vali

// 配置 URL 访问权限
@Override
protected  void configure(HttpSecurity http) throws Exception {
	http.authorizeRequests() // 开启 HttpSecurity 配置
		.antMatchers("/admin/**").hasRole("ADMIN") // admin/** 模式URL必须具备ADMIN角色
		.antMatchers("/user/**").access("hasAnyRole('ADMIN','USER')") // 该模式需要ADMIN或USER角色
		.antMatchers("/db/**").access("hasRole('ADMIN') and hasRole('DBA')") // 需ADMIN和DBA角色
		.anyRequest().authenticated() // 用户访问其它URL都必须认证后访问（登录后访问）
		.and().formLogin().loginProcessingUrl("/login").permitAll() // 开启表单登录并配置登录接口
		.and().csrf().disable(); // 关闭csrf
}

WebSecurity web
web.ignoring().antMatchers("/css/**");  //anyRequest();
ingore是完全绕过了spring security的所有filter，相当于不走spring security


查看当前所属分支
git branch -vv

cd /xx/xx
git clone git@github.com:chengqun2/chess.git
git checkout -b newBranch
git add .
git commit -m '注释'
git remote
git push origin newBranch

git取消commit; HEAD^的意思是上一个版本
git reset --soft HEAD^

403 Forbidden
Spring Security CSRF 保护默认是开启的，那么在 POST 方式提交表单的时候就必须验证 Token，如果没有，
那么自然也就是 403 没权限了

spring-security 跨域,除了@CrossOrigin外，还需要配置WebSecurityConfig

yum install java-1.8.0-openjdk

Error: PostCSS received undefined instead of CSS string
问题原因
node-sass 和 sass-loader 版本与当前的不兼容，安装对应版本的包即可。
解决方案
npm uninstall sass-loader
npm install sass-loader


-webkit-mask


磁盘清理：
G:\downloads\spacesniffer_1_3_0_2

查看服务：ps -ef | grep -i redis （或：ps -aux|grep redis）
$ grep -i "linux" welcome.txt


p:nth-child(2)
p:nth-child(odd) {
  background: red;
}
p:nth-child(even) {
  background: blue;
}

<style> 
div {
  width: 100px;
  height: 100px;
  background-color: red;
  animation: example 4s linear infinite;
}

@keyframes example {
  from {transform: rotate(0deg);}
  to {transform: rotate(360deg);}
}

@keyframes example {
  0%   {background-color: red;}
  25%  {background-color: yellow;}
  50%  {background-color: blue;}
  100% {background-color: green;}
}

</style>

docker(centos /data / ..)
docker start **CONTAINER ID**

telnet ip port 
telnet 50.144.0.47 8089
退出telnet. 退出telnet的命令:ctrl+]，然后再输入q就可以退出了
wget ip:port

centos安装docker:
yum install docker-ce docker-ce-cli containerd.io

使用docker安装mysql：
docker images
docker pull mysql:5.6
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.6
netstat -na|grep 3306
docker ps


systemctl start postgresql-13.service

1.15.90.81

yum install postgresql12 postgresql12-server postgresql12-contrib postgresql12-libs -y

sudo yum install postgresql-server postgresql-contrib
sudo postgresql-setup initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo -u postgres psql -c "SELECT version();"
sudo systemctl restart postgresql
ss -nlt | grep 5432
create user admin password 'admin';
GRANT ALL PRIVILEGES ON DATABASE test_db TO admin;
ALTER USER admin WITH SUPERUSER;

postgres -V
CTRL+ALT+T change to superuser
systemctl stop postgresql-9.5.service
yum remove postgresql*

docker login : chengqun710   ww8459526

CI: Continuous integration（持续集成）
持续集成主要是在代码更改时自动分支合并、
	构建并执行一系列的测试（包括单元测试、集成测试、端到端测试等），
	确保这些变更不会破坏原来的应用。
CD: Continuous delivery（持续交付）
持续交付和部署则是 CI 测试通过之后把构建结果存档、
	发布到预布环境和生产环境、最后再进行验收测试的过程。

a pod is running at least a container
	
http://localhost:9090/test/22
@RequestMapping("/test/{id}")
public Map test(@PathVariable("id") Long id) {
	Map map = new HashMap();
	map.put("id",id);
	return map;
}

幂等性实现方案:
1、防重表
2、redis等


所谓第三方登录，实质就是 OAuth 授权:
1. A 网站让用户跳转到 GitHub。
2. GitHub 要求用户登录，然后询问"A 网站要求获得 xx 权限，你是否同意？"
3. 用户同意，GitHub 就会重定向回 A 网站，同时发回一个授权码。
4. A 网站使用授权码，向 GitHub 请求令牌。
5. GitHub 返回令牌.
6. A 网站使用令牌，向 GitHub 请求用户数据。



写SQL尽量先查询和过滤数据量小的表，再去join大的表
mysql explain使用：
extra列：
Using index：使用覆盖索引，表示查询索引就可查到所需数据，不用扫描表数据文件，往往说明性能不错。
Using Where：在存储引擎检索行后再进行过滤，使用了where从句来限制哪些行将与下一张表匹配或者是返回给用户。
Using temporary：在查询结果排序时会使用一个临时表，一般出现于排序、分组和多表 join 的情况，查询效率不高，建议优化。
Using filesort：对结果使用一个外部索引排序，而不是按索引次序从表里读取行，一般有出现该值，都建议优化去掉，因为这样的查询 CPU 资源消耗大。

单点登录的标准做法:单独部署一个认证中心 (Apereo CAS 是一个企业级单点登录系统)



JDK：Java Development Kit
JRE：Java Runtime Environment

oracle分区（partition）查询

wait 可以释放当前线程对 lock 对象锁的持有，而 sleep 则不会

what is springcloud?


mysql修改端口，编辑/etc/my.cnf文件,修改端口，重启即可


SpaceSniffer 磁盘清理工具

Vue(vue,vuex,vue-rounter) 全家桶

html - CSS如何使<TD>固定高度？ td里面加个div
<td>
  <div style="height: 50px; overflow:auto;">
      ...
  </div>
</td>



scss、less
axios(api调用)
element-ui、iview、ant-ui
webpack
nginx



IE8 不支持vw,vh（宽度建议使用百分比）;不支持flex布局
div中 两个span设置垂直居中，可以先 div span{vertical-align:middle;margin-top:10px;} 
悬浮显示使用hover：
父hover后 改变子
.item-1:hover .item-1-child{
    background-color:#50ff00;
}
相邻同级：
.item-1:hover +.item-2{
    background-color:#50ff00;
}
不相邻同级：
.item-1:hover ~.item-3{
    background-color:#50ff00;
}


1、新建一个react项目：
npx create-react-app my-app
cd my-app
npm start

display: grid;
grid-template-columns: 100px 100px 100px;
grid-template-rows: 100px 100px 100px;
/* grid-template-columns: repeat(3, 33.33%);
  grid-template-rows: repeat(3, 33.33%); */
/*grid-template-columns: repeat(2, 100px 20px 80px);*/
/*2fr是1fr的两倍，fr是比例的意思，fraction*
grid-template-columns: 1fr 2fr;


display: flex;
/* flex-direction 决定主轴的方向 row(默认)|row-reverse|column|column-reverse*/
/* flex-direction: row; */
/* flex-wrap决定当排列不下时是否换行以及换行的方式,nowrap(默认)|wrap|wrap-reverse */
/* flex-wrap:wrap; */
flex-grow:1; 指定了flex容器中剩余空间的多少应该分配给项目（flex增长系数），默认0
order:1; order属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。不写这个属性，box放在最前。
justify-content: flex-start | flex-end | center | space-between | space-around; //水平方向
align-items: flex-start | flex-end | center | baseline | stretch;  //垂直方向
align-content: flex-start | flex-end | center | space-between | space-around | stretch;  //水平+垂直
flex-shrink:如果所有项目的flex-shrink属性都为1，当空间不足时，都将等比例缩小。如果一个项目的flex-shrink属性为0，其他项目都为1，则空间不足时，前者不缩小。



1、oracle利用 to_number判断是否是数字
CREATE OR REPLACE FUNCTION isnumeric(str IN VARCHAR2)
    RETURN NUMBER
IS
    v_str FLOAT;
BEGIN
    IF str IS NULL
    THEN
       RETURN 0;
    ELSE
       BEGIN
          SELECT TO_NUMBER (str)
            INTO v_str
            FROM DUAL;
       EXCEPTION
          WHEN INVALID_NUMBER
          THEN
             RETURN 0;
       END;
       RETURN 1;
    END IF;
END isnumeric;


Oracle的CONCAT函数不像MySql那样支持三个参数的拼接，需要把SQL语句修正为：
and e.empId like CONCAT(CONCAT('%',#{empId}),'%')
或者 and e.empId like '%' || #{empId} ||'%';  以上仅对Oracle有效！

cmd查看class文件：
javap -verbose Hello.class


redis-cli -h 127.0.0.1 -p 6379 -a myPassword

前端项目部署：
1、打包项目：npm run build
2、将打包后的dist目录下项目进行nginx配置：
		location / {
            root   F:\git\vue-manage-system\dist;
            index  index.html index.htm;
        }
3、访问nginx的ip+server配置的端口即可打开页面

G:\downloads\nginx-1.18.0\nginx-1.18.0
windows系统下nginx：
启动：start nginx
停止：nginx.exe -s quit
重新加载配置文件(nginx.conf)：nginx.exe -s reload
重新打开日志：nginx.exe -s reopen
查询版本：nginx -v

js:
const body = document.body;
const div = document.querySelector("div")
console.log(div.textContent)   //display为none也会打印出来
console.log(div.innerText)  //只打印页面展示的内容，隐藏的不显示
div.innerHTML("<strong>Hello</strong>") //可以读出属性strong  //加粗
body.append(div)

attribute是HTML标签上的特性，它的值只能够是字符串； id、name、type等
property是DOM中的属性，是JavaScript里的对象；



响应式布局：（通过 link里的media设置，根据不同屏幕宽度，引入不同的css）
<link rel="stylesheet" type="text/css" href="index.css"/>
<link rel="stylesheet" type="text/css" href="index01.css" media="screen and (max-width:1024px) and (min-width:720px)"/>
<link rel="stylesheet" type="text/css" href="index02.css" media="screen and (max-width:720px)"/>


npm install --save vuex


<link rel="stylesheet" href="//res.layui.com/layui/dist/css/layui.css"  media="all">
<div class="layui-progress">
  <div class="layui-progress-bar" lay-percent="40%"></div>
</div>
温馨提示：进度条的宽度是 100% 适配于它的父级元素，如上面的进度条是在一个 300px 的父容器中。
layer.tips(content,elem,{tips:[2,"#fff"],time:0})   支持上右下左四个方向，通过1-4进行方向设定

css:
box-sizing: content-box;  //content-box  是默认值
box-sizing: border-box;
//border: solid #5B6DCD 10px;
//padding: 5px;
ie7:*margin-top ,加个 *号，只在ie7下生效
align-items:center flex布局下 垂直居中
设置文字背景渐变色：
span {
	background: linear-gradient(to right, red, blue);
	-webkit-background-clip: text;
	color: transparent;
}

yarn和npm命令对比
npm install === yarn 
npm install taco --save === yarn add taco
npm uninstall taco --save === yarn remove taco
npm install taco --save-dev === yarn add taco --dev
npm update --save === yarn upgrade

babel:可以将 es6 转成 es5 文件

eclipse debug启动老是跳转到断点，提示SilentExitException
解决方法：在eclipse中选择Window->Preference-> Java ->Debug，将“Suspend execution on uncaught exceptions”的勾去掉即可。

LVS是Linux Virtual Server的简称，也就是Linux虚拟服务器。LVS提供的负载均衡技术


Error running 'All in project-name': Command line is too long. Shorten command line for All in project-name or also for JUnit default configuration.
.idea/workspace.xml
<component name="PropertiesComponent">
添加：
    <property name="dynamic.classpath" value="true" />

idea右侧 Gradle build->bootJar 即可打jar包	
	

Nginx动静分离配置 :
location 匹配uri（域名后面的 如 www.qq.com/a/b 的 /a/b）
server_name 域名
访问静态资源（如 文件路径：/data/image/a.png）
location /image/{
	root /data/;
	autoindex on;  (开启autoindex 自动列出文件夹中的所有文件)
}
http://xx.com/image/a.png
location /ydpcs{
	proxy_pass http://50.144.0.47:8089/ydpcs;
}


github搜项目： in:name spring boot stars:>1000 pushed:>2019-09-01

redis安装：yum install gcc-c++
redis后台启动 修改redis.conf->daemonize yes
[root bin]# redis-server config/redis.conf    (redis启动)
关闭redis:shutdown
退出redis:exit
springboot  pom:spring-boot-starter-data-redis  2.x 后使用了 lettuce操作redis(jedis ->lettuce)

oracle 查询同车牌号时间最大的那一条数据
select *
  from (select row_number() over(partition by hphm order by time desc) rn, 表.*
           from  表)  where rn = 1

js:
The unshift() method adds one or more elements to the beginning of an array and returns the new length of the array.

uniapp:
props 接收其他组件的属性值
HBuilder easy-git插件


chrome css
-webkit-background-clip:text;

mybatis:
<if test="type != null and type == '1'.toString()">
</if>

The steps in Vue lifecycle are 
beforCreate, created, beforeMount,
 mounted, beforeUpdate, updated, beforeDestroy, destroyed.


cmd操作git
cd D:\xx
git status 
git pull
git add .
git commit -m "注释"
git push


jdk bin中的jvisualvm.exe 可以根据pid查询java程序所在目录

ApplicationRunner：继承 ApplicationRunner 接口的类的 
	run方法会(在Spring容器启动完成时)被自动执行（前提是这个类被Spring 管理）

定时任务：
	@EnableScheduling
	@Scheduled(fixedRate = 1000 * 60)

1、idea 文件编码问题（切换到gbk，再切回utf8即可）
2、IDEA运行项目时，出现Error:(4, 10) java: 程序包javax.websocket.server不存在
点击 + ,找到 D:\apache-tomcat-7.0.96-windows-x64\apache-tomcat-7.0.96\lib\websocket-api.jar
3、IDEA - 配置Tomcat并运行Web项目。run->edit configuration-> + Tomcat server
4、idea查看svn地址：subversion -> relocate
5、idea web添加lib ,Project Structure -> Modules-> Dependencies-> + library
6、ctrl + r: 当前文件内容替换
7、ctrl+shift+u idea大小写切换
8、idea web项目导出war包：Project Structure -> Artifacts -> 
	type: Web application Archive  。点击build 自动构建war包
9、配置svn：File->Settings->Version Control ->Subversion->关联已安装的TortoiseSVN\bin\svn.exe
10、配置java web项目 Project Structure -> artifacts -> output root 下面 增加 WEB-INF
11、idea -> project structure -> artifacts ->
    web application exploded：这个是以文件夹形式发布项目，发布项目时就会自动生成文件夹在指定的output directory；
	web application archive：就是war包形式,将项目打成一个war包在指定位置
	
idea插件 Alibaba Java Coding Guidelines
	
lay-search：可搜索的下拉框，根据 lay-filter的值进行查询
form.on('select(lay-filter的值)',function(data){
	console.info(data.value);
})
<form class="layui-form">
	<div class="layui-form-item">
		<div class="layui-inline col-sm-12">
			<select id="TemplateOptions" name="effectsType" class="layui-select" lay-verify="required" lay-filter="selectTemplate" lay-search>
				<option value="">实体要素内容选择</option>
			</select>
		</div>
	</div>
</form>


每个请求按照访问 Ip（即Nginx的前置服务器或客户端IP）的 hash结果分配，
这样每个访客会固定访问一个后端服务器，可以解决 session 一致问题。
upstream zhang21 {
    ip_hash;
    server 192.168.1.11:7777;
    server 192.168.1.22:8888;
    server 192.168.1.33:9999;
}
location / {
    root html;
    index index.html index.htm;
    proxy_pass http://zhang21(upstream名称）;
}



npm install -g @vue/cli --force

npm init -y
npm install express  (安裝dependency)
npm run (scripts中的command)

redis console 
select 2
flush db 清空redis库

::-webkit-scrollbar — 滚动条.

Windows中杀死占用某个端口的进程：
netstat -ano | findstr 80 //列出进程极其占用的端口，且包含 80
taskkill -PID <进程号> -F //强制关闭某个进程

阿里云 centos服务器
139.196.145.61
root 

wget -P /usr/java 网址
yum install 
FlashphonerWebCallServer =172.19.238.240

mybatis二级缓存：
mybatis.xml：
<settings>
	<setting name="cacheEnabled" value="true" />
</settings>
mapper.xml
<mapper>
	<cache
        eviction="LRU"
        flushInterval="60000"   //毫秒
        size="1024"
        readOnly="true"
    />
</mapper>

nodemon : 自动重启Nodejs项目

vim:
HJKL 左下上右
tar -zxvf linux解压 .tgz 压缩文件

css移动（第一个参数：左右，第二个参数：上下）：
transform:translate(-25px,-25px);

rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov
rtsp://50.144.10.30/1234569.sdp

npm install -g cnpm --registry=https://registry.npm.taobao.org
淘宝的npm镜像代替国外的资源，用cnpm命令来全部代替npm
cnpm install 
cnpm run 

G:\downloads\node-video-master\node-video-master
nodejs启动项目
npm install 
node app.js
打包：
C:\Users\HP\.pkg-cache\v2.6
//pkg -t win app.js
pkg -t win package.json

234 141

vlc播放器播放 rtsp视频流

css
tr:nth-child(odd)
表示HTML表格中的奇数行。

Git 
Workspace：工作区 
Index / Stage：暂存区
Repository：仓库区（或本地仓库）
Remote：远程仓库

微人事 密码123
阿里云服务器：
106.15.51.152

idea当前页替换：ctrl + R 

登录
mysql -uroot -p 初始化密码
修改密码
alter user 'root'@'localhost' identified by 'xxxxx';

java 操作流  后打开的先关闭

在laydate.render中加,trigger: 'click'，就可以避免闪退了

layui skin
cat /etc/issue 查看centos版本

$( "#myselect option:selected" ).text();

vuejs 框架：https://nuxtjs.org/

Photoshop之Cutterman一键切图插件

<script defer src="./script.js"></script> defer：页面加载完再加载js

oracle：select wm_concat(name) name from test;

() =>  等价于  function()

springboot项目启动失败，Unable to start web server;拉到最下面

在my.ini修改：
#开启主从复制，主库的配置
log-bin= mysql3306-bin
sql:
grant replication slave on *.* to 'slave01'@'127.0.0.1'identified by '123456';
flush privileges;

"use strict"; Defines that JavaScript code should be executed in "strict mode".

@Controller 控制器（注入服务）
@Service 服务（注入dao）
@Repository dao（实现dao访问）
@Component （把普通pojo实例化到spring容器中，相当于配置文件中的<bean id="" class=""/>）
@Component泛指组件，当组件不好归类的时候，我们可以使用这个注解进行标注

vuejs  
<div :class="temp>16?'warm':'cold'"></div>
<input @keypress="functionA"  />
<li v-for="(item,index) in list" v-on:click="test()" 
  :class="{'left-content':item.type==0,'right-content':item.type==1}">
	<div> {{item.id}}</div>
</li>

data() {
    return {
      todoCount: 0,
	};
}	
<div v-show="todoCount > 0">

挖矿原理

Oracle 不同数据库表联合查询(需要dba):
file->new-> database link

大于号：$('parent > childchild')表示获取parent下的所有下一级childchild

oralce substr("ABCDEFG", -3); //返回：EFG，注意参数-3，为负值时表示从尾部开始算起，字符串排列位置不变。

String header = request.getHeader("");

@Value("")
@Bean的方法的返回值识别为Spring Bean，并注册到容器中，归入IoC容器管理
全局异常的处理：@ControllerAdvice + @ExceptionHandler(Exception.class)
@ControllerAdvice
public class SpringControllerAdvice {
  @ExceptionHandler(Exception.class)
  public ModelAndView exception(Exception e) {
    e.printStackTrace();
    return new ModelAndView("error");
  }
}

阿里云服务器：
106.15.51.152
Ww8459526
chengqun.xyz

微信小程序:
<button size="mini" bindtap="save">保存</button>
catchtap不允许事件冒泡，bindtap允许
<input bindinput="bindKeyInput" value="{{inputValue}}" auto-focus placeholder="将会获取焦点"/>
  post请求：
	method: 'POST',
	'content-type':'application/x-www-form-urlencoded'


幂等性：就是用户对于同一操作发起的一次请求或者多次请求的结果是一致的，
不会因为多次点击而产生了副作用。
    为需要保证幂等性的每一次请求创建一个唯一标识token, 先获取token, 
并将此token存入redis, 请求接口时, 将此token放到header或者作为请求参数请求接口, 
后端接口判断redis中是否存在此token:如果存在, 正常处理业务逻辑, 并从redis中删除此token, 
那么, 如果是重复请求, 由于token已被删除, 则不能通过校验, 返回请勿重复操作提示如果不存在, 
说明参数不合法或者是重复请求, 返回提示即可


像素px是相对于显示器屏幕分辨率而言的。(引自CSS2.0手册)
em是相对长度单位。相对于当前对象内文本的字体尺寸。(引自CSS2.0手册)
vw：视窗宽度的百分比（1vw 代表视窗的宽度为 1%）
vh：视窗高度的百分比
vmin：当前 vw 和 vh 中较小的一个值
vmax：当前 vw 和 vh 中较大的一个值

js两次!! 强制转成boolean类型

分布式ID都有哪些生成方式？
1、基于Java的UUID ,不推荐
2、基于数据库自增ID ,不推荐
3、基于数据库集群模式(设置起始值和自增步长) ,不推荐
4、基于数据库的号段模式
id biz_type max_id step version 
 1   101     1000  2000    0
5、基于Redis模式 (利用redis的 incr命令实现ID的原子性自增)
   set seq_id 1  // 初始化自增ID为1
   incr seq_id   // 增加1，并返回递增后的数值(integer) 2
6、基于雪花算法（Snowflake）模式 . twitter公司开源 .OK
   缺点：依赖机器时间，如果发生回拨会导致可能生成id重复。 下面重点讨论时间回拨问题

ajax jsonp 解决get请求的跨域

div{width:100%;height:100%;position:fixed;} 占满全屏幕
$("div").fadeOut();
document.onreadystatechange =function(){
	//页面加载完成：document.readyState == complete  
	console.log(document.readyState);
}

@NoArgsConstructor: 自动生成无参数构造函数。
@AllArgsConstructor: 自动生成全参数构造函数

spring data jpa extends JpaRepository

"20121231023350".replace(
    /^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})$/,
    "$1/$2/$3 $4:$5:$6");  // "2012/12/31 02:33:50"

big data solution architect
小表join大表效率更高

系统CPU突然飙升且GC频繁，如何排查？
	top命令:显示系统中各个进程的资源占用状况
	jstack -l pid


Nginx负载均衡是通过upstream模块来实现的，内置实现了三种负载策略：
	轮循（默认）
		Nginx根据请求次数，将每个请求均匀分配到每台服务器
	最少连接
		将请求分配给连接数最少的服务器。Nginx会统计哪些服务器的连接数最少。
	IP Hash
		绑定处理请求的服务器。第一次请求时，根据该客户端的IP算出一个HASH值，
		将请求分配到集群中的某一台服务器上。
		后面该客户端的所有请求，都将通过HASH算法，找到之前处理这台客户端请求的服务器，然后将请求交给它来处理。
	upstream tomcats {
		server 192.168.0.100:8080 weight=2 max_fails=3 fail_timeout=15;
		server 192.168.0.101:8080 weight=3;
		server 192.168.0.102:8080 backup;
	}

"//div[@class='course-item']"
scrapy crawl 
java 16(无锡) 37（苏州） 80（南京） 92(杭州) 247  

用户发送一个请求，系统 A 收到请求后，先查本地 ehcache 缓存，如果没查到再查 redis。如果 ehcache 和 redis 都没有，再查数据库，将数据库中的结果，写入 ehcache 和 redis 中。

python:
pip install beautifulSoup4
 
redis windows下启动，配置自定义参数：
cd到redis目录,redis-server.exe redis.windows.conf

全局异常处理

除了在持久化对象时会用到对象序列化之外，当使用RMI(远程方法调用)，或在网络中传递对象时，都会用到对象序列化

android studio快捷键：选中代码块，然后 ctrl+alt+t 。
idea 打断点，右击断点，设置进入断点的条件！
idea 断点调试：set value
idea itar/iter快捷键 生成for循环
idea Ctrl+G 搜索行号

url->connection->getInputStream->	

https://laptop-1tgqk746/svn/cq

java类加载机制:类从被加载到虚拟机(JVM)内存中开始，到卸载出内存为止
内存模型

nginx启动
[root@localhost ~]# /usr/local/nginx/sbin/nginx
停止/重启
[root@localhost ~]# /usr/local/nginx/sbin/nginx -s stop(quit、reload)

onmouseover + layer.tips

Java web项目xx$1.class是匿名内部类的编译结果

前端：mootools
MooTools是一个简洁，模块化，面向对象的开源JavaScript web应用框架。
// create a new Class instance
var myRequest = new Request({
    url: 'getMyText.php',
    method: 'get',
    onRequest: function(){
        myElement.set('text', 'loading...');
    },
    onSuccess: function(responseText){
        myElement.set('text', responseText);
    },
    onFailure: function(){
        myElement.set('text', 'Sorry, your request failed :(');
    }
});
// and to send it:
myRequest.send(data);

Kubernetes(k8s):部署和管理容器的平台

@Resource By name，加载失败，会自动再按类型加载
@Autowired By type + @Qualifier 变为By name。
It is suggested to use @Resource for fields and setter injection. 
Stick with @Qualifier and @Autowired for constructor or a multi-argument method injection.

过滤器Filter ->拦截器Interceptor -> action执行 ->拦截器 ->过滤器

spring security 缺点：角色相关配置代码太多、大数据下几乎不可用、没有直接可操作的界面.

redis 防刷（key value,value存访问次数）。自定义注解+拦截器

elasticsearch 索引(数据库)、类型(表)、文档(行)
	例：建立一个Poems索引,创建一个Poem类型，
	    "Poem":{"propertis":{"title":{"type":"keyword"},"author":{"type":"keyword"}}};
		文档:{"title":"静夜思","author":"李白"}

Dubbo使用了第三方的ZooKeeper作为其底层的注册中心,实现服务的注册和发现.

SpringCloud使用Spring Cloud Netflix Eureka实现注册中心.
SpringCloud有Zuul路由网关,作为路由服务器,进行消费者的请求分发.
SpringCloud专注于解决各个微服务之间的协调与配置,服务之间的通信,熔断,负载均衡等.
Spring Cloud核心组件：Eureka（服务的注册与发现）、Feign（动态代理）、Ribbon（负载均衡）
  、Hystrix（熔断/降级）、Zuul（网络路由）
业务场景：订单服务->库存服务/仓储服务/积分服务
Eureka是微服务架构中的注册中心，专门负责服务的注册与发现
  Eureka Client：负责将这个服务的信息注册到Eureka Server中
  Eureka Server：注册中心，里面有一个注册表，保存了各个服务所在的机器和端口号
Feign Client会在底层根据你的注解，跟你指定的服务建立连接、构造请求、发起请求、获取响应、解析响应  
*首先Ribbon会从 Eureka Client里获取到对应的服务注册表，
 也就知道了所有的服务都部署在了哪些机器上，在监听哪些端口号。
 然后Ribbon就可以使用默认的Round Robin算法，从中选择一台机器
 Feign就会针对这台机器，构造并发起请求

O(1)指的是常数时间运行，比如操作对象为一个链表，对其有一个算法，O(1)时间指的是，无论链表大或者小，所耗费的时间都是一样的
O(n)指的是某算法的运行时间与输入规模成正比，即，若输入规模为T,花费时间为N,则输入规模2T时花费时间为2N

kafka 消费者groupId,代表一个消费者
kafka 旧数据删除策略：基于时间/基于大小。删除过期的文件并不会提高kafka的性能！

分布式数据库如何设计？

设置Linux服务器时间：date -s "2007-08-03 14:15:00"
var json = {'a':'aa','b':'bb'};
json['a']='AAAA';
console.log(json);

基于zookeeper临时有序节点可以实现的分布式锁

redis实现分布式锁:Redis是单线程的,
  1.多台服务器执行 setnx key value (返回1，说明该进程获得锁)成功执行todo，执行完todo,删除key.
  1).设置key的有效期 "expire key timeout" ,超过这个时间锁会自动释放，避免死锁.
  2).第二种方式，设置value为当前时间+1秒,其他服务器get value时，判断value值，
    过大了就直接删除key.重新设置key value

喜马拉雅问了redis的数据存储结构:
键的类型只能为字符串，值支持五种数据类型：字符串、列表、集合、散列表、有序集合(String、Hash(即Map) 、List 、 Set 、 Ordered Set)
rehash；
bilibili问了redis的事务与集群。
Redis 通过 MULTI 、 DISCARD 、 EXEC 和 WATCH 四个命令来实现事务功能
MULTI->(将多个命令打包， 然后一次性、按顺序地执行)->EXEC
事务提供了一种将多个命令打包，然后一次性、有序地执行的机制。
事务在执行过程中不会被中断，所有事务命令执行完之后，事务才能结束。
多个命令会被入队到事务队列中，然后按先进先出（FIFO）的顺序执行。
WATCH:监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。
只有在客户端的 REDIS_DIRTY_CAS 选项未被打开时，才能执行事务，否则事务直接返回失败。
DISCARD can be used in order to abort a transaction

Redis Lpush 命令将一个或多个值插入到列表头部。
Redis Sadd 命令将一个或多个成员元素加入到集合中，已经存在于集合的成员元素将被忽略。
Redis Zrem 命令用于移除有序集中的一个或多个成员，不存在的成员将被忽略。
关于JAVA的，阿里的蚂蚁金服问了如下一些问题：
java.lang.Object有哪些常用的方法,
改写一个类的toString方法需要注意哪些问题，
hashCode方法如使用，
==与equals的区别，
线程创建的几种方法，各自的使用场景，
hashmap、hashtable的数据结构实现，
java线程同步有哪些方法、各自的优缺点，jvm的结构，java代码优化

Groovy是一种基于Java平台的面向对象语言
new JSONObject(map)

session 需要入库，token不需要入库。服务端通过 算法(如HMAC-SHA256)+密钥 生成token给客户端，
	客户端保存起来（如cookie中），每次请求将token发给服务端验证，
	服务端再用同样的算法和密钥 对token进行解码 验证。

git克隆项目，创建分支，提交和同步修改，到合并分支请求的整套流程

SimpleDateFormat线程不安全,可以使用ThreadLocal<SimpleDateFormat>，或者common-lang包：FastDateFormat.getInstance().format(new Date());


	
mybatis-plus自动生成代码
chrome去掉滚动条：
body::-webkit-scrollbar {
    display: none;
}

cd D:\Program Files\Nox\bin
.\Nox_adb.exe connect 127.0.0.1:62001



android Emulator模拟器
秒s /毫秒ms /微秒μs /皮秒picosecond
https cookies web application secure
Spring MVC – Catch the exceptions thrown by view page
redirect：重定向原理

CAP定理，BASE理论   RabbitMQ消息确认机制

spring的TransactionCallback接口来实现事务

freemarker/thymeleaf 从Contoller->页面

一旦分布式了之后，通信、缓存、消息、事务、锁、配置、日志、监控、会话 ？

reddit
openresty防刷/限流

maven setting.xml可以改为 阿里云镜像，加快下载速度
spring项目启动时，可以指定生产环境：java -jar -Dspring.profiles.active=prod xx.jar
id is not present 表示必传的参数id 没有传

Oracle中的事务??
mysql InnoDB 支持事务，MyISAM 不支持事务
@RequestParam @RequestBody @PathVariable 等参数绑定注解详解

JSON.parse("text..."):convert text into a JavaScript object
JSON.stringify(obj):convert obj into a string.

INSERT INTO user(username,real_name,email,password,permission,is_deletable,is_updatable) 
VALUES("system","系统","system@local.host",sha2("123456",256),3,1,1);

(map.code)!"red"  这种方式，能够处理map或者code为miss value的情况；

<#assign str = "abcdefghijklmn"/>
${str?substring(0,4)} // 输出abcd

${emp.date?string('yyyy-MM-dd')} //日期格式

WebService，顾名思义就是基于Web的服务。它使用Web(HTTP)方式，接收和响应外部系统的某种请求。从而实现远程调用.
1:从WebService的工作模式上理解的话，它跟普通的Web程序（比如ASP、JSP等）并没有本质的区别，都是基于HTTP传输协议的程序。 
2:WebService所使用的数据均是基于XML格式的。目前标准的WebService在数据格式上主要采用SOAP协议。
  SOAP协议实际上就是一种基于XML编码规范的文本协议。


maven pom: compile/test/runntime/provided/system
默认就是compile
<scope>provided</scope> 只是编译中使用，但不会打到war中
system:依赖项不会从maven仓库抓，而是从本地文件系统拿(需要配合systemPath属性使用)

/dev/null is a black hole where any data sent, will be discarded
>/dev/null 2>&1 is redirect the output of your program to /dev/null. Include both the Standard Error and Standard Out

clean package -pl qbzhpt-yjzh -am
pl,--projects <arg>  手动选择需要构建的项目,项目间以逗号分隔;A project can be specified by [groupId]:artifactId or by its relative path.
-am,--also-make      构建指定模块,同时构建指定模块依赖的其他模块;

HandlerInterceptorAdapter 拦截器：preHandle()等，true继续往下走，false返回
WebMvcConfigurerAdapter详解
@Primary：自动装配时当出现多个Bean候选者时，被注解为@Primary的Bean将作为首选者，否则将抛出异常
Netflix Zuul:Zuul基于Eureka的服务发现功能动态 实现路由的功能
@Qualifier(“office”)中的office是Bean的名称，所以@Autowired和@Qualifier结合使用时，自动注入的策略就从byType转变成byName了。
@Qualifier 只能和@Autowired 结合使用，是对@Autowired有益的补充。

jenkins、SONAR

SQL Injection Based on 1=1 is Always True
SELECT * FROM Users WHERE Name ="" or ""="" AND Pass ="" or ""=""

idea打开maven多模块项目，直接引入父模块的pom.xml文件即可
.tld文件后缀：TLD（taglib description）是JSP的标签库描述文件
.ftl文件后缀：Freemarker模板的文件后缀名

app接口 一直跳转到登陆页，注意拦截器

缓存框架（Redis、MemoryCache等）
微服务（dubbo、Spring Cloud等）
全文检索（Solr、ElasticSearch等）
分布式发布/订阅消息队列系统（ActiveMQ、Kafka等）

Lombok是一个通过注解以达到减少代码的Java库,如通过注解的方式减少get,set方法,构造方法等。
MyBatis-Plus（简称 MP）是一个 MyBatis 的增强工具，在 MyBatis 的基础上只做增强不做改变，为简化开发、提高效率而生。	
项目基于 Spring Boot 2.1.0 、 Jpa、 Spring Security、redis、Vue的前后端分离的后台管理系统，项目采用分模块开发方式， 权限控制采用 RBAC，支持数据字典与数据权限管理，支持一键生成前后端代码，支持动态路由
https://auauz.net/dashboard
后台管理系统：菜单显示 架构调整
You are literally the best coder I know.

@media screen and (min-width: 1201px) and (max-width: 1500px) { 
	.abc {width: 1200px} 
} 
@media screen and (min-width: 901px) and (max-width: 1200px) { 
	.abc {width: 900px} 
} 

代码放coding

npm太慢， 淘宝npm镜像使用方法:npm config set registry https://registry.npm.taobao.org
vscode终端： npm start
BEM 命名规范

['a','b'].slice(1,2);
"".slice(start,end);
The slice() method returns a new array from begin to end (end not included).

删除数组对象中的某个元素
Array.splice(start,deleteCount)
const index = array.indexOf(5);
if (index > -1) {
  array.splice(index, 1); // 2nd parameter means remove one item only
}

jdbc.url=jdbc:mysql://10.39.149.200:33006/epg_app?useUnicode=true&characterEncoding=UTF-8
jdbc.username=root
jdbc.password=iwhaleCloud@2018

vscode js文件按f5进入调试模式
tomcat->webapps->manager 
进行 Server Status 和 Applications 管理，对服务器和其他应用进行启动、重启、关闭等操作，对 Session、JVM 性能参数等进行监听并管理
kill -9 `ps -ef | grep $1 | grep java | awk '{print $2}'`
sshpass -p "YOUR_PASSWORD" ssh -o StrictHostKeyChecking=no YOUR_USERNAME@SOME_SITE.COM:2400
#rpm -ivh example.rpm 安装 example.rpm 包并在安装过程中显示正在安装的文件信息及安装进度
File-> Settings
In Popup menu: Project-> Project Interpreter-> add or create virtualenv environment(search mysql etc.)
Ctrl+Alt+L idea格式化代码
disputer 框架
tomcat/conf文件夹下tomcat-users.xml:<user username="tomcat" password="tomcat" roles="manager-script"/>
tomcat/webapps的manager接口
http://localhost:8080/manager/text/start?path=/tt

Velocity、Freemaker 等模板引擎
linux: jps( Java Virtual Machine Process Status Tool ) 、pkill -f
sudo apt-get install build-essential
$(this).addClass('active').siblings().removeClass('active');
npm chengqun/Ww88459526
Eclipse需要安装egit插件(github) https 
hbase kafka solr hive 应用场景
Math.random() :
	returns a random number between 0 and 1
	inclusive of 0, but not 1
sts
ctrl+o
springcloud 
GC multi-thread Runnable Callable
单例模式 Singleton pattern
thread join 应用场景：主线程等待子线程完成（例 耗时操作放到子线程进行）
join底层是wait方法，所以它是会释放对象锁的，
而sleep在同步的方法中是不释放对象锁的，只有同步方法执行完毕，其他线程才可以执行。

面向切面写入数据库(Aspectj)
kotlin

JSX: Javascript xml
设计模式之单例模式-饿汉式&懒汉式

1、线程 状态？ 运行、阻塞、结束 (New->Runnable->Terminated)
 New、Runnable、Blocked、Waiting、Timed Waiting、Terminated
2、JVM optimize
3、Mysql 联合索引 ABC字段，D如何 可以命中：
最左原则
联合索引又叫复合索引。对于复合索引:Mysql从左到右的使用索引中的字段，
一个查询可以只使用索引中的一部4份，但只能是最左侧部分。
例如索引是key index (a,b,c). 可以支持a | a,b| a,b,c 3种组合进行查找，但不支持 b,c进行查找。
 索引不会包含有NULL值的列
只要列中包含有NULL值都将不会被包含在索引中，复合索引中只要有一列含有NULL值，那么这一列对于此复合索引就是无效的。
所以我们在数据库设计时不要让字段的默认值为NULL。
4、redis性能如何提高(improve redis performance)
1).使用Batch操作 
2).使用PipeLine管道 
5、java设计模式 业务场景
6、连接池 配置
<!-- 基本属性 url、user、password -->
<property name="url" value="${jdbc.url}" />
<property name="username" value="${jdbc.username}" />
<property name="password" value="${jdbc.password}" />
<!-- 配置初始化大小、最小、最大 -->
<property name="initialSize" value="1" />
<property name="minIdle" value="1" />
<property name="maxActive" value="20" />
<!-- 配置获取连接等待超时的时间 -->
<property name="maxWait" value="60000" />
<!-- 配置间隔多久才进行一次检测，检测需要关闭的空闲连接，单位是毫秒 -->
<property name="timeBetweenEvictionRunsMillis" value="60000" />
<!-- 配置一个连接在池中最小生存的时间，单位是毫秒 -->
<property name="minEvictableIdleTimeMillis" value="300000" />
<!-- 打开PSCache，并且指定每个连接上PSCache的大小 -->
<property name="poolPreparedStatements" value="true" />
<property name="maxPoolPreparedStatementPerConnectionSize" value="20" />
<!-- 配置监控统计拦截的filters，去掉后监控界面sql无法统计 -->
<property name="filters" value="stat" />

Q:Java garbage collector - When does it collect?
A common strategy in generational garbage collectors is to run the collector 
when an allocation of generation-0 memory fails!

Q:GC(garbage collection)优点：
消除手动 内存分配/释放 的负担

Q:GC缺点：
When the garbage collector thread is running, other threads are stopped
, meaning the application is stopped momentarily.

Q:What are stack(栈) and heap(堆)?
The stack is a part of memory.
The heap is a large bulk of memory intended for allocation of objects.
When you create an object with the new keyword, 
it gets allocated on the heap. However, 
the reference to this object lives on the stack. 

Q:generational garbage collection?
garbage根据age分类

Q：how the GC collects an eligible object?
1).if all its references are null. 
2).Cyclic dependencies without any live external reference are also eligible for GC
3).a parent object is set to null,children will eligible for GC

Q: How do you trigger garbage collection from Java code?
System.gc() and Runtime.gc()等方法并不能保证执行 垃圾收集.
it will only trigger if JVM thinks it needs a garbage collection based on Java heap size.

Q: String +号 拼接字符串的缺陷：
When concatenating two String instances, a new object is created, 
and strings are copied. This could bring a huge garbage collector overhead 
if we need to create or modify a string in a loop.
StringBuffer is different from StringBuilder in that it is thread-safe.
If you need to manipulate a string in a single thread, use StringBuilder instead.

Q:How can we make sure main() is the last thread to finish in Java Program?
We can use Thread join() method to make sure all the threads created 
by the program is dead before finishing the main function. 

Q:What is volatile keyword?
When we use volatile keyword with a variable, 
all the threads read it’s value directly from the memory and don’t cache it. 
This makes sure that the value read is the same as in the memory.

Q:What is ThreadLocal?
Java ThreadLocal用于创建线程局部变量。
Every thread has it’s own ThreadLocal variable and they
can use it’s get() and set() methods to get the default value 
or change it’s value local to Thread.

Q:How can we achieve thread safety in Java?
1).Synchronization is the easiest and most widely used tool for thread safety in java.
2).Use of Atomic Wrapper classes from java.util.concurrent.atomic package. 
	For example AtomicInteger
3).Use of locks from java.util.concurrent.locks package.
4).Using thread safe collection classes, check this post for usage of ConcurrentHashMap for thread safety.
5).Using volatile keyword with variables to make every thread read the data from memory, not read from thread cache.

Q:What are differences between wait and sleep method in Java?
The only major difference is to wait to release the lock or monitor, 
while sleep doesn't release any lock or monitor while waiting.

Q:How to take a thread dump(线程转储，然后分析线程阻塞)?
Linux you can do this by command "kill -3"
windows use "CTRL+Break." 

Q：Why do we call start() method which in turns calls run() method, 
	why not we directly call run() method?
When you call the start() method, it creates a new thread 
and executes code declared in the run()  while directly calling the run() method. 
This doesn't create any new threads and executes code on the same calling thread

Q:JVM optimize? 
1).Use StringBuilder to concatenate Strings 
2).Use + to concatenate Strings in one statement
3).Use primitives where possible.(it’s better to use an int instead of an Integer...)
	That allows your JVM to store the value in the stack instead of the heap
4).Try to avoid BigInteger and BigDecimal
5).Check the current log level first
	// don’t do this
	log.debug(“User [” + userName + “] called method X with [” + i + “]”);
	// do this
	if (log.isDebugEnabled()) {
		log.debug(“User [” + userName + “] called method X with [” + i + “]”);
	}
6).Cache expensive resources, like database connections

Mysql：	
InnoDB 和 Myisam 都是用 B+Tree 来存储数据的。


Q:内置锁(synchronized)、显示锁(ReentrantLock) 区别?
内置锁能够解决大部分需要同步的场景，只有在需要额外灵活性是才需要考虑显式锁，
	比如可定时RenentrantLock.tryLock(long timeout, TimeUnit unit)、
	可中断RenentrantLock.lockInterruptibly()、多等待队列RenentrantLock.newCondition() 等特性。
显式锁虽然灵活，但是需要显式的申请和释放，并且释放一定要放到finally块中，否则可能会因为异常导致锁永远无法释放！这是显式锁最明显的缺点。
综上，当需要同步时请优先考虑更安全的更易用的隐式锁。

========================================================================
hashmap结构；什么对象能作为key
hashmap,concurrentHashMap,hashtable比较
String,StringBuilder,StringBuffer
对象的深浅复制
多线程：
wait,sleep分别是谁的方法，区别
countLatch的await方法是否安全，怎么改造
线程池参数，整个流程描述
背后的底层原理aqs，cas
ThreadLocal原理，注意事项，参数传递
Java的锁，内置锁，显示锁，各种容器
锁优化：锁消除，锁粗化，锁偏向，轻量级锁
web方面：
servlet是否线程安全，如何改造
session与cookie的区别，get和post区别，tcp3次握手，文件上传用post还是get
session的存储
如何防止表单重复提交
jvm:
jvm内存模型，jvm问题工具,jps,jinfo,jmap...
数据库：
最重要的索性及底层实现
索性失效的场景
最左原则
查看执行计划
carndiation
锁的类型，行级表级悲观乐观锁
解释数据库事务及特性
隔离级别及实现：
	MySQL 的事务隔离级别一共有四个，分别是读未提交、读已提交、可重复读以及可串行化。
	MySQL 的隔离级别的作用就是让事务之间互相隔离，互不影响，这样可以保证事务的一致性。
	MySQL 默认的隔离级别也是可重复读。

redo log .undo logbin log主从复制
mvcc,Next-Key Lock
分布式：
问了CAP，跟base
zookeeper满足了CAP的哪些特性，paxos
缓存穿透怎么解决
redis的io模型
如果保证redis高可用
redis是单线程还是多线程
线上cpu占比过高怎么排查
一致性hash
分库分表
spring:
ioc,aop原理
ioc初始化流程
springmvc的流程
springboot,spring cloud相关组件
做过的项目，梳理清理，画图
mysql: explain和profile
========================================================================

什么时候要使用索引？
​ 主键自动建立唯一索引；

​ 经常作为查询条件在WHERE或者ORDER BY 语句中出现的列要建立索引；

​ 作为排序的列要建立索引；(单纯的order by 不会用到索引，但如果在where中出现，就可以用索引了。)

​ 查询中与其他表关联的字段，外键关系建立索引

​ 高并发条件下倾向组合索引；

​ 用于聚合函数的列可以建立索引，例如使用了max(column_1)或者count(column_1)时的column_1就需要建立索引

什么时候不要使用索引？

​ 经常增删改的列不要建立索引；

​ 有大量重复的列不建立索引；

​ 表记录太少不要建立索引。只有当 数据库里已经有了足够多的测试数据时，它的性能测试结果才有实际参考价值。如果在测试数据库里只有几百条数据记录，它们往往在执行完第一条查询命令之后就被全部加载到内存里，这将使后续的查询命令都执行得非常快--不管有没有使用索引。只有当数据库里的记录超过了1000条、数据总量也超过了MySQL服务器上的内存总量时，数据库的性能测试结果才有意义。

SQL优化的一些部分：
如何避免全表扫描？

1、where字句别用or链接，可以union all.2、in和not in也慎用，可以between and. 3.避免对字段进行null值判断。4,where字句别用!=和<>操作符5、别用以通配符开头的like的查询。6、别在where子句对字段进行表达式操作和函数操作。 7任何地方都不要使用 select * from t。8、尽量使用数字型字段。9、复合索引尽量满足最左前缀原则。10,在查找唯一一条数据的时候，使用limit 1.10、类型不一致会导致失效，例如字符串不加单引号会导致索引失效。

​ 索引优化：

​ 1、根据最左前缀原则，我们一般把排序分组频率最高的列放在最左边

​ 2、模糊查询以%为开始的查询，只能使用全文索引来进行优化。

​ 3、使用短索引。对串列进行索引，如果可能应该指定一个前缀长度。

in与exists的区别。使用上，in 后面的查询返回结果只能有一个字段。而exists没有限制。

本质上： A exists B;exists相当于遍历外面A,看A中数据是否存在于B。而in,相当于将结果集B分解开，用or相连，相当于做多次的查询。

exists相当于查询筛选，in则是多次查询;

1、如果查询的两个表大小相当，那么用in和exists差别不大。

2、如果两个表中一个表大，另一个是表小，那么IN适合于外表大而子查询表小的情况。

3、如果两个表中一个表大，另一个是表小，EXISTS适合于外表小而子查询表大的情况。

in不会使用索引搜索，会全表扫描。

数据量过大：

1、查询时限定数据范围。2、读写分离，主写从读。3、垂直分区4、水平分区.
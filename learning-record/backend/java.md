### 1. Mapped Statements collection does not contain value for后面是什么类什么方法之类的：
   错误原因有几种：
   1)、mapper.xml中没有加入namespace
   2)、mapper.xml中的方法和接口mapper的方法不对应
   3)、mapper.xml没有加入到mybatis-config.xml中(即总的配置文件)，例外：配置了mapper文件的包路径的除外
   4)、mapper.xml文件名和所写的mapper名称不相同。
   org.apache.ibatis.binding.BindingException: Invalid bound statement (not found)
   查看读取mapper.xml配置，例如是否是读取的 /*Mapper.xml,然后新写的xml名字是否包含后缀xxMapper.xml
### 2. Linux安装jdk
	1).下载jdk-8u65-linux-x64.tar.gz版;
	2).将文件jdk-8u65-linux-x64.gz移动到/usr/java/下，并解压：
	tar -xzvf  jdk-8u65-linux-x64.gz
	3).在/etc/profile文件中，配置环境变量，是JDK在所有用户中生效：打开/etc/profile文件　　vi /etc/profile
	4).编辑profile文件，在最后添加：
	export JAVA_HOME=/usr/java/jdk1.8.0_65
	export JRE_HOME=$JAVA_HOME/jre
	export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
	export PATH=$JAVA_HOME/bin:$PATH
	保存退出后，执行source /etc/profile使修改的环境变量生效
	5).使用java -version命令测试是否成功     
### Mybatis - Invalid bound statement (not found)
Check if scanned the config of mapperLocations 

### Maven打包时将外部引入的jar包 打包到项目jar包中
`<includeSystemScope>true</includeSystemScope>`

### Java connect Linux to get server info: ganymed-ssh2-262.jar
<dependency>
  <groupId>ch.ethz.ganymed</groupId>
  <artifactId>ganymed-ssh2</artifactId>
  <version>262</version>
</dependency>
	Connection connection = new Connection(hostname);
	connection.connect();
	boolean isAuthenticated = connection.authenticateWithPassword(username, password);
	if (!isAuthenticated) {
		throw new IOException("Authentication failed.");
	}
	Session session = connection.openSession();
	session.execCommand(command);
	BufferedReader reader = new BufferedReader(new InputStreamReader(session.getStdout()));
	String line;
	while ((line = reader.readLine()) != null) {
		System.out.println(line);
	}
	session.close();
	connection.close();

### start a jar
`nohup java -jar starfish.jar > nohup.out 2>&1  -Duser.timezone=Asia/Shanghai &`

### convert timestamp to date
`// 1727666666286`
`long timestamp = System.currentTimeMillis();`
`// Mon Sep 30 03:16:40 GMT+08:00 2024`
`Date date = new Date(timestamp);`


### mybatis collection属性值就是传入的List或array对象在自己封装的map里面的key 
<foreach item="id" collection="ids" open="and id in (" separator="," close=")">
    #{id}
</foreach>
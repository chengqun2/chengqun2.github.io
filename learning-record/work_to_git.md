1. http://stackoverflow.com/
2. 将json数据传到页面  PrintWriter out= response.getWriter();
   out.print(JSONUtil.toJSONString(jsonMap));

4.分页功能 service 层代码：
   public List<UinTestBean> getByPatamter(UinTestBean bean) {
   int pageOffset = ((bean.getPage() - 1) * bean.getRows());
   bean.getPager().setPageOffset(pageOffset);
   return mapper.getByPatamter(bean);
   }
   mybatis.xml层代码：limit #{pager.pageOffset},#{rows}
5.spring mvc 文件上传 jar包：commons-io-2.2 ；
   (@RequestParam("file1") MultipartFile file1)
   FileUtils.copyInputStreamToFile(file1.getInputStream(),
   new File("D:\\test\\images\\", System.currentTimeMillis()
   + file1.getOriginalFilename()));
6.request.getRequestDispatcher("xxx_success.jsp").forward(request, response);
   response.sendRedirect("xxx_failure.jsp");
7.java.lang.IllegalArgumentException: Mapped Statements collection does not contain value for com.uin.mapper.PricingPlanMapper.selectByPlanName  (没有在 mybatis-config.xml 中配置)
8.eclipse安装svn插件地址：Subclipse 1.8.x - http://subclipse.tigris.org/update_1.8.x
9.jar not loaded  (检查下项目 构建路径，查看是否有jar包需要去除)
10.easyui确认框：var isSure = confirm("Are you sure?");
11.easyui数组拼接：var row = $('#data-list').datagrid('getChecked');
   var spIds = [];
   for (var i = 0; i < row.length; i++) {
   spIds.push(row[i].spId); //注意修改你的id列
   }

12.jsp页面引入jstl标签：17:26 2015/9/23
1).下载jstl.jar包和standard.jar包放到项目的lib文件夹下
2).然后在你的jsp页面里引入如下代码：
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
13.eclipse安装svn插件地址：http://subclipse.tigris.org/update_1.8.x
14安卓国内镜像地址：mirrors.neusoft.edu.cn
15.http://localhost:8080/uinmeeting/mobile/mobileRequest.shtml?method=searchGroup&params={}
16.$('#grid').datagrid('load', {
username:$('#username').val(),
end: $('#end').datetimebox('getValue')
});

17.tomcat server图片上传并显示：
<Context docBase="/data/ddm" path="/ddm/uin_pic"  reloadable="true" debug="0" />
<Context docBase="ddm_web" path="/" reloadable="false" source="org.eclipse.jst.jee.server:ddm_web"/>
docBase 是图片实际存放地址
path 是项目路径 读取时 src 用的 地址
http://localhost:8080/ufu/uin_picserver/xx.jpg
1).设置文件上传目录，目录可以为服务器任意位置；
2).在tomcat 的server下 配置 图片相对路径 及 服务器图片实际存放路径；
3).图片读取时，读取 图片相对路径 即可
18.Properties properties = new Properties();
InputStream inputStream = this.getClass().getResourceAsStream(
"/conf/upload.properties");
19.     static ApplicationContext context = new ClassPathXmlApplicationContext(
	        new String[]{"spring-*.xml"}); 
	SiteMainService<SiteMain> siteMainService = (SiteMainService)context.getBean("siteMainService");
	//    UserMainService<UserMain> userMainService = (UserMainService)context.getBean("userMainService");
20.     // InputStream : 此抽象类是表示字节输入流的所有类的超类。
	    InputStream inputStream = entity.getContent();
	    // InputStreamReader 是字节流通向字符流的桥梁
	    // OutputStreamWriter 是字符流通向字节流的桥梁
	InputStreamReader inputStreamReader = new InputStreamReader(
	inputStream, "UTF-8");
	// 从字符输入流中读取文本，缓冲各个字符，从而实现字符、数组和行的高效读取。
	BufferedReader reader = new BufferedReader(inputStreamReader);// 读字符串用的。
	21.百度 “ip”为本机所在网络的外网IP地址，映射在路由器中进行配置
	22.div绝对布局，始终显示在页面右下角：
   <div id="baoxiu-div" style="background-color: white; display: block; width: 200px; height: 150px; border: 1px solid #ccc; 
        right: 3%; bottom: 4%; z-index: 9006; position: absolute;">
   </div>
23.easyui设置input隐藏、显示、添加属性、去除属性
$('#editForm').form({
    onLoadSuccess:function(data){
        if (data.id && data.id>0 ) {
            $("input[name='name']").attr("readOnly","true");
            $("input[name='pwd']").validatebox({"required":false});
            $("input[name='pwdRepeat']").validatebox({"required":false});
            $("#pwd").hide();
            $("#pwdRepeat").hide();
        }
    }
});
$('#edit-win').dialog({
    onClose:function(){
        $('#pwdMsg').html("");
        $("input[name='name']").removeAttr("readOnly");
        $("input[name='pwd']").attr("required","true");
        $("input[name='pwdRepeat']").attr("required","true");
        $("#pwd").show();
        $("#pwdRepeat").show();
    }
});
24.linux 常用命令： 删除abc文件夹 rm -rf abc
25. mybatis 设置可读取自动递增的主键:
 useGeneratedKeys="true" keyProperty="id"
26.文件（附件）拷贝：void org.apache.commons.io.FileUtils.copyInputStreamToFile(InputStream source, File destination) 
27.JQuery: div中追加div   $("#chargeNames").append("<div style='margin-left:130px;'><span> "+ data[x].name +"</span></div>");
28.表增加一个记录创建时间的字段（记录生成时的系统时间）
  alter table test
   add COLUMN create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '记录生成时间'
29.linux vi 
	1).进入vi后，在Command mode下按‘i’、‘a’或‘o’三键就可进入Insert mode
	2).改完后按esc退出编辑模式
	3).保存并退出(:wq) 

30.mybatis map传递数组参数：
<delete id="deleteByIdList" parameterType="java.util.Map" >
delete from uin_company_with_type
where id in
<foreach collection="list" item="id" open="("
separator="," close=")">#{id}
</foreach>
</delete>

31.DATE_FORMAT(create_time,'%Y-%m-%d %H:%i') create_time
32.ajax json success  @ResponseBody
ajax简单示例：
$.get(url,function(data){
alert(data);
});
33. 启动禅道：/opt/zbox/zbox start
	34.linux下载网页命令：wget -r -p -np -k -P ~/qunar/ http://www.qunar.com/
	35.mysql:FIND_IN_SET
	36.svnadmin create 文件夹
	37.字段主键值 区分大小写：alter table crm_customer modify column id varchar(10) BINARY;
	38.Cannot find ./catalina.sh
	The file is absent or does not have execute permission
	This file is needed to run this program
	没有给bin目录下的文件授权可执行权限：
	chmod +x *.sh
	或   chmod 777 *
	39.触发器demo:
	CREATE TRIGGER t_after_insert_on_uin_user
	AFTER
	insert on test.tt
	FOR EACH ROW
	BEGIN
	insert into  ecp.test_user(user_name,pwd) values(new.user_name,new.pwd);
	END;
	  
	41.eclipse中tomcat加载不到项目（启动加载）：项目中搜索：wb-resource ，修改 source-path"
	43.mysql安装，中文编码选最下面那个自定义(utf8)
	44.linux查看磁盘占用情况：df -h ;
	du -sh * （查看当前目录下 每个文件夹的大小）
	45.linux:mysql --version
	46.linux安装mysql：apt-get install mysql-client-core-5.5   
	apt-get install mysql-server
	47.linux连接mysql数据库：mysql -h 111.4.115.227 -u root -p
	48.ubuntu server下安装了MySQL 5.5数据库，然后在windows下通过Navicat for MySQL连接时，
	出现 Can't connect to mysql server on xxx.xxx.xxx.xxx(10038) 的问题。
	解决方案如下：
	1、授权
	mysql>grant all privileges on *.*  to  'root'@'%'  identified by 'youpassword'  with grant option;
	mysql>flush privileges;
	2、修改/etc/mysql/my.conf
	找到bind-address = 127.0.0.1这一行
	改为bind-address = 0.0.0.0即可				   
	49.linux安装apache: sudo apt-get install apache2
	50.linux配置php环境：http://www.cnblogs.com/lufangtao/archive/2012/12/30/2839679.html php配置第4行，文件夹路径应为：apache2
	php安装You don't have permission to access /index.html on this server.
	解决办法：<Directory />中  deny from all 改为 "allow" from all
	51.The type java.io.ObjectInputStream cannot be resolved. It is indirectly referenced from required .class files
	解决办法：jdk版本保持一致，（同52），找到JRE选项卡。
	52.maven项目断点调试：
	1)、找到Eclipse中Debug Configuration，找到Maven Build选项。
	2)、选择Maven Build下某项目，然后点击Source选项卡，然后Add你要调试的Source
	53.eclipse转web项目，右击选中项目Properties -> Project Facets 转web项目
	54.eclipse window -> perferences -> server:runtime 配置tomcat+jdk版本
	55.Oracle创建用户，并授权：
	create user yz0401 identified by yz0401;
	grant resource,connect to yz0401;
	56.php站点配置：apache->httpd.conf->修改 DocumentRoot 和 <Directory
	57.php多站点配置：apache->httpd.conf->
	1).Include conf/extra/httpd-vhosts.conf去掉注释
	2).wamp安装路径中conf/extra/httpd-vhosts.conf 添加相应路径等
	58.maven项目 下载之后，缺少jar包，run as -> maven-install即可
	59.eclipse红色感叹号 原因 ：1).jar包缺失。2). 关联项目缺失
	60.Caused by: java.sql.SQLException: Table './ddm/uin_schedule_user_log' is marked as crashed and should be repaired
	1)mysql数据存放：/var/lib/mysql/ddm
	2)myisamchk -r 表名
	61.ipconfig -all  查询DNS
	
64.	url自动跳转	 
	   <script language='javascript'>
	   document.location = 'http://www.uin.com';
	   </script>
	   65./**
	   * 递归获取文件夹下 所有的子文件（包括子文件夹下的文件）
	   *
	   * @param childrenArrayList
	   * @param floderId
	   * @return
	   */
	   public List<UinCloudStorage> getChildrenList(
	   List<UinCloudStorage> childrenArrayList, Integer floderId) {
	   List<UinCloudStorage> childrenList = uinCloudStorageMapper
	   .getChildrenListByParentId(floderId);
	   childrenArrayList.addAll(childrenList);
	   for (UinCloudStorage uinCloudStorage : childrenList) {
	   getChildrenList(childrenArrayList, uinCloudStorage.getId());
	   }
	   return childrenArrayList;
	   }
66. 创建视图(及case使用，删除视图/表 drop view/table等)
	CREATE VIEW v_test AS
	SELECT
	id,
	nickname,
	CASE `status`
	WHEN '1' THEN '男'
	WHEN '2' THEN '女'
	ELSE '其他' END `status`
	FROM
	users
	
	68./**
	* 将数据从数据库中取出后，再根据创建时间（天）分组
	*
	* @param arrangeList
	* @return
	  */
	  public Map<String, List<UinArrange>> groupArrangeDataByCreateTime(
	  List<UinArrange> arrangeList) {
	  Map<String, List<UinArrange>> map = new HashMap<String, List<UinArrange>>();
	  for (UinArrange arrange : arrangeList) {
	  if (map.containsKey(arrange.getCreateTime())) {// map中异常批次已存在，将该数据存放到同一个key（key存放的是异常批次）的map中
	  map.get(arrange.getCreateTime()).add(arrange);
	  } else {// map中不存在，新建key，用来存放数据
	  List<UinArrange> tmpList = new ArrayList<UinArrange>();
	  tmpList.add(arrange);
	  map.put(arrange.getCreateTime(), tmpList);
	  }
	  }
	  return map;
	  }

	/**
	* 取出分组数据
	*
	*/
	List<ArrangeDayViewEntity> arrangeDayViewList = new ArrayList<ArrangeDayViewEntity>();
	Map<String, List<UinArrange>> map2 = scheduleService
	.groupArrangeDataByCreateTime(list);
	for (Map.Entry<String, List<UinArrange>> entry : map2
	.entrySet()) {
	ArrangeDayViewEntity entity = new ArrangeDayViewEntity();
	entity.setDay(entry.getKey());
	entity.setArrangeDayList(entry.getValue());
	arrangeDayViewList.add(entity);
	System.out.println("Key = " + entry.getKey() + ", Value = "
	+ entry.getValue());
	}
	map.put("list", arrangeDayViewList);
	69.U会是否报名sql:
	SELECT a1.id,
	CASE ISNULL(a2.JOIN_TIME)
	WHEN '1' THEN '0'
	ELSE '1' END is_join,a2.JOIN_TIME
	from uin_meetings a1
	left join
	(SELECT t1.*,t2.JOIN_TIME from uin_meetings t1
	LEFT JOIN uin_meetings_history t2
	on t1.id = t2.MEETING_ID
	where t1.USER_ID = '18662062998') a2
	on a1.id = a2.id

	   71.du -sh /a/b(查看文件夹大小)
	   top（查看cpu等）、free（查看内存等） 	
	   72.Ubuntu 安装redis：
	   sudo apt-get install redis-server
	   查看服务：ps -ef | grep -i redis （或：ps -aux|grep redis）
	   sudo /etc/init.d/redis-server status
	   进入客户端： redis-cli(或：redis-cli -p 6877 (p为端口号) )
	   退出客户端：exit
	   输入密码：auth uin!4008946001
	   修改密码：config set requirepass uin!4008946001
	   /etc/init.d/redis-server restart
	   service redis restart
	   查看所有key: keys *
	   set key1 value1、get key1
	   73.HttpServletRequest中读取HTTP请求的body(content to send)：
	   BufferedReader br = request.getReader();
	   String str, wholeStr = "";
	   while ((str = br.readLine()) != null) {
	   wholeStr += str;
	   }
	   System.out.println(wholeStr);
74. 调用第三方API：
	/**
	* 公共请求方法（http请求）
	*
	* @param headRequestAddress
	* @param requestJson
	* @return
	  */
	  public String httpciletRequest(String headRequestAddress, String requestJson) {
	  log.info("Server:" + headRequestAddress);
	  log.info("params:" + requestJson);
	  StringBuilder result = new StringBuilder();
	  HttpParams paramsw = createHttpParams();
	  DefaultHttpClient httpClient = new DefaultHttpClient(paramsw);
	  HttpPost post = new HttpPost(headRequestAddress);
	  post.addHeader("content-type", "application/json");
	  try {

	  	BasicHttpEntity requestBody = new BasicHttpEntity();
	  	requestBody.setContent(new ByteArrayInputStream((requestJson
	  			.toString()).getBytes("UTF-8")));
	  	requestBody.setContentLength(requestJson.toString().getBytes(
	  			"UTF-8").length);

	  	post.setEntity(requestBody);

	  	HttpResponse httpResponse = httpClient.execute(post);
	  	int httpCode = httpResponse.getStatusLine().getStatusCode();
	  	if (httpCode == HttpURLConnection.HTTP_OK && httpResponse != null) {
	  		httpResponse.getAllHeaders();
	  		HttpEntity entity = httpResponse.getEntity();
	  		httpResponse.getFirstHeader("content-type");
	  		// 读取服务器返回的json数据（接受json服务器数据）
	  		InputStream inputStream = entity.getContent();
	  		InputStreamReader inputStreamReader = new InputStreamReader(
	  				inputStream, "UTF-8");
	  		BufferedReader reader = new BufferedReader(inputStreamReader);// 读字符串用的。
	  		String s;
	  		while (((s = reader.readLine()) != null)) {
	  			result.append(s);
	  		}
	  		reader.close();// 关闭输入流
	  		// 在这里把result这个字符串个给JSONObject。解读里面的内容。
	  		log.info("RESULT====" + result.toString());
	  	}
	  } catch (Exception e) {
	  // TODO: handle exception
	  e.printStackTrace();
	  }

	  return result.toString();
	  }

	public HttpParams createHttpParams() {
	int timeOut = ConfigUtil.TIME_OUT;
	HttpParams params = new BasicHttpParams();
	HttpConnectionParams.setStaleCheckingEnabled(params, false);
	HttpConnectionParams.setConnectionTimeout(params, timeOut * 1000);
	HttpConnectionParams.setSoTimeout(params, timeOut * 1000);
	HttpConnectionParams.setSocketBufferSize(params, 8192 * 5);
	return params;
	}
75. 安装mysql: sudo apt-get install mysql-server		
	登录mysql: mysql -uroot -p
	使用grant all privileges on来更改用户对应某些库的远程权限（可以增加新用户）:
	grant all privileges on *.* to 'root2'@'%' identified by 'uin!321' with grant option;
	flush privileges;
	查看mysql开启远程的用户：select host,user from mysql.user;
	76.ctrl+c 退出ping、telnet等
	77.ubuntu nginx安装配置：
	1.sudo apt-get install nginx
	2.chmod a+x /etc/init.d/nginx   (a+x ==> all user can execute  所有用户可执行)
	3.修改默认端口： /etc/nginx/sites-available
	4./etc/init.d/nginx status(start/stop/restart)
	5./etc/nginx/nginx.conf 配置server等
	server_name后面 不能加"/"；(Restarting nginx: nginx: [emerg] invalid URL prefix in /etc/nginx/nginx.conf:83
	nginx: configuration file /etc/nginx/nginx.conf test failed)
	78.ubuntu防火墙：
	sudo ufw status 查看防火墙状态
	sudo ufw disable 关闭
	sudo ufw allow 80 允许外部访问80端口
79.
在 ssh ， telnet 终端中文显示乱码解决办法（ CentOS 5.3 、redhat）
#vi /etc/sysconfig/i18n
将原内容 LANG="en_US.UTF-8"
SYSFONT="latarcyrheb-sun16"
修改为
LANG="zh_CN.GB18030"
LANGUAGE="zh_CN.GB18030:zh_CN.GB2312:zh_CN"
SUPPORTED="zh_CN.UTF-8:zh_CN:zh:en_US.UTF-8:en_US:en"
SYSFONT="lat0-sun16"

用 yum 安装中文字体
#yum install fonts-chinese.noarch
断开 ssh ，重新连
在终端输入 date 命令测试
#date
2009 年 11 月 24 日 星期一 12:09:00 CST
80.linux jdk->jre->fonts下 放入字体包
81.查看svn服务
ps -ef | grep svn
svnserve -d -r /data/subversion
82.查看本机所有端口开放情况：
nmap 127.0.0.1
83.java项目tomcat端口映射 与 php项目apache映射不同(php项目映射，必须指定ip、项目路径)！
84.eclipse ctrl+t 查看子类
85.oracle创建用户、授权
create user c##cq identified by cq;
grant create session,create table,create view,create sequence,create procedure,unlimited tablespace to c##cq;
86.cmd->sqlplus 进入oracle
87.maven添加oracle ：
1).cd到jar包所在文件夹
mvn install:install-file -DgroupId=com.oracle -DartifactId=ojdbc14 -Dversion=10.2.0.4.0 -Dpackaging=jar -Dfile=ojdbc14.jar
2).
<!-- 添加oracle jdbc driver -->  
<dependency>    
    <groupId>com.oracle</groupId>    
    <artifactId>ojdbc14</artifactId>    
    <version>10.2.0.4.0</version>
</dependency>
88.存储过程断点调试
pl/sql Procedures->右击某个存储过程 Test-> Add source to editor
89.oracle存储过程示例：（存储过程中不commit，放到代码事务中提交）
create or replace procedure t1(pid in number, num11 out number)
as aa number;
begin
select num1 into aa from tab1 where id = pid;
update tab1 set num1 = num1 + 1 where id = pid;
select num1 into num11 from tab1 where id = pid;
dbms_output.put_line('前：' || aa || '后：' || num11);
end;
90.包头：
create or replace package mypackage is
type usercursor is ref cursor;
procedure queryUser(pid in number, user out usercursor);
end mypackage;
包体：
create or replace package body mypackage is
procedure queryUser(pid in number, user out usercursor) is
begin
open user for
select * from tab1 where id = pid;
end queryUser;
end mypackage;
91.包头包体调试：
pl/sql Packages->点击某个包头->右击某个存储过程或函数-> Test
92.ECharts图表:
1).echarts(bar柱状图)：需要
xAxis : [
{
type : 'category',
data : ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
}
],
yAxis : [
{
type : 'value'
}
],
2).echarts(pie饼图) 不需要xAxis,yAxis。tooltip->formatter多一个  d（饼图：百分比 | 雷达图：指标名称）
93.安装postman(http rest接口测试)
1).Postman_v4.1.3.crx -> Postman_v4.1.3.zip -> 解压到Postman_v4.1.3文件夹
-> google浏览器（更多工具->扩展程序->开发者模式->加载已解压的扩展程序->打开Postman_v4.1.3文件夹）
94.json格式化：https://www.json.cn/  
95.https使用form提交
96.mybatis大于转译
<![CDATA[
    and (work_year >=#{workYear1} and work_year <=#{workYear2})
]]>
97.jquery获取5-20之间的随机数	var x = 20;
var y = 5;
var rand = parseInt(Math.random()*(x-y+1)+y);
98.每3秒调用一次addCount()：
$(function() {
//设置定时调用
var timer = setInterval('addCount()',3000);
//停止定时调用
clearInterval(timer);
//再次启动 定时调用
timer = setInterval('addCount()',3000);
});
function addCount() {
}		
99.window->preference->User Settings
100.<a href="javascript:addCount('zhab','${idnumber}');"</a>
101.js获取主机名+端口号（location.host），跳转：window.location = "http://"+location.host;
102.maven-search Files (pom、jar View All)，点击View All ..-sources.jar 源码包
103.hbase获取最新的一行记录：
Scan scan = new Scan();
scan.setReversed(true);
ResultScanner rss = table.getScanner(scan);
Result[] result = rss.next(1);
System.out.println("haha" + new String(result[0].getRow(), "utf-8"));
104.查询重复数据：
select *
from table1 a
where rowid != (select max(rowid)
from table1 b
where a.name1 = b.name1
and a.name2 = b.name2……)

105.删除重复数据：
delete from table1 a
where rowid != (select max(rowid)
from table1 b
where a.name1 = b.name1
and a.name2 = b.name2……)
106.truncate table 只删除表数据，不删除表结构，不触发trigger;ddl语句，自动提交，速度比delete快。
107.oracle获取所有用户表的表数据量：
select 'select count(*) from '|| table_name ||';' from user_tables;
108.oracle取第一条数据： where rownum=1
109.虚拟机安装操作系统报错（Inter VT-x ...）：重启进入bios->选择advanced->cpu setup->Intel(R) V... ->enabled
110.VM虚拟机 网络设置：
1).bridged（桥接模式）：类似局域网中的一台独立主机
桥接模式centos虚拟机下 etc/sysconfig/network-script/ifcfg-eth0文件修改（需要以root登录，否则无法修改）为：

	DEVICE="eth0"
	BOOTPROTO="static"
	HWADDR="00:0C:29:75:FD:7E"
	MTU="1500"
	NM_CONTROLLED="yes"
	ONBOOT="yes"
	IPADDR="10.39.136.202"
	NETMASK="255.255.255.0"
	GATEWAY="10.39.136.254"
	
	其中IPADDR与主机ip在同一网段，GATEWAY默认网关与主机一致
111.xftp4连接虚拟机，协议选择SFTP
112.pl/sql连接oracle， service_name=orcl (orcl是sid)
113.ORACLE分页sql:
select *
from (select rownum ro, t.* from CZRK_CZRK t where rownum <= (20 * 3))
where ro > 20 * (3 - 1)
114.服务器连接hbase需要放入hosts文件,路径: C:\Windows\System32\drivers\etc
115.create table nameA as select * from nameB
116.oracle 复制数据库
select 'create '|| table_name ||' as select * from ycsjzl_qt.'||table_name ||';' from user_tables;
117.mongodb查询：
db.表名.find({ "$and" : [ { "字段名1" : "字段值1"},{ "字段名2" : "字段值2"}]}).skip(0).limit(500)
118.jsp html table <c:forEach>下，判断td字段值
<td>
<c:choose>
<c:when test="${xjwz.mz=='05'}">
维吾尔族
</c:when>
<c:otherwise>
其他
</c:otherwise>
</c:choose>
</td>
119.js每20秒执行一次函数：
function upMove(){
console.log("111");
}
$(function(){
window.setInterval(upMove, 1*1000*20);
})
120.eclipse变量跟踪（变色）:shift+alt+o
121.Hbase根据rowkey查询，并取出结果：
Get get = new Get(rowKey);
// Set the column family name and column name.
get.addColumn(familyName, qualifier[0]);
get.addColumn(familyName, qualifier[1]);
// Submit a get request.
Result result = table.get(get);
// Print query results.
for (Cell cell : result.rawCells()) {
LOG.info(Bytes.toString(CellUtil.cloneRow(cell))
+ ":" + Bytes.toString(CellUtil.cloneFamily(cell))
+ "," + Bytes.toString(CellUtil.cloneQualifier(cell))
+ "," + Bytes.toString(CellUtil.cloneValue(cell)));
}
122.Hbase过滤查询：
// 获取表描述符
HTableInterface table = (HTableInterface) InitHWAuthUtil
.getInstance().getHTable(
QueryWatch.WATCH_TIME_INDEX_TABLE_NAME);
// Scan 扫描器实例
Scan scan = new Scan();
// 使用PageFilter进行查询
PageFilter pageFilter = new PageFilter(pageCount);
scan.setFilter(pageFilter);
// 设置扫描器缓存大小，缓存面向行一级操作，每次获取几行数据
// scan.setCaching(20);
scan.setCacheBlocks(true);
//倒序
scan.setReversed(true);
scan.setStartRow(Bytes.toBytes(endTime));
scan.setStopRow(Bytes.toBytes(startTime));
// 进行扫描
resultScanner = table.getScanner(scan);	 
// 循环遍历
for (Result result : resultScanner) {
String rowkey = Bytes.toString(result.getRow());
}
123.cmd exp命令导出表(full=y是导出整个库)：
exp CLGJDSJ_320/CLGJDSJ_320@50.16.134.27:1521/ORCLETL file=d:/T_BASE_DLJKJCXX_YC.dmp tables=(T_BASE_DLJKJCXX_YC)
imp cldsj_ht/cldsj_ht@50.144.2.39:1521/ycdsjfwpt fromuser=CLGJDSJ_320 touser=cldsj_ht file=d:/T_BASE_DLJKJCXX_YC.dmp full=y ignore=y
124.springMVC配置多个视图解析器（html和jsp）
<bean id ="freeMarkerConfigurerId" class="org.springframework.web.servlet.view.freemarker.FreeMarkerConfigurer">
<property name="templateLoaderPath" value="/view/html/" />
<property name="defaultEncoding" value="utf-8" />
</bean>
<bean id="htmlViewId" class="org.springframework.web.servlet.view.freemarker.FreeMarkerViewResolver">
<property name="viewClass" value="org.springframework.web.servlet.view.freemarker.FreeMarkerView"/>
<property name="contentType" value="text/html;charset=utf-8"/>
<property name="order" value="0"/>
<property name="suffix" value=".html"/>
</bean>

	<bean id="jspViewId" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<property name="viewClass" value="org.springframework.web.servlet.view.InternalResourceView"/>
		<property name="order" value="1"/>
		<property name="prefix" value="/view/jsp/"/>
		<property name="suffix" value=".jsp"/>
	</bean>	
125.获取客户端ip（输入ip地址访问）:
String ip = request.getRemoteAddr();
126.eclipse打jar包文件：MANIFEST.MF；导出的jar包和引用资源放到同一目录下(lib、conf等)。
127.jdbc封装、查询：
/**
* dbcp
*/
public static DataSource getDataSource(String url, String username, String password) {
BasicDataSource dataSource = new BasicDataSource();
dataSource.setUrl(url);
dataSource.setUsername(username);
dataSource.setPassword(password);
return dataSource;
}
/**
* dbutil工具
*/
public static String getUpdateTimeQuery(String sql, Object params, DataSource dataSource) {
try {
QueryRunner queryRuner = new QueryRunner(dataSource);
List<Map<String, Object>> list = queryRuner.query(sql, new MapListHandler());
if (list != null && !list.isEmpty() && list.get(0).get("updateTime") != null) {
return list.get(0).get("updateTime").toString();
} else {
return "";
}
} catch (Exception e) {
LOG.error("Error occured while attempting to query data", e);
return "";
}
}
128.多线程执行。
public static void main(String[] args) {
//线程池接口。newCachedThreadPool：可重用固定线程数的线程池
ExecutorService pool = Executors.newCachedThreadPool();
for (int i = 0; i < 10; i++) {
Thread thread = new UpdateNameThread();
pool.execute(thread);
}
pool.shutdown();
}
class UpdateNameThread extends Thread {
@Override
public void run() {
IDNumberJDBCUtil.updateName2();
}
}
129.查询oracle某用户下各表注释及行数：
select a.table_name,b.comments,a.num_rows from user_tables a,user_tab_comments b where a.table_name=b.table_name;
130.eclipse报内存溢出（PermGen space）：
window->preferences->installed jres->jdk edit->Default VM arguments:  -Xms512M -Xmx1024M -XX:PermSize=512M -XX:MaxPermSize=1024M
131.Hbase:主表的索引作为索引表的rowkey,主表的rowkey作为索引表的列
132.Hbase查询表行数：
long totalCount=new AggregationClient(conf).rowCount(TableName.valueOf("DimensoftWatch_HphmJgskIndex"), new LongColumnInterpreter(), scan);
133.tomcat项目配置ip直接访问：
1).tomcat server.xml 端口号改为80;且加上 <Context docBase="ddm" path="/" reloadable="true" />;
2).web.xml中welcome-file改为首页路径
134.Maven配置jar包文件夹路径：window->preference->maven->User Settings->User Settings 配置settings.xml文件路径；
settings.xml中再配置jar包的repository(例：<localRepository>D:\soft\m2\repository</localRepository>)
135.hbase过滤查询(根据rowkey查询，设置起始rowkey,结束的rowkey。及根据某字段的值查询)：
Scan scan = new org.apache.hadoop.hbase.client.Scan();
String familyName = "GC";
scan.addFamily(Bytes.toBytes(familyName));
//scan.addColumn(Bytes.toBytes(familyName), Bytes.toBytes("HPHM"));
String hphm = "苏JP238J";
scan.setStartRow(Bytes.toBytes(hphm));
scan.setStopRow(Bytes.toBytes(hphm+"99"+"20190418120042"+"999900000000000108"));
FilterList filterList = new FilterList(
FilterList.Operator.MUST_PASS_ALL);
Filter rowFilter1 = new RowFilter(CompareFilter.CompareOp.EQUAL,new RegexStringComparator(kkbh));
filterList.addFilter(rowFilter1);		
//查询号牌号码 苏JP238J的记录
if (StringUtils.isNotBlank(hphm)) {
Filter colfier = new SingleColumnValueFilter(
Bytes.toBytes(familyName), Bytes.toBytes("HPHM"),
CompareFilter.CompareOp.EQUAL, Bytes.toBytes(hphm));
filterList.addFilter(colfier);
scan.setFilter(filterList);
}
136.oracle查询常住人口年龄小于14周岁的数量（视图）
create or replace view czrk_view_lt14 as
select count(*) lt14_count from(
select floor(months_between(sysdate,csrq)/12) as age  from CZRK_CZRK
) tt
where tt.age<14;
137.Hbase插入rowkey及其他字段。
String rowKey = (String)c.get("RYSBH")+(String)c.get("SFHM");
Put putRow = new Put(Bytes.toBytes(rowKey));
for (Map.Entry<String, Object> entry : c.entrySet()) {
//System.out.println(entry.getKey() + " " + entry.getValue());
putRow.addColumn(Bytes.toBytes(familyname), Bytes.toBytes(entry.getKey()),
Bytes.toBytes(entry.getValue().toString()));
}		
138.Map排序示例（根据key升序）
public class SortMap {
public static void main(String[] args) {
Map<String, Object> map = new HashMap<String, Object>();
map.put("1", "aa");
map.put("3", "cc");
map.put("2", "bb");
Map<String, Object> sortMap = new TreeMap<String, Object>(new MapKeyComparator());
sortMap.putAll(map);
}
}
class MapKeyComparator implements Comparator<String> {
@Override
public int compare(String o1, String o2) {
return o1.compareTo(o2);
}
}
139.git版本回退：https://blog.csdn.net/gomeplus/article/details/78241070
140.git detached head解决方法:
$ git branch
$ git checkout master
$ git pull
141.redis配置文件 redis.conf
1).注释掉：bind 127.0.0.1
2).加上密码：requirepass aipai123
142.java 两个日期相减，获取差值（返回xx天xx小时...）
public static String getDistanceTime(Date date1, Date date2){
long day = 0;
long hour = 0;
long min = 0;
long sec = 0;
long time1 = date1.getTime();
long time2 = date2.getTime();
long diff ;
if(time1<time2) {
diff = time2 - time1;
} else {
diff = time1 - time2;
}
day = diff / (24 * 60 * 60 * 1000);
hour = (diff / (60 * 60 * 1000) - day * 24);
min = ((diff / (60 * 1000)) - day * 24 * 60 - hour * 60);
sec = (diff/1000-day*24*60*60-hour*60*60-min*60);
return day + "天" + hour + "小时" + min + "分" + sec + "秒";
}
143.lib下的jar包添加到pom中
<dependency>
<groupId>com.dhr.aipai</groupId>
<artifactId>sandpay-cashier-sdk-2.0.1</artifactId>
<version>2.0.1</version>
<scope>system</scope>
<systemPath>${project.basedir}/src/main/resources/lib/sandpay-cashier-sdk-2.0.1.jar</systemPath>
</dependency>
144.linux查找文件： find / -name '*aipai*'
145.linux启动jar包命令：
nohup java -Xms1024m -Xmx6144m -jar aipai-0.1.0.jar > 20180823.log &
146.oracle number类型，不加长度，对应java，java.math.bigdecimal
147.mysql decimal对应mybatis java.math.bigdecimal类型					 
148.mysql获得一小时前的时间点：
DATE_SUB(NOW(),INTERVAL  1 HOUR);
149.Cron表达式范例：
@Scheduled(cron = "0 30 09 * * ?") 每天上午9:30触发
@Scheduled(cron = "0 0 */1 * * ?") 每小时执行一次
150.解决navicat连接mysql失败（1251--Client does not support authentication protocol requested by server）
登录cmd命令行(mysql -uroot -p123456)执行：
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
低版本Mysql使用：
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('new_password');
151.maven中web项目依赖的项目被打包成了jar：
打开（eclipse:window->show view->other->搜索nav）navigator视图->查看变成Jar包的项目的.settings目录下的配置文件,
比对是否缺失文件（org.eclipse.wst.common.project.facet.core.xml等），或者文件中缺失配置，拷贝其他项目的文件放入。
152.SELECT USER_NO from ap_customer  
GROUP BY USER_NO
HAVING count(*)>1
153.tomcat启动修改cmd标题：bin目录下catalina.bat文件修改：
if "%TITLE%" == "" set TITLE=cldsj
154.linux crond服务、crontab命令 定时备份数据库
1). /etc/crontab 编写crontab命令
2).查看crond的服务状态：status crond.service
3).service crond start （restart等）
155.mysql导出数据库(windows cmd导出 末尾不要加分号)
mysqldump -P3307 -u root -p test> D:\test.sql
156.sql left join时，小表（数据量少的）放左边
157.eclipse快捷键:ctrl+shit+t 查方法所属jar包
158.Runnable vs. Callable in Java
1).Runnable tasks can be run using the Thread class or ExecutorService,
Callables can be run only using the ExecutorService.
2).Callable可以有返回值
159.window.open()不能放在ajax的success中执行，否则会被chrome浏览器拦截（被当做广告了）
160.javascript encodeURI()（url编码）、encodeURIComponent()（url解码）
161.// URL url = ClassLoader.getSystemResource("SIMKAI.TTF");
URL simplifiedChineseUrl = Thread.currentThread().getContextClassLoader().getResource("./SIMKAI.TTF"); //加载字体文件（解决linux环境下无中文字体问题）
162.字段直接赋值，并改为字段类型：
select cast('文字' as nvarchar2(100)) from utest;
163.js字符串替换：
var str="a,b,c";
str.replace(/,/g,'→');
"a→b→c"
164.css3属性：
[class^='icon-'], [class*=' icon-'] { display:inline-block;  }
^:class以icon-开头;
$:以.结尾;
[class*='icon']:类名包含icon;
165.setTimeout只在指定时间后执行一次：
function test() {     			
} 			
window.setTimeout(function() {
test();
}, 1000);
166.后台转Json：
JSONObject json = new JSONObject();
JSONArray jsonArray = JSONArray.fromObject(list);
return jsonArray.toString();
前端：var list = '${list}';
var listArray = $.parseJSON(list);
for(var i=0;i<listArray.length;i++){
myAddIcon(listArray[i].JD,listArray[i].WD,listArray[i].JWD_NAME);
}
167.后台map接收参数：
Map map = super.getParamValues(request);
protected static Map<String, String> getParamValues(
HttpServletRequest request) {
Map<String, String> map = new HashMap<String, String>();
@SuppressWarnings("rawtypes")
Enumeration names = request.getParameterNames();
while (names.hasMoreElements()) {
String key = (String) names.nextElement();
String value = request.getParameter(key);
if (value != null && value != "") {
map.put(key, value);
}
}
return map;
}
168.获取oracle clob字段，展示到页面上(头像)
1).<result column="user_img" jdbcType="CLOB" property="userImg" />
2).Map map2 = loginManager.getUserImg(map);
oracle.sql.CLOB userImgClob = (oracle.sql.CLOB)map2.get("userImg");
Reader is;
String userImg = "";
try {
is = userImgClob.getCharacterStream();
BufferedReader br = new BufferedReader(is);
String string = br.readLine();
StringBuffer sBuffer = new StringBuffer("");
while(string!=null){
sBuffer.append(string);
string = br.readLine();
}
userImg = sBuffer.toString();
} catch (Exception e1) {
e1.printStackTrace();
}
3).var imgSrc = 'data:image/jpeg;base64,'+'${userImg}';
$(".user-image").attr("src",imgSrc);
169.activiti修改流程图：(流程定义表：act_re_procdef,version_字段)		
1).bpmn修改流程：sequenceFlow :
<conditionExpression xsi:type="tFormalExpression"><![CDATA[${path=="handleEnd"}]]></conditionExpression>
2).FormController:  action.put("handleEnd", "办结");
3).SendFileService: path = String.valueOf(param.get("path"));
variables.put("path", path);
if("handleEnd".equals(path)){
taskService.complete(taskId, variables);
}
4).diagram.jsp、sendFile_draft.jsp
170.Hbase表查询 rowkey按首字母/数字 查询(按字典排序)。rowkey ：start/end hphmValue1 ->hphmValue2 ...
171.custom-fat.jar (将所有需要的资源全部打到jar包中，使项目可以直接使用)
172.<!-- 启动对@Aspectj注解的支持 -->
<aop:aspectj-autoproxy proxy-target-class="true" />
<!-- 将自定义的切面类注入Spring容器 -->
<bean class="com.njws.aop.LogAspect" />
173.删除eclipse中svn记录，以便更好svn账户(C盘扫描Subversion)：
C:\Users\FTP\AppData\Roaming\Subversion\auth
SVN账号在登录的时候，默认是保存在个人电脑的C:\Users\Administrator\AppData\Roaming\Subversion\auth\svn.simple\ 目录下的。
如果需要切换别的账号，需要怎么做呢？ 勾选需要清除的账号，点击OK即可清除历史账号。
清除后，即可用新的账号密码访问了
174.tomcat server.xml中配置https (https://50.144.0.47:8443/stcldsj/loginByPki.xhtml):
<Connector SSLEnabled="true" URIEncoding="UTF-8" acceptCount="500" clientAuth="want"
connectionTimeout="30000" disableUploadTimeout="true" enableLookups="false"
keystoreFile="C:/1111" keystorePass="11111111" maxProcessors="300" maxSpareThreads="75"
maxThreads="300" minProcessors="50" minSpareThreads="5" port="8443"
protocol="org.apache.coyote.http11.Http11Protocol" scheme="https" secure="true"
sslProtocol="TLS" truststoreFile="C:/1111" truststorePass="11111111"/>
175.1).application-springmvc.xml:
xmlns:aop="http://www.springframework.org/schema/aop"
<!-- 启动对@Aspectj注解的支持 -->
<aop:aspectj-autoproxy proxy-target-class="true" />
<!-- 将自定义的切面类注入Spring容器 -->
<bean class="com.njws.aop.LogAspect" />
2).切面类
@Aspect
public class LogAspect{
@AfterReturning("within(com.ws..*) && @annotation(la)")
public void after(JoinPoint jp, LogAnnotation la) {}

			@AfterThrowing(pointcut="within(com.njws.controller..*) && @annotation(la)", throwing="ex")
			public void logException(JoinPoint joinPoint, LogAnnotation la, Exception ex) {}
		}
	3).自定义注解
		@Retention(RetentionPolicy.RUNTIME)
		@Target({ElementType.METHOD})
		public @interface LogAnnotation {
			//操作所在模块或功能名称
			String operateName();
		}
176.hbase取rowkey
String rowkey = Bytes.toString(result.getRow());		
177.hbase取字段值
for (Result r = resultScanner.next(); r != null; r = resultScanner.next()) {
for (Cell cell : r.rawCells()) {
//rowkey:family,column,columnValue
//320900000000000106_20180926202557_苏JH199M:INDEX,HPHM,苏JH199M
LOG.info(Bytes.toString(CellUtil.cloneRow(cell)) + ":"
+ Bytes.toString(CellUtil.cloneFamily(cell)) + ","
+ Bytes.toString(CellUtil.cloneQualifier(cell)) + ","
+ Bytes.toString(CellUtil.cloneValue(cell)));
}
}
178.400 Bad	request error: 检查url参数类型是否正确(Date,String等 前后台是否对应)
179.oracle group by(类似mysql的group_concat)
select LISTAGG(t.comments,',') within group (order by t.column_name) comments from user_col_comments t
group by t.table_name
180.web.xml -> welcome-file-list -> getRootMap() -> ResourceBundle res = ResourceBundle.getBundle("urls")
->	urlsMap = new HashMap<String, String>();
Enumeration e = res.getKeys();
while (e.hasMoreElements()) {
String key = e.nextElement().toString();
String value = res.getString(key);
urlsMap.put(key, value);
}
-> new ModelAndView(viewName,map);
181.dom4j 解析xml，取得xml中数据(dom4j.jar、jaxen.jar)
Document doc = DocumentHelper.parseText(xml);
// 获取Row节点集合,当xml节点目录名称为:RBSPMessage/Method/Items/Item/Value/Row
List list = doc.selectNodes("RBSPMessage/Method/Items/Item/Value/Row");
// 判断节点是否为空同时节点大于2
if (list != null && list.size() > 2) {
// 获取第一个Row节点
Element stateElement = (Element) list.get(0);
// 获取返回数据状态
String state = ((Element) stateElement.elements().get(0)).getText();
if (state.equalsIgnoreCase("000")) {// 状态等于000代表结果返回正常
}
}
182.rest接口，调用方（客户端、spring库）：
restTemplate.postForObject("http://221.231.109.86:9090/insertOracle/rest/inserting/insertOracle",list, ArrayList.class);
String maxTime = restTemplate.getForObject("http://localhost:8080/insertOracle/rest/inserting/getMaxTime", String.class);
提供方（服务端、接收方、javax.ws.rs-api库、jersey）：
@POST
@Path("insertOracle")
@Produces({ "application/json", "application/xml" })
public String insert(String list) {}
183.idea ctrl+shift+N 查看文件和类、alt+7查看类中所有方法、sout(输出到控制台)
184.在 Windows 系统中，hosts文件的位置为：C:\Windows\System32\drivers\etc
185.Eclipse需要安装egit插件(github) https 	
186.身份验证错误,要求的函数不受支持(windows远程桌面连接问题)
1). 打开注册表，快捷输入 “regedit”（类似找命令提示符 输入 cmd 一样）
2).找文件夹 路径：HKLM(缩写)\Software\Microsoft\Windows\CurrentVersion\Policies\System\CredSSP\Parameters
大概到System 后就没有了自己创建文件夹就好。
3).然后再最底部文件夹里面 新建 DWORD（32）位的。
文件名 "AllowEncryptionOracle" ，值 : 2.
187.linux查看系统版本:
lsb_release -a
cat /etc/os-release
188.nohup java -jar a.jar > nohup.out 2>&1 &
2>&1的意思是将标准错误(2)也定向到标准输出(1)的输出文件中。
Linux 中三种标准输入输出，分别是STDIN，STDOUT，STDERR，对应的数字是0，1，2。
189.pkill -f abcd (匹配jar所在文件夹，停止进程) 	
190.图片转base64位字符串（oracle,spring库）
File file = new File("D:"+File.separator+"2.jpg");
fileBytes = FileUtils.readFileToByteArray(file);
String imgString = new sun.misc.BASE64Encoder().encode(fileBytes);
191.对js数组分组 (根据某个字段分组，转为json)
function groupBy(arr,prop){
var grouped = {};
for(var i=0;i<arr.length;i++){
var p = arr[i][prop];
if(!grouped[p]){
grouped[p] = [];
}
grouped[p].push(arr[i]);
}
return grouped;
}
192.js保留数组中的前3个：valueArray.splice(3,valueArray.length);
193.eclipse配置自定义文件夹为lib包：eclipse ->properties-> deployment assembly ->add -> folder (编译时加载lib包)
194.css div居中：{position: absolute;top:0;bottom: 0;left:0;right: 0;margin: auto;}
195.var el = document.createElement('img');
el.setAttribute("kkbh", "3209");
$(el).click(function(){});//增加点击事件
196.var div = $.clone(document.getElementById('sbpop'));
$(div).find("#kkbh").text('aaa');
$(div).show();
197.<div onclick="javascript:refresh('../qbxxsb.html')">aa</div>
function refresh(url){
top.window.location.href = url;
}
198.(对象锁) 代码块：synchronized(this)(或者object等)、普通方法前加synchronized
199.(类锁)   代码块：synchronized(类名.class)、static方法前加synchronized，全局唯一
200.修改linux的jdk版本、maven版本(/etc/profile)
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_211
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
export MAVEN_HOME=/usr/local/apache-maven-3.5.3
export PATH=${MAVEN_HOME}/bin:$PATH
source /etc/profile  (使配置生效)
201.查看Linux版本：lsb_release -a
202.linux修改字符编码 /etc/sysconfig/i18n
203.tomcat/conf文件夹下tomcat-users.xml:<user username="tomcat" password="tomcat" roles="manager-script"/>
tomcat/webapps的manager接口(/list、/reload、/start、/stop)：http://localhost:8080/manager/text/start?path=/tt
204.修改tomcat配置，url访问日志：http://localhost:8080/logs/catalina.2019-04-29.log
1).修改tomcat/conf下的logging.properties  改为${catalina.base}/webapps/ROOT/logs
2).修改tomcat/bin/catalina.sh  	改为CATALINA_OUT="$CATALINA_BASE"/logs/catalina.out
205.css中!important的优先级最高，高于内置的style，慎用!important。
206.windows cmd 根据pid查询端口号，kill：
netstat -aon|findstr "3306"
taskkill /T /F /PID 9088
netstat -ano | findstr pid
pid可以在屏幕最下方任务栏右击->点击任务管理器->服务 查到
207.freemarker ${(map.code)!""}  这种方式，能够处理map或者code为miss value的情况
208.navicat查看mysql版本: select version() from dual;
209.linux停止某个tomcat.
kill -9 `ps -ef | grep /usr/local/tomcat-gxr | grep java | awk '{print $2}'`
210.eclipse目录eclipse.ini
-vm
D:\jdk8\jdk1.8.0\jre\bin\server\jvm.dll
211.postman post:body里放json对象，raw、JSON(application/json)
{
"fileId":"0416ac7e-d7b1-4977-8450-74710a3c3f01",
"flag":"send"
}
212.java后台get方式可以使用
String name = request.getParameterMap().containsKey("name")?request.getParameter("name"):"";接收参数
213.java后台post方式可以使用(@RequestBody Map<String, Object> arg)接收参数
214.tld文件使用：
1).web.xml:
<jsp-config>
<taglib>
<taglib-uri>http://www.njws.cn/jsp/jtl/functions</taglib-uri>
<taglib-location>/WEB-INF/pages/common/njws.tld</taglib-location>
</taglib>
</jsp-config>
2).jsp: (加载jsp页面时，会请求后台，将这个页面用到的字典都放入)
${fun:getSelectedOptions("ZDLX",dict.flag)}
3).tld:
<short-name>fun</short-name>
<uri>http://www.njws.cn/jsp/jtl/functions</uri>
<function>
<name>getSelectedOptionsWithDefaultValue</name>
<function-class>com.ws.sys.core.utils.tags.DictionaryTag</function-class>
<function-signature>java.lang.String getSelectedOptions(java.lang.String,java.lang.String,java.lang.String)
</function-signature>
</function>
4).java:DictionaryTag类 getSelectedOptions(String dicCode, String dicItemCode)
215.main方法中直接加载spring及mapper
ApplicationContext context=new ClassPathXmlApplicationContext("context*.xml");
JdcdjMapper jdcdjMapper=(JdcdjMapper)ServiceLocator.getInstance().getService(JdcdjMapper.class);
216.spring-servlet.xml
<!--拦截器 权限控制 -->
<bean
class="org.springframework.web.servlet.mvc.annotation.DefaultAnnotationHandlerMapping">
<property name="interceptors">
<list>
<bean class="com.ws.sys.core.web.interceptor.AccessControlInterceptor" />
<bean class="com.ws.sys.core.web.interceptor.PermissionInterceptor" />
</list>
</property>
</bean>
public class AccessControlInterceptor extends HandlerInterceptorAdapter
217.maven模块项目，svn下载后删除（不删除磁盘项目），再重新以maven项目导入
218.eclipse打开ftl格式文件报空指针错误：windows->preferences-general-editors-file associations-
关联 *.ftl与jsp关联。content types :jsp->jsp fragment 增加*.ftl再设置编码格式utf-8(update)
219.spring配置通过@Value("${xx.xxx}")取yml或properties文件中属性
220.bi导出可执行jar，选择 copy required libraies into a sub-folder ...
221.去掉后缀：web.xml配置 不加.后缀访问Controller
<servlet>
<servlet-name>Spring-Servlet</servlet-name>
<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value>
classpath:spring-servlet.xml
</param-value>
</init-param>
<load-on-startup>1</load-on-startup>
</servlet>
<servlet-mapping>
<servlet-name>Spring-Servlet</servlet-name>
<url-pattern>/*</url-pattern>
</servlet-mapping>
222.maven模块化项目，模块调用另一个模块报错，查看下parent
<parent>
<groupId>com.ws</groupId>
<artifactId>qbzhpt</artifactId>
<version>0.0.1-SNAPSHOT</version>
</parent>
223.KafkaConsumer构造失败(Failed to construct kafka consumer)：
查看krb5.conf、user.keytab文件是否读取到！
224.ul、li切换
<ul class="a-ul">
<li class="on">aa</li>
<li>bb</li>
<li>cc</li>
</ul>
// .a-ul li：指li在这个ul中的排序(.divParent .div 通用)
$('.a-ul li').click(function(){
if($(this).hasClass('on')){
$(this).removeClass('on');
if($(this).index() == 0 ){
console.log('has-a,\nto do...');
}else if($(this).index() == 1 ){
console.log('has-b,to do...');
}else if($(this).index() == 2 ){
console.log('has-c,to do...');
}
}else{
$(this).addClass('on');
if($(this).index() == 0 ){
console.log('not has-a,to do...');
}else if($(this).index() == 1 ){
console.log('not has-b,to do...');
}else if($(this).index() == 2 ){
console.log('not has-c,to do...');
}
}
});
225.maven pom修改后，需要进行maven->update project操作
226.默认选中下拉框中的某个option: $("selectId").val("");
227.pl/sql安装，配置中文
1).查询出服务端编码:select userenv('language') from dual;(AMERICAN_AMERICA.ZHS16GBK)
2).配置环境变量：NLS_LANG=AMERICAN_AMERICA.ZHS16GBK(上步查询出的编码)
228.页面debugger拿到json,json转换为字符串：JSON.stringify(json)   
229.js string转json(JSON.parse(data)): var data ="[[120.12645,33.39428],[120.12601,33.39419]]";
JSON.parse(data) 将data转为：数组[[120.12645,33.39428],[120.12601,33.39419]]
230.HandlerInterceptorAdapter 处理器拦截器适配器：afterCompletion(...,Exception ex) 可以打印全局异常处理
231.nohup java -jar ./qbzhpt-yjzh-0.0.1-SNAPSHOT.jar -Dwebname=qbzhpt-yjzh >/dev/null 2>&1 &
232.多线程：
public void getDataAll() {
List<Map<String, Object>> list = JDBCUtils.getInstance().getData(sql);
ExecutorService pool = Executors.newFixedThreadPool(100);
int each = list.size() / 100;
for (int i = 0; i < 100; i++) {
	pool.execute(new GetFromHbaseThread(list.subList(i*each, i==99? list.size(): (i+1)*each)));
}
pool.shutdown();
}
class GetFromHbaseThread extends Thread{
final List<Map<String, Object>> list;
public GetFromHbaseThread(List<Map<String, Object>> subList) {
	list = subList;
}
@Override
public void run() {
	try {
		HBaseSample.getData(list);
	} catch (IOException e) {}
	}
} = Executors.newFixedThreadPool(100);
int each = list.size() / 100;
for (int i = 0; i < 100; i++) {
	pool.execute(new GetFromHbaseThread(list.subList(i*each, i==99? list.size(): (i+1)*each)));
}
	pool.shutdown();
}
class GetFromHbaseThread extends Thread{
final List<Map<String, Object>> list;
public GetFromHbaseThread(List<Map<String, Object>> subList) {
list = subList;
}
@Override
public void run() {
try {
HBaseSample.getData(list);
} catch (IOException e) {}
}
}
233.linux查看当前目录文件夹大小：du -sh * | sort -nr
234.springmvc传递list(列表数据放到Body中，post方式传递): http://localhost:8088/insert?topic=cccc
[{"date":"20190726", "cap_time":"20190726131313"},{"date":"20190727", "cap_time":"20190727161616"]
@RequestMapping(value = "/insert",method = RequestMethod.POST)
public Map<String, Object> test(String topic, @RequestBody List<Map<String, Object>> list) {}
235.(String转Map,str="{date=20190726}" )jackson-databind-2.6.3.jar
ObjectMapper mapper = new ObjectMapper();
Map readValue = mapper.readValue(str, Map.class);
(String转JSONArray,str="[{"ID":"1","VALUE":"a"},{"ID":"2","VALUE":"b"}]" )
JSONArray array = mapper.readValue(str, JSONArray.class);
236.plsql配置：Tools->preferences .\instantclient_11_1、.\instantclient_11_1\oci.dll
237.window.parent.$('.layui-layer').css({'background-color':'','background-image':"url('<%=request.getContextPath()%>/view/ws_main/images/ydzh/y-bodybg.jpg')",'top':'20px'});
238.mysql中文乱码：表结尾加上：DEFAULT CHARSET=utf8;
239.websocket:
js: var websocket = new WebSocket('ws://localhost:8080/getData');
//onopen用于指定连接成功后的回调函数
websocket.onopen = function(){};
//onmessage用于指定当从服务器接受到信息时的回调函数
websocket.onmessage = function(event){
JSON.parse(event.data);
}
java:
@ServerEndpoint("/getData")
@Component
public class TestClass(){
@OnOpen //建立连接时触发
public void onOpen(){}
@OnMessage //收到客户端消息时触发
public void onMessage(String message,Session session){}
}
240.oracle NUMBER(precision,scale):precision代表数字总长度,scale表示小数点后数字位数
241.oracle 获取当前时间一小时前:sysdate - interval '1' hour
242.mvn clean package -pl qbzhpt-yjzh -am  -Dmaven.test.skip=true
243.Java Oracle Clob转String.
CLOB clob = null;
InputStream in = clob.getAsciiStream();
StringWriter w = new StringWriter();
IOUtils.copy(in, w);
w.toString();
244.poi处理excel日期（数字转字符串格式）:
DataFormatter formatter = new DataFormatter();
formatter.formatCellValue(row.getCell(10));
245.nginx:nginx.exe -s reload
246.nginx:
#对/ydpcs开头的路径 进行负载均衡请求
http://221.231.109.86:9091/kqxxForward/ydpcs/insertUserTemperature.html
location /ydpcs{
proxy_pass http://50.144.0.47:8089/ydpcs   #请求转向 定义的服务器列表
}
247.Hbase索引表完善:主表的索引作为索引表的rowkey,主表的rowkey作为索引表的列
T_320_CLGJXX： String rowkey = hphmValue+hpzlValue+jgskValue+kkbhValue;
DimensoftWatch_KkbhIndex ： String rowkey = kkbhValue + "_" + jgskValue + "_" + hphmValue ;
DimensoftWatch_TimeIndex：String rowkey = jgskValue + "_" + kkbhValue + "_" + hphmValue;
DimensoftWatch_HphmJgskIndex：String rowkey = hphmValue + "_" + jgskValue;
248.RestTemplate接口示例：
String url = "http://50.144.0.48:8080/yc_wwyjpt/qbpt/qxbk/getRygj.xhtml?pageNum="+pageNum+
"&numPerPage="+numPerPage+"&queryParam="+query+"&startTime="+startTime+"&endTime="+endTime;
HttpHeaders headers = new HttpHeaders();
headers.setAccept(Arrays.asList(MediaType.APPLICATION_JSON));
HttpEntity<String> entity = new HttpEntity<String>(headers);
ResponseEntity<String> result = restTemplate.exchange(url, HttpMethod.GET,entity,String.class);
ObjectMapper mapper = new ObjectMapper();
Map resultMap = mapper.readValue(result.getBody(),Map.class);
List<Map<String, String>> datas = (List<Map<String, String>>) resultMap.get("allData");
249.javascript倒排序一个js字符串: str.split("").reverse().join("");
250.本机git关联github：
cmd->ssh-keygen ,生成验证码(存在生成的目录下 id_rsa.pub文件中) 拷贝到github个人主页->setting-> SSH and GPG keys
git clone git@github.com:xxxx.git
git pull origin master
git add xx.txt
git status
git push origin master
251.U会是否报名sql(简化版):
SELECT t1.*,
CASE ISNULL(t2.id)
WHEN '1' THEN '0'
ELSE '1' END is_join from uin_meetings t1
LEFT JOIN (select MEETING_ID from uin_meetings_history) t2
on t1.id = t2.MEETING_ID
where t1.USER_ID = '18662062998'
252.div高度超出，加滚动条
height: 200px;  
overflow: auto;	 
253.jdk自带的证书生成工具keytool.(cmd敲命令即可)
1).为服务端生成证书：
keytool -genkey -v -alias tomcat -keyalg RSA -keystore D:\home\tomcat.keystore -validity 36500
2).为客户端生成证书：
keytool -genkey -v -alias mykey -keyalg RSA -storetype PKCS12 -keystore D:\home\mykey.p12
3).让服务端信任客户端证书：
keytool -export -alias mykey -keystore D:\home\mykey.p12 -storetype PKCS12 -storepass 123456 -rfc -file D:\home\mykey.cer
4).让客户端信任服务器证书：
keytool -keystore D:\home\tomcat.keystore -export -alias tomcat -file D:\home\tomcat.cer
5).tomcat server.xml配置：
<Connector SSLEnabled="true" URIEncoding="UTF-8" acceptCount="500" clientAuth="want"
connectionTimeout="30000" disableUploadTimeout="true" enableLookups="false"
keystoreFile="D:\home\tomcat.keystore" keystorePass="123456" maxProcessors="300" maxSpareThreads="75"
maxThreads="300" minProcessors="50" minSpareThreads="5" port="8443"
protocol="org.apache.coyote.http11.Http11Protocol" scheme="https" secure="true"
sslProtocol="TLS" truststoreFile="D:\home\tomcat.keystore" truststorePass="123456"/>
6).测试： https://127.0.0.1:8443/query?topic=00002
254.tomcat bin\startup.bat启动闪退，可在文件最后一行加上 pause
tomcat启动报错：Tomcat Neither the JAVA_HOME nor the JRE_HOME environment variable is defined
-- setlocal
set JAVA_HOME=C:\Java\jdk1.8.0_45
set JAVA_JRE=C:\Java\jdk1.8.0_45\jre
255.全局异常的处理：@ControllerAdvice + @ExceptionHandler(Exception.class)
@ControllerAdvice
public class SpringControllerAdvice {
@ExceptionHandler(Exception.class)
public ModelAndView exception(Exception e) {
e.printStackTrace();
return new ModelAndView("error");
}
}
256.oracle去重、合并
select idnumber, listagg(name,',') within group( order by name )
from name_table group by idnumber
257.nginx windows cmd
start nginx
tasklist /fi "imagename eq nginx.exe"
taskkill /T /F /PID 29608
nginx -s reload  
nginx -s quit
258.nginx conf/nginx.conf下配置路径转发
例：配置 nginx启动端口为 ：
server {listen       8088;}
rest项目配置location /dataAction {
proxy_pass http://localhost:8099;   #请求转向 定义的服务器列表
}
rest项目访问路径就由：http://localhost:8099/dataAction/query
变为：		  http://localhost:8088/dataAction/query
259.cmd测试 ip+端口号 是否可以连接
telnet 106.15.51.152 8080			
260.mybatis开启二级缓存：
mybatis.xml：
<settings>
<setting name="cacheEnabled" value="true" />
</settings>
mapper.xml:
<mapper>
<cache
eviction="LRU"
flushInterval="60000"   //缓存过期时间，单位为毫秒，60000即为60秒，缺省值为空，即只要容量足够，永不过期
size="1024"
readOnly="true"
/>
<select id="getOrder" parameterType="int" resultType="TOrder"  useCache="false">
</select>
useCache="false"表示该select语句不使用缓存（即使xml最开头的全局cache启用）
</mapper>
261.yum search java
yum install java-1.8.0-openjdk-devel.x86_64
262.springboot项目添加swagger，进行接口管理
<dependency>
<groupId>io.springfox</groupId>
<artifactId>springfox-swagger2</artifactId>
<version>2.9.2</version>
</dependency>
<dependency>
<groupId>io.springfox</groupId>
<artifactId>springfox-swagger-ui</artifactId>
<version>2.9.2</version>
</dependency>

	@Configuration
	@EnableSwagger2
	public class SwaggerConfig {
		@Bean
		public Docket api() {
			return new Docket(DocumentationType.SWAGGER_2)
					.select()
					.apis(RequestHandlerSelectors.any())
					.paths(PathSelectors.any())
					.build();
		}
	}
	http://localhost:8080/swagger-ui.html 可以看到效果
263.oracle 查询同车牌号时间最大的那一条数据
select * from (select row_number() over(partition by hphm order by time desc) rn, 表.*
from  表)  where rn = 1
264.oracle触发器，在插入一个表的时候，需要根据一个字段的值更新另一个字段的值：
create or replace trigger tri_debug_demo1
before insert on debug_demo1
for each row
begin
:new.note2 := :new.note;
end tri_debug_demo1;
265.启动tomcat报错：java.security.AccessControlException: access denied
找到文件jdk目录，E:\software\jdk1.7.0_60\jre\lib\security下的java.policy
然后在grant{}中的最后一行加上：permission java.security.AllPermission; 保存，然后重新启动即可
266.maven将第三方jar包，放入本地pom中
mvn install:install-file -Dfile=F:\git\ycpcs30\ycpcs30\libs\taobao-sdk-java-auto_1479188381469-20190806.jar -DgroupId=taobao-sdk-java -DartifactId=taobao-sdk-java -Dversion=2 -Dpackaging=jar
267.jquery绑定事件
$('body').on('click', '.name', function () {
$(this).parent.find('.pic-box').show();
//do sth...
});
268.div边框添加阴影效果: X轴偏移量、Y轴偏移量、模糊半径、扩散半径和颜色
box-shadow: 1px 1px 5px 5px rgba(0, 0, 255, .2);
269.前端传json,后端接收
var data = {
id:1,
name:"test"
}
$.ajax({
type : "post",
url : "/sys/saveData",
dataType : 'json',
contentType:'application/json',
data : JSON.stringify(data),
success : function(data) {
console.info(data);
}
});
@RequestMapping(value = "/saveData",method= RequestMethod.POST)
public ResultBean<Map> saveData(@RequestBody Map<String, Object> map){
String xxxx= (String) map.get("xxxx");
return null;
}
270.解决mouseover、mouseout一直循环触发导致的闪烁问题 ：
在需要隐藏显示的div上加上 pointer-events: none;
271.查看linux某个文件夹占用空间大小：  du -h --max-depth=1 /yd
272.服务器文件 拖不上去，报错 ：encountered 1 errors during the transfer.
先查看磁盘空间是否已满。
273.kafka 消费，groupId修改后， 就会将所有数据 重新开始消费
274. oracle->导入kafka(生产)->消费进hbase.
	 275.悬浮显示使用hover：
	 父hover后 改变子
	 .item-1:hover .item-1-child{
	 background-color:#50ff00;
	 }
	 改变相邻同级：
	 .item-1:hover +.item-2{
	 background-color:#50ff00;
	 }
	 改变不相邻同级：
	 .item-1:hover ~.item-3{
	 background-color:#50ff00;
	 }
	 276.关闭catalina.out打印日志：
	 1).在Tomcat的bin目录下找到catalina.sh
	 2).修改catalina.sh中的对应信息
	 if [ -z "$CATALINA_OUT" ] ; then
	 ? #CATALINA_OUT="$CATALINA_BASE"/logs/catalina.out
	 ? CATALINA_OUT=/dev/null
	 fi
	 277.tail -100 /文件路径  查看文件最后的100行
	 278.Oracle将多个相同字段的值合并到一条记录中
	 select id,username,wm_concat(address) from table group by id,username;
	 279.获取标签的name名称：$("#xxx").attr('name')
	 280.eclipse修改项目名称：
	 1).修改.project
	 2).修改项目目录：.settings\org.eclipse.wst.common.component
	 281.Eclipse 自动提示功能配置：Window > Preferences > Java > Editor > Content Assist   
	 282.oracle截取-前面的字符串：select substr('AAA-BBB',0,instr('AAA-BBB','-',-1)-1) 值 from dual;
	 283.css根据不同屏幕的分辨率设置宽度：
	 @media screen and(max-width:1300px){
	 .main{width:1000px;}
	 }
	 选择table下的第一个td： tr:first-child
	 选择table下的第二个td： tr:nth-child(2)
	 284.关闭Tomcat日志：server.xml和logging.properties
	 285.spring boot项目，修改pom文件后，可能会没重新加载到依赖等。
	 可以在 maven->plugins->spring-boot->spring-boot:run 运行下
	 286.idea -> maven -> runner ->
	 VM OPTIONS: -Dspring.profiles.active=dev	-Dspring-boot.run.fork=false
	 environment variables：SPRING_PROFILES_ACTIVE=dev
	 287.将sql文件导入到postgresql(使用cmd操作psql)：
	 1). open the cmd
	 2). SET PGCLIENTENCODING=utf-8
	 3). chcp 65001
	 4). psql -h localhost -U postgres
	 5). 查看数据库列表： \l
	 6). 切换到axione_isf6数据库： \c axione_isf6
	 7). sql文件导入到数据库：   \i F:/aliengen/v1.1.1.sql	 
	 288.centos安装docker:
	 yum install docker-ce docker-ce-cli containerd.io
	 289.使用docker安装mysql：
	 docker images
	 docker pull mysql:5.7.35
	 docker run -d -p 3306:3306 -v mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.35 --lower_case_table_names=1
	 netstat -na|grep 3306
	 sudo iptables -A INPUT -p tcp --dport 3306 -j ACCEPT
	 docker ps
	 290.docker安装postgresql
	 docker pull postgres
	 docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=admin -d postgres
	 docker exec -it 5f5048789aa441c109fb95827371b8f4de5b59f83d214910f9674c735571f545 bash
	 psql -U postgres
	 CREATE DATABASE axione_isf;
	 \q
	 291.docker buildx create --driver-opt env.BUILDKIT_STEP_LOG_MAX_SIZE=50000000
	 docker 使用Dockerfile 创建镜像：
	 docker buildx build -t test-docker .
	 //创建一个新的容器并运行镜像：
	 docker run -p 9090:9090 test-docker
	 292.评级组件（打星）：
	 var rate =3;
	 "★★★★★☆☆☆☆☆".slice(5 - rate, 10 - rate);
	 293.yum install db5 error(-30973) :
	 mkdir /var/lib/rpm/backup
	 cp -a /var/lib/rpm/__db* /var/lib/rpm/backup/
	 rm -f /var/lib/rpm/__db.[0-9][0-9]*
	 rpm --quiet -qa
	 rpm --rebuilddb
	 yum clean all
	 294.install mysql on centos:
	 sudo yum localinstall https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
	 sudo yum install mysql-community-server
	 sudo systemctl enable mysqld
	 sudo systemctl start mysqld
	 sudo systemctl status mysqld
	 sudo grep 'temporary password' /var/log/mysqld.log
	 sudo mysql_secure_installation
	 Aa123456!
	 mysql -u root -p
	 CREATE USER 'cq'@'%' IDENTIFIED BY 'Cq@Passw0rd';
	 GRANT ALL PRIVILEGES ON *.* TO 'cq'@'%' WITH GRANT OPTION;
	 mysql -u cq -h 1.15.90.81 -p
	 295.set lower_case_table_names = 1 (to make table_name case insensitive)
	 vim /etc/my.cnf
	 [mysqld]
	 lower_case_table_names = 1
	 systemctl restart mysqld
	 296.linux查看服务器 8000 端口的占用情况：
	 lsof -i:8000
	 或者：
	 netstat -tunlp | grep 端口号
	 297.windows安装telnet,在cmd中输入：
	 dism /Online /Enable-feature /FeatureName:TelnetClient
	 298.退出telnet. 退出telnet的命令:ctrl+]，然后再输入q就可以退出了
	 299.linux查看端口被哪个进程占用的方法
	 lsof -i:端口号
	 kill -9 pid
	 300.oracle：select replace(replace(value,chr(9),''),chr(10),'') from dual;
	 Chr(9)	HT	Horizontal Tab（tab键的两个空格）
	 Chr(10)	LF	Line Feed(换行符)
	 Chr(13) Carriage Return(回车)
	 Chr(32) Space(空白) ...
	 301.mysql 多行拼接成一行：
	 SELECT person_id,GROUP_CONCAT(hobbies SEPARATOR ', ') FROM peoples_hobbies
	 GROUP BY person_id;
	 302.git取消commit; HEAD^的意思是上一个版本
	 git reset --soft HEAD^
	 303.windows删除mysql服务：
	 sc delete mysql
	 304.window10开启录屏 快捷键：  win+alt+r
	 305.js保留2位小数并四舍五入：Math.round(number * 100) / 100
	 306.新建一个react项目：
	 npx create-react-app my-app
	 cd my-app
	 npm start
	 新建一个react项目并使用typescript：
	 npx create-react-app my-app --template typescript
307. spring-data-jpa
	 @Transient
	 TLine line; // 临时存储用，不存入数据库
308. centos查询文件夹大小： du -sh /path
 查看当前目录下各文件、文件夹的大小： du -h --max-depth=1
309. less转换成css
	 npm install -g less
	 lessc style.less style.css
310. git增加ssh认证：
	C:\Users\HP\.ssh\id_rsa.pub
311. nacos在windows下单机启动
 ./startup.cmd -m standalone
312. 测试git地址：
 git ls-remote https://github.com/chengqun2/chess.git
313. postgresql递归查询，查询parent_id = 3045 及所有子列表
 WITH RECURSIVE subordinates AS (
 SELECT
 menu_id,
 menu_name,
 parent_id,
 PATH,
 order_num
 FROM
 sys_menu
 WHERE
 parent_id = 3045 UNION
 SELECT
 e.menu_id,
 e.menu_name,
 e.parent_id,
 e.PATH,
 e.order_num
 FROM
 sys_menu e
 INNER JOIN subordinates s ON s.menu_id = e.parent_id
 ) SELECT
*
FROM
	subordinates 
ORDER BY
	parent_id,
	order_num	
314.lambda获取列表的对象中最小的parentId
private int getParentId(List<SysMenu> menus) {
if (null!=menus && !menus.isEmpty() && menus.size()>0){
SysMenu min = menus.stream().min(Comparator.comparing(SysMenu::getParentId)).get();
return min.getParentId().intValue();
}else{
return 0;
}
}
315.windows安装rocketmq
1).配置环境变量：ROCKETMQ_HOME： F:\soft\rocketmq-all-4.9.4-bin-release\bin
2).启动 NameServer   （启动%ROCKETMQ_HOME%/bin/mqnamesrv.cmd ;  修改%ROCKETMQ_HOME%/bin/runserver.cmd中的内存：set "JAVA_OPT=%JAVA_OPT% -server -Xms256m -Xmx512m"）
3).启动 Broker （在call之前增加 set "NAMESRV_ADDR=localhost:9876"，双击mqbroker.cmd脚本启动Broker）
cd F:\soft\rocketmq-all-4.9.4-bin-release\bin
启动 NameServer:  F:\soft\rocketmq-all-4.9.4-bin-release\bin>start mqnamesrv.cmd
启动 Broker:  F:\soft\rocketmq-all-4.9.4-bin-release\bin>mqbroker.cmd -c ../conf/broker.conf
docker安装rocketmq-console：
docker run -e "JAVA_OPTS=-Drocketmq.namesrv.addr=127.0.0.1:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false" -p 8090:8090 -t styletang/rocketmq-console-ng
316.根据某个属性去掉对象数组中的某个对象
this.userOptions = this.userOptions.filter(function( obj ) {
return obj.userId !== response.data.userId;
});
317.Windows环境RocketMQ broker启动失败闪退: 清空 C:\Users\HP\store ，再次启动。
318.Linux搜索历史命令history：
history | grep -w 'docker run'
319.nacos本地安装：
1).配置application.properties中的mysql连接
2).mysql导入nacos_config数据库
320.yarn install 报错; node-sass镜像源进行设置成国内的:
yarn config set sass-binary-site http://npm.taobao.org/mirrors/node-sass
321.Vue判断字符串A中是否包含某字符串B
<span v-if="scope.row.hjdxz.includes(scope.row.hjdxzqhhz)">
{{scope.row.hjdxz}}
</span>
<span v-else>
{{scope.row.hjdxzqhhz +scope.row.hjdjdhz + scope.row.hjdxz}}
</span>

324.maven install
install the package into the local repository, for use as a dependency in other projects locally		
325.java正则替换所有非数字为空：
"00a122c34d5eee6s7892as3".replaceAll("[^0-9]","");  返回00122345678923
326.java8 Convert List<Map> to Comma-Separated String
String mlphxxs = userBulidList.stream().map(x->x.get("mlphbm").toString())
.collect(Collectors.joining(","));
327.java8 分页查询
list = list.stream().skip(( pageNum - 1) * pageSize).limit(pageSize).collect(Collectors.toList());
328.pom文件打包：
<build>
<plugins>
<!-- 打包 -->
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-jar-plugin</artifactId>
<configuration>
<outputDirectory>${basedir}/../../app-run/${project.build.finalName}/${project.build.finalName}/</outputDirectory>
</configuration>
</plugin>
</plugins>
</build>
329.COPY ./ruoyi-modules-system (source目录) /ruoyi-modules-system(目标目录)
330.win10修改git用户名和邮箱  
//修改本目录下仓库的用户名
git config user.name "用户名"
git config user.email "邮箱"
//修改全局仓库下用户名和邮箱
git config --global user.email   "391323163@qq.com"
git config --global user.name  "qun.cheng"
git config --global --list
331.手机微信小程序怎么打开调试工具：
进入小程序，点击右上角三个点的按钮，在页面底部看到【开发调试】按钮，点击此按钮
可以看到【打开调试】按钮，点击此按钮，会退出小程序
重新进小程序可以看到右下角多了个绿色按钮
点击绿色按钮，就能看到请求信息、返回信息
332.maven项目置灰pom.xml文件，pom.xml中右击选择 maven->ignore projects 或者unignore projects
333.maven项目新建子模块，右击项目，new->module->next->parent
334.若依使用小结：
1)、配置F:\soft\nacos-server-2.0.2\nacos\conf\application.properties 中的mysql数据源
2)、启动nacos之后，在 http://127.0.0.1:8848/nacos  配置管理-配置列表
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
	1)、双击 idea->maven->ruoyi(root)->package 打包	 
	2)、java -Dfile.encoding=utf-8 -jar ruoyi-gateway.jar   (cmd中运行,设置encoding修复启动报错malformed)
	   java -Dfile.encoding=utf-8 -jar ruoyi-auth.jar 	
	   java -Dfile.encoding=utf-8 -jar ruoyi-modules-system.jar   
	   java -Dfile.encoding=utf-8 -jar wayz-beiwaitan.jar  
	3)、前端打包部署(npm run build:prod)：
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
		taskkill /T /F /PID 29608
335.ps -ef | grep nacos		
336.Map<String, List<Map>> userMap = list.stream().collect(Collectors.groupingBy(pcs -> pcs.get("pcs").toString()));
for (Map.Entry<String, List<Map>> entry : userMap.entrySet())
{
int addCount=0, updateCount=0, deleteCount=0, totalCount=0;
String jzdpcshz = "", manageCreateBy = "";
for (Map map : entry.getValue()) {
if(CpacPersonGatherDataStateEnum.status2.getCode().equals(map.get("data_state"))){
addCount = Integer.valueOf(map.get("num").toString());
}
else if(CpacPersonGatherDataStateEnum.status0.getCode().equals(map.get("data_state"))){
updateCount = Integer.valueOf(map.get("num").toString());
}else{
deleteCount = Integer.valueOf(map.get("num").toString());
}
totalCount = addCount + updateCount + deleteCount;
jzdpcshz = map.get("jzdpcshz").toString();
manageCreateBy = map.get("manage_create_by").toString();
}
CpacUserGatherStatisticsDto cpacUserGatherStatisticsDto = new CpacUserGatherStatisticsDto(DateUtils.convertDateToStr(cpacPersonGatherPolice.getBeginUpdateTime())+"-"+DateUtils.convertDateToStr(cpacPersonGatherPolice.getEndUpdateTime()), jzdpcshz, manageCreateBy, addCount, updateCount, deleteCount, totalCount);
list2.add(cpacUserGatherStatisticsDto);
}
337.Mybatis
<choose>
<when test="addressTypeStr != null and addressTypeStr != '' and addressTypeStr.contains('4'.toString())">
and (FIND_IN_SET(c.address_type,#{addressTypeStr}) or c.address_type is null)
</when>
<otherwise>
<if test="addressTypeStr != null and addressTypeStr != ''">
and FIND_IN_SET(c.address_type,#{addressTypeStr})
</if>
</otherwise>
</choose>
338.Mysql多表联合更新（通过关联表进行数据更新）
UPDATE cpac_person_gather_police_check1 t
INNER JOIN (
SELECT
rid,
create_date,
data_state,
operator_id,
operator
FROM
cpac_person_gather_update a
WHERE
1 = 1
AND create_date IN ( SELECT min( create_date ) FROM cpac_person_gather_update b WHERE a.rid = b.rid )) t2 ON t.rid = t2.rid
SET t.gather_create_by = t2.operator,
t.gather_create_by_id = t2.operator_id
339.com.baomidou.dynamic.datasource.exception.CannotFindDataSourceException: dynamic-datasource can not find primary datasource
检查是否读取到了nacos配置文件，或者nacos配置文件格式有错误
340.Mysql查询返回行号rownum
SELECT @rn:=@rn+1 AS rownum,rid,xm
FROM (
SELECT rid,xm
FROM cpac_person_gather_police_check6
) t1, (SELECT @rn:=0) t2;
341.docker run -d --restart=always -p 15003:15003 docker.newayz.com/shaoxing-shangyu/wayz-rf-shaoxing-shangyu:1.0.7
342.ElasticSearch 9200和9300端口的作用
9300是TCP协议端口号，ES集群之间通讯端口号
9200端口号，暴露ES RESTful接口端口号. uris: 127.0.0.1:9200
343.访问swagger右上角服务列表没有展示新增服务，
确认是否在ruoyi-gateway-dev.yml配置了对应服务的路由。
spring:
cloud:
gateway:
routes:
# xxxx服务
- id: ruoyi-xxxx
uri: lb://ruoyi-xxxx
predicates:
- Path=/xxxx/**
filters:
- StripPrefix=1
344.获取本机外部ip地址： curl ifconfig.me
345.portainer(默认9000端口)手动部署docker镜像：
1).images: pull the image
2).services: Change container image -> Apply changes
346.Java多线程(CompletableFuture)：
supplyAsync 执行CompletableFuture任务，支持返回值
runAsync 执行CompletableFuture任务，没有返回值。
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
347.idea补全等号左边：ctrl+alt+v
348.hutool工具类发送网络请求:
<dependency>
<groupId>cn.hutool</groupId>
<artifactId>hutool-all</artifactId>
<version>5.7.18</version>
</dependency>
String url = "https://xxx/xx";//指定URL
Map<String, Object> map = new HashMap<>();//存放参数
map.put("A", 100);
map.put("B", 200);
HashMap<String, String> headers = new HashMap<>();//存放请求头，可以存放多个请求头
headers.put("xxx", xxx);
//发送get请求并接收响应数据
String result= HttpUtil.createGet(url).addHeaders(headers).form(map).execute().body();
//发送post请求并接收响应数据
String result= HttpUtil.createPost(url).addHeaders(headers).form(map).execute().body();
349.docker 进入容器，测试接口
docker exec -it 95c7dbb20239fafd bash
curl --location --request GET 'http://127.0.0.1:15005/lgi/point?oid=330681'
docker logs 95c7dbb20239fafd
docker stop 95c7dbb20239fafd
350.class not found ,先clean试下.
351.springboot配置数据源，需要验证查询(validation-query)
spring:
datasource:
druid:
validation-query: SELECT 1
352.lombok日志添加  
@Slf4j
public class LogExample{}
will generate:
public class LogExample{
private static final org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(LogExample.class);
}
353.idea: Command line is too long. Shorten command line for:
Edit configurations ->Shorten command line: JAR manifest
354.Type “cmd” into the box and then press Ctrl+Shift+Enter to run the command as an administrator.
355.安装chocolatey(Windows下的软件包管理器)
1. 点击“开始”菜单搜索找到 Windows PowerShell ISE并以管理员身份运行
2. Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
355.chocolatey安装rabbitmq:
RabbitMQ是一款使用Erlang语言开发的，所以安装rabbitmq之前需要先安装erlang(通用的面向并发的编程语言)
choco install rabbitmq -y
安装web管理界面插件：
C:\Program Files\RabbitMQ Server\rabbitmq_server-3.11.16\sbin>rabbitmq-plugins enable rabbitmq_management
http://localhost:15672/    guest  guest
355.chocolatey安装make(a build automation tool):
choco install make -y
356.https://github.com/apitable 项目本地运行：
1).In the APITable directory, open the three command lines of git bash (在目录中右击选择 Git Bash Here)
2).first run make dataenv and make install to install the environment,
3).after ensuring that these two commands are running normally, execute make run in the three command lines in turn, select 1, 2, 3.
357.maven项目打包，正常情况下，scope=system的dependency是不会打进包中的，
<dependency>
<groupId>com.oracle</groupId>
<artifactId>ojdbc8</artifactId>
<version>8.0</version>
<scope>system</scope>
<systemPath>${project.basedir}/libs/ojdbc8.jar</systemPath>
</dependency>
此时如果需要将jar包打输出到lib中，需添加配 includeSystemScope=true
<plugin>
<configuration>
<includeSystemScope>true</includeSystemScope>
</configuration>
</plugin>
358.oracle递归查询上级.(下级 code = parent_code 即可)
SELECT code,parent_code,name
FROM sys_dept
START WITH code = '2'
CONNECT BY PRIOR parent_code = code 	
362.windows本机安装Linux系统(Ubuntu等)
1).wsl --install -d Ubuntu
Virtual hard disk files must be uncompressed and unencrypted and must not be sparse.
2).fsutil behavior set disableencryption 1
3).fsutil behavior set disablecompression 1
4).重启机器
5).修改文件夹属性->去掉压缩内容复选框 C:\Users\HP\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc
6).设置本机linux系统用户密码：chengqun    123456
363.cmd print current date: %date%
364.docker安装Jenkins:
1).docker network create jenkins
2).docker run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind --storage-driver overlay2
3).Create a Dockerfile with the following content:
FROM jenkins/jenkins:2.401.2-jdk17
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker0.-archive-keyring.asc \
https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
https://download.docker.com/linux/debian \
$(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
4).docker build -t myjenkins-blueocean:2.401.2-1 .
5).docker run --name jenkins-blueocean --restart=on-failure --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.401.2-1
365.docker安装elasticsearch 和 kibana:
1). docker network create elastic
2). docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.12
3). docker run --name es-node01 --net elastic -p 9200:9200 -p 9300:9300 -t docker.elastic.co/elasticsearch/elasticsearch:7.17.12
4). docker logs es-node01
1). docker pull docker.elastic.co/kibana/kibana:8.3.3
2). docker run --name kib-01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.3.3
3). docker logs kib-01
浏览器打开kibana：http://127.0.0.1:5601/app/home#/
366.docker安装elasticsearch，出现The vm.max_map_count kernel setting must be set to at least 262144 错误：
wsl -d docker-desktop -u root
sysctl -w vm.max_map_count=262144
367.Java集合去重
list.stream().distinct().collect(Collectors.toList());
368.docker查看网络列表、某个网络详情
docker network ls
docker network inspect 网络名称
369.oracle计算两个日期(date类型)之间相差的小时、分钟
round(to_number(end_time - start_time) * 24)
round(to_number(end_time - start_time) * 24 * 60)
370.centos启动mysql:
service mysql start
371.windows10启动elasticsearch:
F:\soft\elasticsearch\elasticsearch-7.10.1-windows-x86_64\elasticsearch-7.10.1\bin
双击 elasticsearch.bat
372.centos离线安装elasticsearch(rpm包的方式):
1).rpm -i elasticsearch-7.8.0-x86_64.rpm
2).sudo systemctl daemon-reload
3).sudo systemctl enable elasticsearch.service
4).sudo systemctl start elasticsearch.service
5).systemctl status elasticsearch.service
6).tail -f /var/log/elasticsearch/elasticsearch.log
7).vi /etc/elasticsearch/elasticsearch.yml
8).systemctl restart elasticsearch.service
9).firewall-cmd --zone=public --add-port=9200/tcp --permanent
10).firewall-cmd --reload
373.kibana示例：
GET wayz-es-test/_search
{}

	GET wayz-es-test/_doc/1
	{}

	POST wayz-es-test/_doc/1
	{
	 "id" : "1",
		"mlphbm" : "310006610000110000000000020000",
		"mlphxx" : "上海市浦东新区北西街11弄1号",
		"jddm" : "15012",
		"jdmc" : "张江木街道",
		"jcwdm" : "15016040",
		"jcwmc" : "由由八村居委",
		"qdm" : "310115",
		"qmc" : "上海市浦东新区",
		"pcsdm" : "310115760000",
		"pcsmc" : "张江派出所"
	}
	
	GET wayz-es-test/_search
	{
	  "query" : {
		"query_string" : {
		  "query" : "张江派出所",
		  "default_field": "pcsmc"
		}
	  }
	}	
374.Mysql表锁住：
1).show full processlist;
2).kill id
375.Redis设置key的过期时间，存放短信验证码，防止频繁获取.
@GetMapping("send-sms-for-login")
@ResponseBody
public R<?> sendMessageCode(@RequestParam("phone") String phone) {
// redis 缓存验证码 防止同一个手机号在倒计时内多次发送验证码请求
String cacheKey = UserConstants.SMS_CODE_CACHE_KEY_PREFIX + phone;
String redisCode = redisTemplate.opsForValue().get(cacheKey);
if (org.apache.commons.lang3.StringUtils.isNotBlank(redisCode)) {
long time = Long.parseLong(redisCode.split("_")[1]);
if (System.currentTimeMillis() - time < 60000) {
return R.fail("短信验证频繁获取");
}
}
String code = StringUtils.getSmsCodeStr();
redisTemplate.opsForValue().set(cacheKey, code + "_" + System.currentTimeMillis(), 10, TimeUnit.MINUTES);
smsComponent.sendSmsCode(phone, code);
return R.ok();
}
376.Linux查看已启用的端口列表：
netstat -lntup
377.防火墙 firewall
firewall-cmd --state 	
firewall-cmd --list-ports
firewall-cmd --zone=public --add-port=3690/tcp --permanent
378.防火墙 iptables
iptables -L -n
iptables -A INPUT -p tcp --dport 3690 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 3690 -j ACCEPT
379.CentOS7系统中安装jdk,选择JDK1.8版本进行安装：
yum install java-1.8.0-openjdk
默认安装完只有运行环境，也就说 java 安装目录下只有 jre 文件夹，我们执行 javac 命令会提示“未找到命令”,所以接下来需要安装jdk
yum install java-1.8.0-openjdk-devel.x86_64
380.centos启动svn服务
svnserve -d -r /usr/svn/ --listen-port 3690
381.Linux配置环境变量：
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.382.b05-1.el7_9.x86_64
382.TCP协议发送数据的步骤：
1)、创建客户端的Socket对象: Socket s = new Socket("10.2.120.65",10000);
2)、获取输出流，写数据
3)、释放资源
TCP协议接收数据的步骤：
1)、创建服务器端的Socket对象(ServerSocket): ServerSocket ss = new ServerSocket(10000);
2)、获取数据流，读数据，并把数据显示在控制台
3)、释放资源
383.解决bug：Task java.util.concurrent.FutureTask@1b71049 rejected from java.util.concurrent.ThreadPoolExecutor@d9fdff[Running, pool size = 10, active threads = 10, queued tasks = 0, completed tasks = 2058]
@Configuration
class TaskPoolConfig {
@Bean
public Executor taskExecutor1() {
ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
executor.setCorePoolSize(100);
executor.setMaxPoolSize(100);
executor.setQueueCapacity(100);
executor.setKeepAliveSeconds(60);
executor.setThreadNamePrefix("executor-1-");
return executor;
}
}
384.@ConfigurationProperties(prefix = "minio")
读取yml文件中minio的配置
385.ElasticSearch	Java API:
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
386.linux查看某个文件夹大小
sudo du -hc --max-depth=0 /yd21
387.nginx映射文件夹路径
location /duty {
alias  F:\source\duty-vue3\dist;
}
388.github解决代码下载及提交不了的问题(代理问题 
   fatal: unable to access 'https://github.com/chengqun2/chengqun2.github.io.git/': 
   Failed to connect to 127.0.0.1 port 18080 after 2087 ms: Couldn't connect to server)：
   1.git config --global --list
   2.chrome://net-export/       (监控浏览器，拿到proxy)
   3.git config --global http.proxy http://username:password@127.0.0.1:18080
     或者 git config --global http.proxy http://chengqun2:Ww88459526@127.0.0.1:7890
389.It looks like you're trying to use TypeScript but do not have the required package(s) installed.
    Please install @types/react by running: npm install --save-dev @types/react@17.0.2
	使用 `yarn add -D @types/react@17.0.2` 手动添加依赖。
390.vscode格式化vue代码：Shift+Alt+F
391.idea插件(sql打印时直接拼接好参数)： mybatis-log-plugin-free
392. du -h --max-depth=1 /path/to/directory
393. truncate -s 0 filename
394. 数据库分区策略： 范围分区(Range Partitioning)
	CREATE TABLE sales (
    sale_id INT,
    sale_date int
	)
	PARTITION BY RANGE (sale_date) (
		PARTITION p0 VALUES LESS THAN (2020),
		PARTITION p1 VALUES LESS THAN (2021),
		PARTITION p2 VALUES LESS THAN (2022),
		PARTITION p3 VALUES LESS THAN (2023),
		PARTITION p4 VALUES LESS THAN MAXVALUE
	);
395. Vue3 setup(){
		const name = ref('Bob')
		const age = ref(30)
		return {
			name,
			age
		}
	}
396. spring boot 获取某个类中的值：
	@Value("#{T(com.example.YourClass).YOUR_STATIC_FIELD}")	
397.pki generate trust-store-file
	1、我电脑生成 jks:
	keytool -genkeypair -alias your_alias -keyalg RSA -keysize 2048 -keystore your_keystore.jks -validity 365
	2、根据jks生成 csr:
	keytool -import -alias your_alias -keystore your_keystore.jks -file your_signed_certificate.crt
	3、csr发送请求，得到一个签名证书 
	4、将步骤3得到的签名证书导入步骤1生成的key中：
	   keytool -import -keystore your_keystore.jks -file your_signed_certificate.cer -alias cq	
	5、使用key进行https数字证书登录  
	6、查看key: keytool -list -v -keystore your_keystore.jks
398. 非root用户配置环境变量： 
    sudo vim /etc/profile
	export JAVA_HOME=/home/user_name/java/jdk-18.0.1.1
	export PATH=${JAVA_HOME}/bin:$PATH
   
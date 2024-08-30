### 1. 利用 to_number
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
      /

### 2. 利用 regexp_like
CREATE OR REPLACE FUNCTION isnumeric (str IN VARCHAR2)
    RETURN NUMBER
IS
BEGIN
    IF str IS NULL
    THEN
       RETURN 0;
    ELSE
       IF regexp_like (str, '^(-{0,1}+{0,1})[0-9]+(.{0,1}[0-9]+)$')
       THEN
          RETURN 1;
       ELSE
          RETURN 0;
       END IF;
    END IF;
END isnumeric;
/

### 3. 利用 translate
      CREATE OR REPLACE FUNCTION isnumeric (str IN VARCHAR2)
         RETURN NUMBER
      IS
         v_str VARCHAR2 (1000);
      BEGIN
         IF str IS NULL
         THEN
            RETURN 0;
         ELSE
         v_str := translate(str, '.0123456789', '.');

         IF v_str = '.' OR v_str = '+.' OR v_str = '-.' OR v_str IS NULL
         THEN
            RETURN 1;
         ELSE
            RETURN 0;
         END IF;
      END IF;
      END isnumeric;
      /

### 4. 数据库创建定时任务：
	1).创建存储过程，例：
	create procedure t_update_data()
	BEGIN
	update bug.`data` set assignUser = 'admin' where assignUser = 'null';
	END
	2).创建事件（navicat事件） call t_update_data()，添加到计划中
   
### 5. 更新某一张表的某字段等于另一张表的某字段
	UPDATE uin_target a
	INNER JOIN uin_user b ON a.create_name = b.USERNAME
	SET a.nick_name = b.NICKNAME
	WHERE
	a.create_name = b.USERNAME

### 数据库恢复：rman
RMAN（Recovery Manager）是随Oracle服务器软件一同安装的工具软件，它可以用来备份和恢复数据库文件、归档日志和控制文件，用来执行完全或不完全的数据库恢复。

### 数据库容灾方案：Oracle ADG
Oracle ADG 是一种数据库容灾方案，指的是多个数据库可以拥有相同的数据，一旦某个数据库发生故障，可快速切换到另一个数据库。同时也可以实现读写分离，主库写入，从库读取等等。

### 数据库双活复制: GoldenGate
GoldenGate软件是做Oracle数据库双活复制的   

### 数据同步/灾难性恢复：Data guard
Data guard是ORACLE 推出的一种高可用性 (HIGH AVAILABLE)的数据库方案,在8i之前称之为standby database，从9i开始，正式更名为Data guard，它是在主节点与备用节点间通过日志同步来保证数据的同步，可以实现快速切换与灾难性恢复

### 数据库性能管理解决方案：MaxGauge
MaxGauge主要用于数据库性能监测（支持 Oracle、DB2、MySQL、PostgreSQL、MongoDB）

### RAC
Oracle Real Application Clusters (RAC) 支持您跨多个服务器运行单一 Oracle Database，访问共享存储，充分提高可用性和水平可扩展性。 连接至 Oracle RAC 实例后，您无需修改应用，用户会话即可执行故障切换，安全重播中断期间的变更请求，最终用户完全不会感知到中断。

### 判断字符串中是否包含某个字符串，返回值大于0即存在
`INSTR(string, substring [, start_position [, nth_appearance]])`
string: The string to search within.
substring: The substring to search for.
start_position: Optional. This specifies the position in the string to start the search. If omitted, the default is 1 (beginning of the string).
nth_appearance: Optional. This specifies which occurrence of the substring to find. If omitted, the default is 1 (first occurrence).
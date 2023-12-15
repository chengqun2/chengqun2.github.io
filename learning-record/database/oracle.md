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
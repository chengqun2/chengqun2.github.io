### group_concat
```
SELECT
t1.*, group_concat(t2.team_name)
FROM
uin_service_mobile_seat t1
LEFT JOIN uin_company_team t2 ON FIND_IN_SET(t2.id, t1.group_ids)
GROUP BY
t1.id
```

### mysql 多表更新:
```
UPDATE crm_customer t11
INNER JOIN (
SELECT
sum(t2.order_amt) order_amt,
t2.customer_id customer_id
FROM
scm_order t2
GROUP BY
t2.customer_id
) b ON t11.id = b.customer_id
SET t11.amt = b.order_amt
```

### Mysql 行号 rownum
```
SELECT @rowno:=@rowno+1 AS rownum, id, score FROM table_name, (SELECT @rowno:=0) AS t
ORDER BY score DESC;
```

### mysql8  with as
```
with t1 as 
(SELECT * from person),
t2 as 
(SELECT * from course)
SELECT t1.*, t2.* from t1 join t2 on t1.id = t2.person_id;
```


### docker install mysql
```
docker run --name mysql9 -p 8082:3306 --restart always -e TZ=Asia/Shanghai -e MYSQL_ROOT_PASSWORD=jsfr123456 -e MYSQL_ROOT_HOST=%   -v /etc/docker/test-mysql:/etc/mysql/conf.d -v final-mysql-data:/var/lib/mysql -d mysql:latest 
```
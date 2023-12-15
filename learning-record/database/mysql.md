### group_concat
   SELECT
	t1.*, group_concat(t2.team_name)
	FROM
	uin_service_mobile_seat t1
	LEFT JOIN uin_company_team t2 ON FIND_IN_SET(t2.id, t1.group_ids)
	GROUP BY
	t1.id
### mysql多表更新:
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
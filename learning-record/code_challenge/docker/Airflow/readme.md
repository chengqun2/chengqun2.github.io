## Airflow：是一个强大的开源工作流编排平台，主要用于以编程方式定义、调度和监控工作流，侧重于任务的调度和依赖管理，通常用于构建复杂的多步骤数据工作流，包括 ETL 等数据处理流程。


### init the airflow and start the docker-compose
```
docker-compose up airflow-init
docker-compose up -d
```

### shut-down the docker-compose
```
docker-compose down
```

### shut-down the docker-compose and remove the volumes
```
docker-compose down -v
```


### open web browser 
http://localhost:8080/
Username and password: airflow   airflow

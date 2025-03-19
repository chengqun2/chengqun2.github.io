### 构建镜像
`docker build -t chengqun/example:1.0.1 .`

### 允许该容器最多使用200MB的内存和100MB 的swap。
`docker run -m 200M --memory-swap=300M chengqun/example:1.0.1`

### docker常用命令
```
docker images
docker rmi image_id
docker stop [OPTIONS] CONTAINER [CONTAINER...]
docker start [OPTIONS] CONTAINER [CONTAINER...]
docker restart [OPTIONS] CONTAINER [CONTAINER...]
docker kill [OPTIONS] CONTAINER [CONTAINER...]
docker rm [OPTIONS] CONTAINER [CONTAINER...]
docker logs [OPTIONS] CONTAINER
docker logs CONTAINER_NAME | tail -n 100
```

### docker 拷贝互联网镜像 -> 导入内网服务器
```
docker build -t chengqun/example:1.0.1 .
docker save -o D:\desktop/chengqun-example-1.0.1.tar   chengqun/example:1.0.1
//D:\desktop下的镜像文件上传服务器后：
docker load -i /usr/local/software/chengqun-example-1.0.1.tar
```


### 进入容器: 
`docker exec -it container_id sh`
`exit`


### docker install mysql：
```
docker images
docker pull mysql:5.7.35
docker run -d -p 3306:3306 --restart always -e TZ=Asia/Shanghai -v mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_ROOT_HOST=% -d mysql:5.7.35 --lower_case_table_names=1
netstat -na|grep 3306
sudo iptables -A INPUT -p tcp --dport 3306 -j ACCEPT
docker ps
```

###  Configure Docker to use a mirror registry: vim /etc/docker/daemon.json
```
{
  "registry-mirrors": [
    "https://docker.m.daocloud.io"
  ]
}

sudo systemctl restart docker
sudo systemctl status docker
docker info
```


### 启动容器，关闭后自动删除容器，测试容器启动过程中是否有报错
#### -t（分配伪终端）
#### --rm（自动删除容器）
```
docker run -it --rm --name n8n -p 8083:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```
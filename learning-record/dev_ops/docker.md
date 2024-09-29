### 构建镜像
`docker build -t chengqun/example:1.0.1 .`

### 允许该容器最多使用200MB的内存和100MB 的swap。
`docker run -m 200M --memory-swap=300M chengqun/example:1.0.1`

### docker常用命令
docker images
docker rmi image_id
docker stop [OPTIONS] CONTAINER [CONTAINER...]
docker start [OPTIONS] CONTAINER [CONTAINER...]
docker restart [OPTIONS] CONTAINER [CONTAINER...]
docker kill [OPTIONS] CONTAINER [CONTAINER...]
docker rm [OPTIONS] CONTAINER [CONTAINER...]
docker logs [OPTIONS] CONTAINER
docker logs CONTAINER_NAME | tail -n 100


### docker 拷贝互联网镜像 -> 导入内网服务器
`docker save -o 镜像压缩文件.tar   服务器镜像文件`
`docker load -i 镜像压缩文件.tar`


### 进入容器: 
`docker exec -it container_id sh`
`exit`

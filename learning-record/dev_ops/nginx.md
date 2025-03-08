### nginx部署，可以访问首页，但是不能直接访问其他路径
页面访问：
location / {
    root   html;
    index  index.html index.htm;
    try_files $uri $uri/ /index.html;
}
接口访问：
location /api/ {
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header REMOTE-HOST $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://localhost:8080/;
}

### 负载均衡
1、项目停止时，先注释掉nginx.conf的一个server，reload nginx
2、kill 掉项目进程
3、nohup 启动项目，curl 测试是否启动成功
4、项目启动成功后，reload nginx


### 测试nginx.conf配置是否正确，并且reload nginx
```
nginx -t
nginx -s reload	
```

### nginx 配置文件下载路径 vim nginx.conf
```
location /download/ {
    alias /data/download/;
}
```

### docker 安装nginx, 挂载出配置文件及前端页面目录

```
docker pull nginx
docker run --name my-nginx -p 8081:80 -v /software/nginx-config:/etc/nginx/conf.d -v /software/dify_api:/software/dify_api -d nginx
```

### 配置nginx /software/nginx-config/default.conf
```
server {
    listen 80;
    server_name localhost;

    location / {
        root /software/dify_api;
        index index.html index.htm;
    }

    location /api{
        rewrite ^/api(.*)$ /$1 break;
        proxy_pass http://server_ip_adress:8088;  # Your React dev server
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /test {
        return 200 "Hello from Nginx!";
    }
}
```
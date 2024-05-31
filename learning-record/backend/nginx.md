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
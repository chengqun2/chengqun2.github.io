### nginx部署，可以访问首页，但是不能直接访问其他路径
location / {
    root   html;
    index  index.html index.htm;
    try_files $uri $uri/ /index.html;
}

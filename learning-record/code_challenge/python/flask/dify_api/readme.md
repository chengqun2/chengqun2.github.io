### build docker image
```
docker build -t dify-api:1.0.0 .
docker save -o D:\desktop/dify-api-1.0.0.tar  dify-api:1.0.0
//镜像文件上传服务器后：
docker load -i /software/chat-project/backend/dify-api-1.0.0.tar
```

### 使用setuptools打包为Python包，并使用gunicorn运行
```
1. 本机环境准备（项目打包）：
python setup.py sdist bdist_wheel
生成： dify_api-1.0.0-py3-none-any.whl 上传到服务器

2. 项目关闭
./stop.sh

3. 安装上传的whl文件：
pip install dify_api-1.0.0-py3-none-any.whl --force-reinstall 

4. 项目启动
./start.sh

5. 服务器环境准备:
pip install gunicorn

6.使用 WSGI 服务器（如 Gunicorn）来运行 Flask 应用
nohup gunicorn -w 4 -t 180 -b 0.0.0.0:8081 dify_api.app:app > dify_api.log 2>&1 &
```

### start.sh
```
nohup gunicorn -w 4 -b 0.0.0.0:8081 dify_api.app:app > dify_api.log 2>&1 &
```

### stop.sh 
```
ps -ef|grep dify_api|grep -v grep|awk '{print $2}'|xargs kill -9;
```
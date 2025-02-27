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
生成： dify_api-1.0.0-py3-none-any.whl

2.服务器环境准备:
pip install gunicorn

3.本机打包的后缀为whl的文件上传到服务器后：
pip install dify_api-1.0.0-py3-none-any.whl

4.使用 WSGI 服务器（如 Gunicorn）来运行 Flask 应用
nohup gunicorn -w 4 -b 0.0.0.0:8081 dify_api.app:app > dify_api.log 2>&1 &
```

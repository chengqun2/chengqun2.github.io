# 使用 Python 基础镜像
FROM python:3.12

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Flask 应用运行的端口
EXPOSE 8080

# 定义容器启动时执行的命令
CMD ["python", "app.py"]
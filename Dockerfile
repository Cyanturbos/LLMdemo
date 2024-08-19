# 使用官方的 Python 3.11 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装 Python 依赖
RUN pip install --no-cache-dir chainlit openai

# 暴露端口 8080，Google Cloud Run 使用这个端口
EXPOSE 8080

# 启动应用
CMD ["chainlit", "run", "main.py", "--host", "0.0.0.0", "--port", "8080"]


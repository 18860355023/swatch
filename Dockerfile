# 使用官方 Python 运行时作为父镜像
FROM python:3.9-slim

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录内容复制到容器的 /app 中
ADD . /app

# 创建 pip 配置文件目录
RUN mkdir -p /root/.pip

# 创建 pip 配置文件，设置镜像源
RUN echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > /root/.pip/pip.conf

#升级PIP
RUN pip install --upgrade pip --no-cache-dir --no-build-isolation

ENV PIP_NO_CACHE_DIR=false
ENV PIP_MAX_CONCURRENT_DOWNLOADS=1

# 安装任何需要的包
RUN pip install --no-cache-dir -r requirements.txt

# 使端口 80 可供此容器外的环境使用
EXPOSE 6003

# 定义环境变量
ENV NAME World

# 在容器启动时运行 Python 应用
CMD ["python", "main.py"]
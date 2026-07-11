# [Docker](https://www.runoob.com/docker/docker-tutorial.html)

## 0.简介

Docker 是一个**开源的容器化平台**，核心作用是：

> 把应用程序 + 所有依赖（代码、运行环境、库、配置）打包成一个轻量级、可移植的「容器」（Container），然后可以在任何支持 Docker 的机器上一致地运行。

**一句话总结**： “Build once, run anywhere”（一次构建，到处运行）

它解决了传统开发中最头疼的问题：**“在我电脑上明明能跑，到服务器就挂了”**。

### Docker Engine

Docker 的核心引擎。 真正负责创建、运行、管理容器的后台服务 + 命令行工具。 服务器和生产环境主要使用它。

### [Docker Desktop](https://www.docker.com/products/docker-desktop/)

官方开发的桌面应用程序（带图形界面）。 专为 Windows 和 macOS 开发者设计，一键安装后包含 Docker Engine、Compose、GUI 仪表盘等全套工具，本地开发最方便。

### Docker Compose

多容器编排工具。 通过一个 docker-compose.yml 文件，用一条命令就能同时启动、管理多个互相依赖的容器（比如前端 + 后端 + 数据库）。

### Docker Hub

官方的公共镜像仓库（类似 GitHub 的代码仓库）。 用来存储、分享、下载各种现成的 Docker 镜像（如 MySQL、Nginx、Python 等）。

## 1.创建容器

### 1.1.Docker 安装验证

```
# 1. 运行官方测试镜像（验证 Docker 是否正常）
docker run hello-world
```

### 1.2.构建项目镜像

```
# 1. 进入项目目录
cd F:\your_project\helloworld

# 2. 创建 Dockerfile（纯命令行方式）
@"
FROM python:3.11-slim
WORKDIR /app
COPY hello_world.py .
CMD ["python", "hello_world.py"]
"@ | Set-Content -Encoding utf8 Dockerfile

# 3. 构建镜像（最后的 . 很重要）
docker build -t my-hello-python .

# 4. 运行自己的镜像
docker run my-hello-python
```

### 1.3.结果验收

```
(base) PS F:\my-learning-repo\20260711\helloworld> @"
>> FROM python:3.11-slim
>> WORKDIR /app
>> COPY hello_world.py .
>> CMD ["python", "hello_world.py"]
>> "@ | Set-Content -Encoding utf8 Dockerfile
(base) PS F:\my-learning-repo\20260711\helloworld>

(base) PS F:\my-learning-repo\20260711\helloworld>docker build -t my-hello-world .
[+] Building 0.6s (8/8) FINISHED                                                                           docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                       0.0s
 => => transferring dockerfile: 131B                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                        0.3s
 => [internal] load .dockerignore                                                                                          0.0s
 => => transferring context: 2B                                                                                            0.0s
 => [1/3] FROM docker.io/library/python:3.11-slim@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3  0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3  0.0s
 => [internal] load build context                                                                                          0.0s
 => => transferring context: 19.06kB                                                                                       0.0s
 => CACHED [2/3] WORKDIR /app                                                                                              0.0s
 => [3/3] COPY hello_world.py .                                                                                            0.0s
 => exporting to image                                                                                                     0.2s
 => => exporting layers                                                                                                    0.1s
 => => exporting manifest sha256:95691f6283799adbb66d89b7be883906a6d8b1d4617334ca42535ffdbe93b0e1                          0.0s
 => => exporting config sha256:4c464b6c9fedf4eca72a9c5f33b117d1e92cf0d96b05a1eb460b089f4cf3099d                            0.0s
 => => exporting attestation manifest sha256:877d748aaab074b4733741f64267f2d7faa81fd6bd33919644be66667c54db50              0.0s
 => => exporting manifest list sha256:5d46c5f99bb535df1954496db8ee1869479104f8254adb7412e2db39d33ecf90                     0.0s
 => => naming to docker.io/library/my-hello-world:latest                                                                   0.0s
 => => unpacking to docker.io/library/my-hello-world:latest                                                                0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/zkodwskki7jqa3d7brjqtsj1x
(base) PS F:\my-learning-repo\20260711\helloworld> docker run my-hello-world

准备展示创意 Hello World ...

>> Hello World  

========================================
展示完成！
========================================


            ASCII 艺术版 Hello World
------------------------------------------------------------
  H   H  eee  l     l      ooo        W   W  ooo  rrrr  l         d
  H   H e   e l     l     o   o       W   W o   o r   r l         d
  HHHHH eeeee l     l     o   o       W W W o   o rrrr  l      dddd
  H   H e     l     l     o   o       WW WW o   o r  r  l     d   d
  H   H  eee  lllll lllll  ooo        W   W  ooo  r   r lllll  dddd
------------------------------------------------------------
```

## 附录

### 常用指令速查表

| 用途                      | 命令                          | 说明             |
| ------------------------- | ----------------------------- | ---------------- |
| **查看本地镜像**          | `docker images`               | 列出所有镜像     |
| **查看正在运行的容器**    | `docker ps`                   | 只显示运行中的   |
| **查看所有容器**          | `docker ps -a`                | 包括已停止的     |
| **运行容器**              | `docker run 镜像名`           | 最基础运行       |
| **后台运行容器**          | `docker run -d 镜像名`        | 加 `-d` 后台运行 |
| **删除已停止的容器**      | `docker container prune`      | 清理垃圾容器     |
| **删除镜像**              | `docker rmi 镜像名`           | 删除指定镜像     |
| **查看镜像/容器详细信息** | `docker inspect 名称`         | 高级查看         |
| **进入正在运行的容器**    | `docker exec -it 容器ID bash` | 进去调试         |
| **停止容器**              | `docker stop 容器ID`          | 停止运行中的容器 |
| **强制删除容器**          | `docker rm -f 容器ID`         | 强制删除         |
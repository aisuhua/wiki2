# Docker

## CheetSheet

```sh
# 查看进程信息
docker top <container_id>
```

## 安装

```
# 加当前用户加入 docker 组
sudo gpasswd -a $USER docker
```

## 国内源

```
$ sudo vim /etc/docker/daemon.json
{
  "registry-mirrors":[
    "https://hub-mirror.c.163.com",
    "https://registry.aliyuncs.com",
    "https://registry.docker-cn.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://qby02i3s.mirror.aliyuncs.com"
  ]
}
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

## 常见问题

执行 `sudo systemctl status docker` 后，提示 `Failed to start Docker Application Container Engine.`

```sh
# 查看报错信息
sudo dockerd 
```

## Ref

1. [How to set user and group in Docker Compose](https://blog.giovannidemizio.eu/2021/05/24/how-to-set-user-and-group-in-docker-compose/)

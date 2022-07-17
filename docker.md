# Docker

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

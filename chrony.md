# Chrony

时间服务

## 安装

```
sudo yum install chrony
```

## 客户端配置

作为客户端使用时，需将时间服务器地址添加到配置文件

```
$ sudo vim /etc/chrony.conf
pool time.aisuhua.com
$ sudo systemctl restart chrony 
```

查看正在使用哪些时间服务

```
chronyc sources -v
```

## 服务端配置

作为服务端使用时，给其他服务器提供时间服务。使用本机的系统时间时，配置如下：

```
server 127.0.0.1
local stratum 10
driftfile /var/lib/chrony/chrony.drift
rtcsync
makestep 1.0 3
cmdport 0
cmdallow 127/8
allow 0.0.0.0/0
```

使用外部的时间服务器时，将 `server` 行替换成如下所示

```
server time.aisuhua.com iburst
```

## Ref

1. https://github.com/cturra/docker-ntp/blob/main/assets/startup.sh
2. https://github.com/geoffh1977/docker-chrony/blob/master/files/start.sh
3. [Steps to configure Chrony as NTP Server & Client (CentOS/RHEL 8)](https://www.golinuxcloud.com/configure-chrony-ntp-server-client-force-sync/)

# Kylin

以 Kylin v10 为例进行说明，其他版本会特别标注。

## Network

修改 IP、DNS、网关等信息

```
$ sudo vim /etc/sysconfig/network-scripts/ifcfg-<interface>
IPADDR=22.145.31.100
GATEWAY=22.145.31.254
NETMASK=255.255.255.0
DNS1=114.114.114.114
DNS2=223.223.223.223
...
$ sudo systemctl restart NetworkManager
```

## Ref

暂无

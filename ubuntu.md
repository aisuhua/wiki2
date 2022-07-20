# Ubuntu

以 Ubuntu 20.04 为例进行说明，其他版本会特别标注。

## 网络

静态 IP

```
$ sudo vim /etc/netplan/00-installer-config.yaml
network:
  ethernets:
    ens33:
      dhcp4: false
      addresses: [192.168.3.19/24]
      gateway4: 192.168.3.1
      nameservers:
        addresses: [233.5.5.5, 114.114.114.114]
  version: 2
$ sudo netplan apply
```

## 软件源

PPA

```
sudo sed -i "s/http:\/\/ppa.launchpad.net/https:\/\/launchpad.proxy.ustclug.org/g" /etc/apt/sources.list.d/*.list
sudo apt update
```

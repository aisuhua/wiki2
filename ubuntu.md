# Ubuntu

以 Ubuntu 20.04 为例进行说明，其他版本会特别标注。

## 网络

配置 IP、网关、DNS 等信息

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

官方软件源

```
$ sudo vim /etc/apt/sources.list
deb http://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
## Not recommended
# deb http://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src http://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```

使用中国科技大学的代理地址加速访问 PPA

```
sudo sed -i "s/http:\/\/ppa.launchpad.net/https:\/\/launchpad.proxy.ustclug.org/g" /etc/apt/sources.list.d/*.list
sudo apt update
```

## 常见问题

XRDP 远程 Ubuntu 时，桌面菜单不一样

```
$ sudo vim /etc/xrdp/startwm.sh
export DESKTOP_SESSION=ubuntu
export GNOME_SHELL_SESSION_MODE=ubuntu
export XDG_CURRENT_DESKTOP=ubuntu:GNOME
$ sudo systemctl restart xrpd
```

vmware 443 端口占用

```
Go to menu Edit -> Preferences -> Shared VMs and click on "Disable Sharing".
```

## Ref

1. https://mirrors.ustc.edu.cn/repogen/
2. https://superuser.com/a/1655262
3. https://github.com/neutrinolabs/xrdp/issues/1723

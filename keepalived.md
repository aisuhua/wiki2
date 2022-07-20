# KeepAlived

使用 VIP 实现高可用

## 安装

```
sudo yum install keepalived
```

配置文件位置 `/etc/keepalived/keepalived.conf`

## 操作系统

所有节点服务器配置如下

```
vrrp_instance VI_1 {
    interface enp4s1
    state BACKUP
    virtual_router_id 51
    priority 100
    authentication {
        auth_type PASS
        auth_pass FGwBkQ2K
    }
    virtual_ipaddress {
        22.145.31.244/24;
    }
}
```

注意事项：

1. 为了避免节点恢复后 VIP 切换，需将 `state` 设置为 `BACKUP`，`priority` 设置为一样
2. `virtual_router_id` 所有节点要一致，值的范围是 0-255
3. `auth_pass` 要一样才能通讯

## 应用

以 Nginx 高可用为例

```
$ sudo vim /etc/keepalived/keepalived.conf
vrrp_script check_nginx {
    script "killall -0 nginx"
    interval 2
}

vrrp_instance VI_1 {
    interface enp4s1
    state BACKUP
    priority 100
    authentication {
        auth_type PASS
        auth_pass FGwBkQ2K
    }
    virtual_router_id 31
    virtual_ipaddress {
        22.145.31.245/24;
    }
    track_script {
        check_nginx
    }
}
```

## 容器

```
vrrp_script nginx_container {
    script "/usr/bin/docker exec nginx-nginx-1 killall -0 nginx"
    interval 2
}

vrrp_instance VI_1 {
    interface enp4s1
    state BACKUP
    virtual_router_id 41
    priority 100
    authentication {
        auth_type PASS
        auth_pass 9NQ5Sd9n
    }
    virtual_ipaddress {
        22.145.31.246/24
    }
    track_script {
        nginx_container
    }
}
```

## Ref

1. https://linux.die.net/man/5/keepalived.conf
2. https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/load_balancer_administration/ch-initial-setup-vsa
3. https://www.redhat.com/sysadmin/keepalived-basics

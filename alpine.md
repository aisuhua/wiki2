# Alpine

以 Alpine 3.16 为例进行说明，其他版本会特别标注。

## 软件源

使用清华大学的镜像源

```
sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
```

## 常见问题

运行 glang 二进制程序

```sh
apk add gcompat
```

- https://github.com/openshift/origin/issues/18942#issuecomment-907780179

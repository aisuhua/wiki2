# onlyoffice

## 安装

```
git clone git@github.com:ONLYOFFICE/Docker-CommunityServer.git --depth=1
cd Docker-CommunityServer
docker-compose -f docker-compose.workspace.yml up
```

## 使用

手工激活用户

```sh
# 修改数据库
docker exec -it onlyoffice-mysql-server bash
update core_user set activation_status=1 where username='suhua'

# 重启服务让其生效
docker exec -it onlyoffice-community-server bash
systemctl restart monoserve
```

加入中文字体

```sh
# 下载中文字体
git clone gitgit@github.com:funggtopp/onlyoffice-chinese-fonts.git --depth=1

# 将字体文件拷贝到自定义字体目录
cp -r onlyoffice-chinese-fonts/"fonts for oo6"/* /path/to/Docker-CommunityServer/document_fonts/

# 重新生成字体文件
docker exec onlyoffice-document-server documentserver-generate-allfonts.sh
```

## 参考文献

1. [Adding fonts to ONLYOFFICE Docs](https://helpcenter.onlyoffice.com/installation/docs-community-install-fonts-linux.aspx)
2. [onlyoffice-chinese-fonts](https://github.com/funggtopp/onlyoffice-chinese-fonts)
3. [Installing ONLYOFFICE Workspace using Docker Compose](https://helpcenter.onlyoffice.com/installation/workspace-install-docker-compose.aspx)

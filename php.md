# PHP

## Composer

腾讯云

```
sudo wget https://mirrors.cloud.tencent.com/composer/composer.phar
sudo mv composer.phar  /usr/local/bin/composer
sudo chmod a+x /usr/local/bin/composer
composer config -g repos.packagist composer https://mirrors.cloud.tencent.com/composer/
```

阿里云

```
sudo wget https://mirrors.aliyun.com/composer/composer.phar
sudo mv composer.phar  /usr/local/bin/composer
sudo chmod a+x /usr/local/bin/composer
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

## Install

```sh
# 查看 extension 版本
php --ri phalcon
```

## Ref

1. https://mirrors.cloud.tencent.com/help/composer.html
2. https://developer.aliyun.com/composer

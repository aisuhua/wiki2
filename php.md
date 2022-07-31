# PHP

## Composer

腾讯云

```
sudo wget https://mirrors.cloud.tencent.com/composer/composer.phar
mv composer.phar  /usr/local/bin/composer
chmod a+x /usr/local/bin/composer
composer config -g repos.packagist composer https://mirrors.cloud.tencent.com/composer/
```

阿里云

```
sudo wget https://mirrors.aliyun.com/composer/composer.phar
mv composer.phar  /usr/local/bin/composer
chmod a+x /usr/local/bin/composer
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
```

## Ref

1. https://mirrors.cloud.tencent.com/help/composer.html
2. https://developer.aliyun.com/composer

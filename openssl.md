# OpenSSL

使用笔记

## CheetSheet

```sh
# 查看证书内容
openssl x509 -noout -text -in rootCA.pem

# 检测证书 7 天后是否到期
openssl x509 -checkend $(( 24*3600*7 )) -noout -in rootCA.pem
```

## Ref

1. https://stackoverflow.com/questions/21297853/how-to-determine-ssl-cert-expiration-date-from-a-pem-encoded-certificate

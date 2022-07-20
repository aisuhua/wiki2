# CheetSheet

一些快速操作的脚本

## Namespace

```sh
# 删除一直处在 `Terminating` 的命名空间
kubectl get namespace "stucked-namespace" -o json \
  | tr -d "\n" | sed "s/\"finalizers\": \[[^]]\+\]/\"finalizers\": []/" \
  | kubectl replace --raw /api/v1/namespaces/stucked-namespace/finalize -f -
```

## Ref

1. https://stackoverflow.com/a/59667608

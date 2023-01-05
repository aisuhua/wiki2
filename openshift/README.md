# OpenShift

## 资源

1. https://mirror.openshift.com/pub/openshift-v4/
2. https://openshift-release.apps.ci.l2s4.p1.openshiftapps.com/
3. https://access.redhat.com/labs/ocpupgradegraph/update_path

## 技巧

制作启动盘

```sh
dd if=coreos.iso of=<dev/sdx> status=progress
```

## 参考文献

1. [设置 MCP 更新时最大不可用数](https://access.redhat.com/solutions/4669561)
2. [修改 Worker Pod Limit 值-1](https://docs.openshift.com/container-platform/4.8/post_installation_configuration/machine-configuration-tasks.html#create-a-containerruntimeconfig_post-install-machine-configuration-tasks)
3. [修改 Worker Pod Limit 值-2](https://access.redhat.com/solutions/5366631)
4. [ImagePrunerDegraded error stalling upgrade](https://access.redhat.com/solutions/5370391)

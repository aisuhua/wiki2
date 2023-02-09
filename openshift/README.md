# OpenShift

## 资源

1. https://mirror.openshift.com/pub/openshift-v4/
2. https://openshift-release.apps.ci.l2s4.p1.openshiftapps.com/
3. https://access.redhat.com/labs/ocpupgradegraph/update_path
4. https://openshift-release.apps.ci.l2s4.p1.openshiftapps.com/releasestream/4-stable/release/4.8.56?from=4.8.36

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
5. [How to update the PodDisruptionBudget and RollingUpdate of routers on OCP 4](https://access.redhat.com/solutions/6542021) （[参考1](https://github.com/openshift/cluster-ingress-operator/blob/cb614126da5151f1a115152ae1fc3ef70ee93ca1/pkg/operator/controller/ingress/poddisruptionbudget.go#L71-L74)）
6. [The node in a degraded state because of the use of a deleted machineconfig: machineconfig.machineconfiguration.openshift.io; rendered-$[custom-machine-config] not found in OpenShift 4.x](https://access.redhat.com/solutions/4970731)
7. [Specifying an alternative cluster domain using the appsDomain option](https://docs.openshift.com/container-platform/4.9/networking/ingress-operator.html#nw-ingress-configuring-application-domain_configuring-ingress)
8. [Modifying the template for new projects](https://docs.openshift.com/container-platform/4.7/applications/projects/configuring-project-creation.html#modifying-template-for-new-projects_configuring-project-creation)

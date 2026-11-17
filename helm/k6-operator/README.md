# k6-operator

A Helm chart to install the k6-operator

**Homepage:** <https://github.com/giantswarm/k6-operator-app>

## Source Code

* <https://github.com/giantswarm/k6-operator-app>
* <https://github.com/grafana/k6-operator/blob/main/charts/k6-operator>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://grafana.github.io/helm-charts | k6operator(k6-operator) | 4.7.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| k6operatorEnabled | bool | `false` |  |
| k6operator.customAnnotations | object | `{}` |  |
| k6operator.podAnnotations | object | `{}` |  |
| k6operator.customLabels | object | `{}` |  |
| k6operator.podLabels | object | `{}` |  |
| k6operator.affinity | object | `{}` |  |
| k6operator.tolerations | list | `[]` |  |
| k6operator.installCRDs | bool | `true` |  |
| k6operator.rbac.namespaced | bool | `false` |  |
| k6operator.namespace.create | bool | `false` |  |
| k6operator.metrics.serviceMonitor.enabled | bool | `true` |  |
| k6operator.metrics.serviceMonitor.namespace | string | `""` |  |
| k6operator.metrics.serviceMonitor.jobLabel | string | `""` |  |
| k6operator.metrics.serviceMonitor.interval | string | `""` |  |
| k6operator.metrics.serviceMonitor.scrapeTimeout | string | `""` |  |
| k6operator.metrics.serviceMonitor.relabelings | list | `[]` |  |
| k6operator.metrics.serviceMonitor.metricRelabelings | list | `[]` |  |
| k6operator.metrics.serviceMonitor.selector | object | `{}` |  |
| k6operator.metrics.serviceMonitor.labels | object | `{}` |  |
| k6operator.metrics.serviceMonitor.honorLabels | bool | `false` |  |
| k6operator.service.enabled | bool | `true` |  |
| k6operator.service.labels | object | `{}` |  |
| k6operator.service.annotations | object | `{}` |  |
| k6operator.service.portName | string | `"https"` |  |
| k6operator.manager.logging.development | bool | `true` |  |
| k6operator.manager.replicas | int | `1` |  |
| k6operator.manager.serviceAccount.name | string | `"k6-operator-controller"` |  |
| k6operator.manager.serviceAccount.create | bool | `true` |  |
| k6operator.manager.image.registry | string | `"gsoci.azurecr.io"` |  |
| k6operator.manager.image.repository | string | `"giantswarm/k6-operator"` |  |
| k6operator.manager.image.tag | string | `"controller-v1.4.0"` |  |
| k6operator.manager.image.pullPolicy | string | `"IfNotPresent"` |  |
| k6operator.manager.livenessProbe.httpGet.path | string | `"/healthz"` |  |
| k6operator.manager.livenessProbe.httpGet.port | int | `8081` |  |
| k6operator.manager.livenessProbe.initialDelaySeconds | int | `15` |  |
| k6operator.manager.livenessProbe.periodSeconds | int | `20` |  |
| k6operator.manager.readinessProbe.httpGet.path | string | `"/healthz"` |  |
| k6operator.manager.readinessProbe.httpGet.port | int | `8081` |  |
| k6operator.manager.readinessProbe.initialDelaySeconds | int | `5` |  |
| k6operator.manager.readinessProbe.periodSeconds | int | `10` |  |
| k6operator.manager.env | list | `[]` |  |
| k6operator.manager.envFrom | list | `[]` |  |
| k6operator.manager.resources.limits.cpu | string | `"100m"` |  |
| k6operator.manager.resources.limits.memory | string | `"100Mi"` |  |
| k6operator.manager.resources.requests.cpu | string | `"100m"` |  |
| k6operator.manager.resources.requests.memory | string | `"50Mi"` |  |
| k6operator.manager.containerSecurityContext.runAsNonRoot | bool | `true` |  |
| k6operator.manager.containerSecurityContext.runAsUser | int | `1000` |  |
| k6operator.manager.containerSecurityContext.runAsGroup | int | `1000` |  |
| k6operator.manager.containerSecurityContext.readOnlyRootFilesystem | bool | `true` |  |
| k6operator.manager.containerSecurityContext.allowPrivilegeEscalation | bool | `false` |  |
| k6operator.manager.containerSecurityContext.capabilities.drop[0] | string | `"ALL"` |  |
| k6operator.manager.containerSecurityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| k6operator.manager.podSecurityContext.fsGroup | int | `1000` |  |
| k6operator.manager.podSecurityContext.runAsGroup | int | `1000` |  |
| k6operator.manager.podSecurityContext.runAsNonRoot | bool | `true` |  |
| k6operator.manager.podSecurityContext.runAsUser | int | `1000` |  |
| k6operator.manager.podSecurityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |

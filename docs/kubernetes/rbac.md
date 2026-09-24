# Kubernetes RBAC

<span class="ol-search-aliases">kubectl auth can-i rbac roles rolebindings clusterrole clusterrolebinding permissions</span>

<div class="ol-section-kicker"><span>K8S</span><strong>RBAC</strong></div>

## List effective permissions
```bash
kubectl auth can-i --list
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, Permissions · **Context:** Cluster user · **Requires:** Kubernetes API access · **Noise:** Quiet

## Can create pods
```bash
kubectl auth can-i create pods -A
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, Pods · **Context:** Cluster user · **Requires:** Kubernetes API access · **Noise:** Quiet

## Can read secrets
```bash
kubectl auth can-i get secrets -A
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, Secrets · **Context:** Cluster user · **Requires:** Kubernetes API access · **Noise:** Quiet

## Can impersonate users
```bash
kubectl auth can-i impersonate users
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, Impersonation · **Context:** Cluster user · **Requires:** Kubernetes API access · **Noise:** Quiet

## Role bindings
```bash
kubectl get rolebindings -A -o wide
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, RoleBinding · **Context:** Cluster user · **Requires:** rolebindings list permission · **Noise:** Quiet

## Cluster role bindings
```bash
kubectl get clusterrolebindings -o wide
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, ClusterRoleBinding · **Context:** Cluster user · **Requires:** clusterrolebindings list permission · **Noise:** Quiet

## Bindings to cluster-admin
```bash
kubectl get clusterrolebindings -o json | jq -r '.items[] | select(.roleRef.name=="cluster-admin") | [.metadata.name,(.subjects//[]|map(.kind+":"+.name)|join(","))] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, cluster-admin · **Context:** Cluster user · **Requires:** clusterrolebindings list permission · **Noise:** Quiet

**Related:** [Service Accounts](service-accounts.md) · [Privilege Signals](privilege-signals.md) · [Secrets](secrets.md)

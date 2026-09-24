# Kubernetes Privilege Signals

<span class="ol-search-aliases">kubernetes privileged pod hostpath hostpid hostnetwork capabilities escape container breakout</span>

<div class="ol-section-kicker"><span>K8S</span><strong>Privilege signals</strong></div>

## Privileged containers
```bash
kubectl get pods -A -o json | jq -r '.items[] | .metadata.namespace as $n | .metadata.name as $p | .spec.containers[] | select(.securityContext.privileged==true) | [$n,$p,.name] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, Privileged Pod · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## hostPath mounts
```bash
kubectl get pods -A -o json | jq -r '.items[] | select(any(.spec.volumes[]?; has("hostPath"))) | [.metadata.namespace,.metadata.name,([.spec.volumes[]?|select(has("hostPath"))|.hostPath.path]|join(","))] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, hostPath · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Dangerous added capabilities
```bash
kubectl get pods -A -o json | jq -r '.items[] | .metadata.namespace as $n | .metadata.name as $p | .spec.containers[] | select((.securityContext.capabilities.add // []) | length > 0) | [$n,$p,.name,((.securityContext.capabilities.add//[])|join(","))] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, Capabilities · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Host namespace trio
```bash
kubectl get pods -A -o json | jq -r '.items[] | select(.spec.hostPID==true or .spec.hostNetwork==true or .spec.hostIPC==true) | [.metadata.namespace,.metadata.name,.spec.hostPID,.spec.hostNetwork,.spec.hostIPC] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, Host Namespace · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Pods running as root
```bash
kubectl get pods -A -o json | jq -r '.items[] | .metadata.namespace as $n | .metadata.name as $p | .spec.containers[] | select((.securityContext.runAsNonRoot // false)==false) | [$n,$p,.name,(.securityContext.runAsUser//"unspecified")] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, Root, SecurityContext · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Can create pods in all namespaces
```bash
kubectl auth can-i create pods -A
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, Pod Create · **Context:** Cluster user · **Requires:** Kubernetes API access · **Noise:** Quiet

## Can create privileged-supporting resources
```bash
for r in pods daemonsets deployments jobs cronjobs; do printf '%-12s ' "$r"; kubectl auth can-i create "$r" -A; done
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, RBAC, Workloads · **Context:** Cluster user · **Requires:** Kubernetes API access · **Noise:** Moderate


## Container runtime sockets from a pod shell
```bash
ls -l /var/run/docker.sock /run/containerd/containerd.sock /var/run/crio/crio.sock 2>/dev/null
```
**Tool:** ls · **Platform:** Linux container · **Tags:** Kubernetes, Runtime Socket, Escape Signal · **Context:** Pod shell · **Requires:** Filesystem access · **Noise:** Quiet

## Host-style mounts from a pod shell
```bash
findmnt 2>/dev/null | grep -Ei '/host|/var/lib/kubelet|/run/containerd|docker.sock'
```
**Tool:** findmnt · **Platform:** Linux container · **Tags:** Kubernetes, Mounts, Escape Signal · **Context:** Pod shell · **Requires:** findmnt available · **Noise:** Quiet

## Linux capabilities inside container
```bash
capsh --print 2>/dev/null | grep -E 'Current:|Bounding set'
```
**Tool:** capsh · **Platform:** Linux container · **Tags:** Kubernetes, Capabilities, Escape Signal · **Context:** Pod shell · **Requires:** capsh available · **Noise:** Quiet

## Device exposure inside container
```bash
ls -la /dev | grep -E 'kmsg|mem|sd[a-z]|nvme|mapper' || true
```
**Tool:** ls · **Platform:** Linux container · **Tags:** Kubernetes, Devices, Escape Signal · **Context:** Pod shell · **Requires:** Pod shell · **Noise:** Quiet

## Container cgroup context
```bash
cat /proc/1/cgroup
```
**Tool:** cat · **Platform:** Linux container · **Tags:** Kubernetes, Container Detection, cgroup · **Context:** Pod shell · **Requires:** /proc mounted · **Noise:** Quiet

**Related:** [RBAC](rbac.md) · [Workloads](workloads.md) · [Service Accounts](service-accounts.md)

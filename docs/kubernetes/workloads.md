# Kubernetes Workloads

<div class="ol-section-kicker"><span>K8S</span><strong>Workloads</strong></div>

## All pods
```bash
kubectl get pods -A -o wide
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Pods · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Images in use
```bash
kubectl get pods -A -o json | jq -r '.items[] | .metadata.namespace as $n | .metadata.name as $p | .spec.containers[] | [$n,$p,.name,.image] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, Images, Inventory · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Pods with host network
```bash
kubectl get pods -A -o json | jq -r '.items[] | select(.spec.hostNetwork==true) | [.metadata.namespace,.metadata.name] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, hostNetwork · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Pods with host PID
```bash
kubectl get pods -A -o json | jq -r '.items[] | select(.spec.hostPID==true) | [.metadata.namespace,.metadata.name] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, hostPID · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Pods with host IPC
```bash
kubectl get pods -A -o json | jq -r '.items[] | select(.spec.hostIPC==true) | [.metadata.namespace,.metadata.name] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, hostIPC · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Security contexts
```bash
kubectl get pods -A -o json | jq -r '.items[] | .metadata.namespace as $n | .metadata.name as $p | .spec.containers[] | [$n,$p,.name,(.securityContext//{})] | @json'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, SecurityContext · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

**Related:** [Privilege Signals](privilege-signals.md) · [Service Accounts](service-accounts.md) · [Network](network.md)

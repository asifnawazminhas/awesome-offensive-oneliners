# Kubernetes Secrets

<div class="ol-section-kicker"><span>K8S</span><strong>Secrets</strong></div>

## List secrets
```bash
kubectl get secrets -A
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Secrets · **Context:** Cluster user · **Requires:** secrets list permission · **Noise:** Quiet

## Secret keys without values
```bash
kubectl get secret <SECRET> -n <NAMESPACE> -o json | jq -r '.data | keys[]'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, Secrets, Keys · **Context:** Cluster user · **Requires:** secret get permission · **Noise:** Quiet

## Decode one field
```bash
kubectl get secret <SECRET> -n <NAMESPACE> -o jsonpath='{.data.<KEY>}' | base64 -d; echo
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Secrets, Decode · **Context:** Cluster user · **Requires:** secret get permission · **Noise:** Moderate

## Find TLS secrets
```bash
kubectl get secrets -A --field-selector type=kubernetes.io/tls
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, TLS, Secrets · **Context:** Cluster user · **Requires:** secrets list permission · **Noise:** Quiet

## Find Docker registry secrets
```bash
kubectl get secrets -A --field-selector type=kubernetes.io/dockerconfigjson
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Registry, Secrets · **Context:** Cluster user · **Requires:** secrets list permission · **Noise:** Quiet

**Related:** [Service Accounts](service-accounts.md) · [RBAC](rbac.md) · [Workloads](workloads.md)

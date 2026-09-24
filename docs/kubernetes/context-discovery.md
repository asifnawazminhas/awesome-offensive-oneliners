# Kubernetes Context Discovery

<span class="ol-search-aliases">k8s kubernetes kubectl current context cluster namespace api server</span>

<div class="ol-section-kicker"><span>K8S</span><strong>Context</strong></div>

## Current context
```bash
kubectl config current-context
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Context · **Context:** Cluster user · **Requires:** kubeconfig · **Noise:** Quiet

## All configured contexts
```bash
kubectl config get-contexts
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Contexts · **Context:** Local user · **Requires:** kubeconfig · **Noise:** Quiet

## Current namespace
```bash
kubectl config view --minify --output 'jsonpath={..namespace}{"\n"}'
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Namespace · **Context:** Cluster user · **Requires:** kubeconfig · **Noise:** Quiet

## API server
```bash
kubectl config view --minify --output 'jsonpath={.clusters[0].cluster.server}{"\n"}'
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, API Server · **Context:** Local user · **Requires:** kubeconfig · **Noise:** Quiet

## Namespaces
```bash
kubectl get namespaces
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Namespaces · **Context:** Cluster user · **Requires:** namespaces list permission · **Noise:** Quiet

## Nodes
```bash
kubectl get nodes -o wide
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Nodes · **Context:** Cluster user · **Requires:** nodes list permission · **Noise:** Quiet

**Related:** [RBAC](rbac.md) · [Workloads](workloads.md) · [Network](network.md)

# Kubernetes Network

<div class="ol-section-kicker"><span>K8S</span><strong>Network</strong></div>

## Services
```bash
kubectl get services -A -o wide
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Services · **Context:** Cluster user · **Requires:** services list permission · **Noise:** Quiet

## Ingresses
```bash
kubectl get ingress -A -o wide
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Ingress · **Context:** Cluster user · **Requires:** ingress list permission · **Noise:** Quiet

## Endpoints
```bash
kubectl get endpoints -A
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Endpoints · **Context:** Cluster user · **Requires:** endpoints list permission · **Noise:** Quiet

## Network policies
```bash
kubectl get networkpolicies -A
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, NetworkPolicy · **Context:** Cluster user · **Requires:** networkpolicies list permission · **Noise:** Quiet

## NodePorts
```bash
kubectl get svc -A -o json | jq -r '.items[] | select(.spec.type=="NodePort") | [.metadata.namespace,.metadata.name,([.spec.ports[].nodePort]|join(","))] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, NodePort · **Context:** Cluster user · **Requires:** services list permission · **Noise:** Quiet

## LoadBalancers
```bash
kubectl get svc -A -o json | jq -r '.items[] | select(.spec.type=="LoadBalancer") | [.metadata.namespace,.metadata.name,(.status.loadBalancer.ingress//[])] | @json'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, LoadBalancer · **Context:** Cluster user · **Requires:** services list permission · **Noise:** Quiet

**Related:** [Context Discovery](context-discovery.md) · [Workloads](workloads.md) · [Privilege Signals](privilege-signals.md)

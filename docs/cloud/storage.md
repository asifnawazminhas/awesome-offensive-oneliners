# Cloud Storage

<span class="ol-search-aliases">s3 bucket azure blob gcs storage public access policy anonymous cloud storage</span>

<div class="ol-section-kicker"><span>CLOUD</span><strong>Storage</strong></div>

## S3 list buckets
```bash
aws s3api list-buckets --query 'Buckets[].Name' --output table
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, S3, Inventory · **Context:** Authenticated cloud principal · **Requires:** s3:ListAllMyBuckets · **Noise:** Quiet

## S3 public-access block
```bash
aws s3api get-public-access-block --bucket <BUCKET>
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, S3, Public Access · **Context:** Authenticated cloud principal · **Requires:** s3:GetBucketPublicAccessBlock · **Noise:** Quiet

## S3 bucket policy
```bash
aws s3api get-bucket-policy --bucket <BUCKET> --query Policy --output text | jq .
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, S3, Policy · **Context:** Authenticated cloud principal · **Requires:** s3:GetBucketPolicy · **Noise:** Quiet

## Test anonymous S3 listing
```bash
curl -fsS 'https://<BUCKET>.s3.amazonaws.com/?list-type=2&max-keys=5'
```
**Tool:** curl · **Platform:** Cross-platform · **Tags:** AWS, S3, Anonymous · **Context:** No auth · **Requires:** Network access · **Noise:** Quiet

## Azure storage accounts
```bash
az storage account list --query '[].{Name:name,ResourceGroup:resourceGroup,PublicNetworkAccess:publicNetworkAccess}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Storage, Inventory · **Context:** Authenticated cloud principal · **Requires:** Subscription read access · **Noise:** Quiet

## Azure blob anonymous listing probe
```bash
curl -fsS 'https://<ACCOUNT>.blob.core.windows.net/<CONTAINER>?restype=container&comp=list'
```
**Tool:** curl · **Platform:** Cross-platform · **Tags:** Azure, Blob, Anonymous · **Context:** No auth · **Requires:** Network access · **Noise:** Quiet

## GCS bucket list
```bash
gcloud storage buckets list --project <PROJECT_ID>
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, GCS, Inventory · **Context:** Authenticated cloud principal · **Requires:** storage.buckets.list · **Noise:** Quiet

## Test public GCS object listing
```bash
curl -fsS 'https://storage.googleapis.com/storage/v1/b/<BUCKET>/o?maxResults=5'
```
**Tool:** curl · **Platform:** Cross-platform · **Tags:** GCP, GCS, Anonymous · **Context:** No auth · **Requires:** Network access · **Noise:** Quiet


## S3 controlled write canary
```bash
printf 'authorized-test\n' >/tmp/ol-canary.txt && aws s3 cp /tmp/ol-canary.txt s3://<BUCKET>/ol-canary.txt
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, S3, Write Test · **Context:** Authenticated cloud principal · **Requires:** s3:PutObject and explicit scope · **Noise:** Moderate · **Version:** AWS CLI v2 syntax

## Azure Blob controlled write canary
```bash
az storage blob upload --account-name <ACCOUNT> --container-name <CONTAINER> --name ol-canary.txt --file <FILE> --auth-mode login
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Blob, Write Test · **Context:** Authenticated cloud principal · **Requires:** Blob data write permission and explicit scope · **Noise:** Moderate · **Version:** Azure CLI current syntax

## GCS controlled write canary
```bash
gcloud storage cp <FILE> gs://<BUCKET>/ol-canary.txt
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, GCS, Write Test · **Context:** Authenticated cloud principal · **Requires:** storage.objects.create and explicit scope · **Noise:** Moderate · **Version:** gcloud current syntax

**Related:** [AWS IAM](aws-iam.md) · [Azure Identity](azure-identity.md) · [GCP IAM](gcp-iam.md)

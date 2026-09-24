# Cloud Inventory

Fast inventory one-liners for identifying what the current principal can see.

<div class="ol-section-kicker"><span>CLOUD</span><strong>Inventory</strong></div>

## AWS regions
```bash
aws ec2 describe-regions --query 'Regions[].RegionName' --output text
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, Regions · **Context:** Authenticated cloud principal · **Requires:** AWS credentials · **Noise:** Quiet

## AWS EC2 instances
```bash
aws ec2 describe-instances --query 'Reservations[].Instances[].{Id:InstanceId,PrivateIp:PrivateIpAddress,PublicIp:PublicIpAddress,Profile:IamInstanceProfile.Arn}' --output table
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, EC2, Inventory · **Context:** Authenticated cloud principal · **Requires:** ec2:DescribeInstances · **Noise:** Quiet

## Azure resources
```bash
az resource list --query '[].{Name:name,Type:type,Group:resourceGroup,Location:location}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Inventory · **Context:** Authenticated cloud principal · **Requires:** Subscription read access · **Noise:** Moderate

## Azure VMs
```bash
az vm list -d --query '[].{Name:name,ResourceGroup:resourceGroup,PrivateIps:privateIps,PublicIps:publicIps}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, VM, Inventory · **Context:** Authenticated cloud principal · **Requires:** VM read access · **Noise:** Moderate

## GCP projects
```bash
gcloud projects list --format='table(projectId,name,lifecycleState)'
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, Projects · **Context:** Authenticated cloud principal · **Requires:** Project visibility · **Noise:** Quiet

## GCP compute instances
```bash
gcloud compute instances list --project <PROJECT_ID>
```
**Tool:** gcloud · **Platform:** Cross-platform · **Tags:** GCP, Compute, Inventory · **Context:** Authenticated cloud principal · **Requires:** compute.instances.list · **Noise:** Moderate

**Related:** [AWS IAM](aws-iam.md) · [Azure Identity](azure-identity.md) · [GCP IAM](gcp-iam.md)

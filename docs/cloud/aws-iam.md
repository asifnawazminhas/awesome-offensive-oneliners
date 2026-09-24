# AWS IAM

<span class="ol-search-aliases">aws iam enumerate permissions privilege escalation simulate-principal-policy caller identity policies roles</span>

<div class="ol-section-kicker"><span>AWS</span><strong>IAM</strong></div>

## Current caller
```bash
aws sts get-caller-identity
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Identity · **Context:** Authenticated cloud principal · **Requires:** AWS credentials · **Noise:** Quiet · **Version:** AWS CLI v2 syntax

## List users
```bash
aws iam list-users --query 'Users[].{User:UserName,Arn:Arn}' --output table
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Users · **Context:** Authenticated cloud principal · **Requires:** iam:ListUsers · **Noise:** Quiet · **Version:** AWS CLI v2 syntax

## List roles
```bash
aws iam list-roles --query 'Roles[].{Role:RoleName,Arn:Arn}' --output table
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Roles · **Context:** Authenticated cloud principal · **Requires:** iam:ListRoles · **Noise:** Quiet · **Version:** AWS CLI v2 syntax

## Attached user policies
```bash
aws iam list-attached-user-policies --user-name <USER>
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Policies · **Context:** Authenticated cloud principal · **Requires:** iam:ListAttachedUserPolicies · **Noise:** Quiet · **Version:** AWS CLI v2 syntax

## Inline user policies
```bash
aws iam list-user-policies --user-name <USER>
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Inline Policy · **Context:** Authenticated cloud principal · **Requires:** iam:ListUserPolicies · **Noise:** Quiet · **Version:** AWS CLI v2 syntax

## Role trust policy
```bash
aws iam get-role --role-name <ROLE> --query 'Role.AssumeRolePolicyDocument'
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Trust Policy · **Context:** Authenticated cloud principal · **Requires:** iam:GetRole · **Noise:** Quiet · **Version:** AWS CLI v2 syntax

## Simulate sensitive actions
```bash
aws iam simulate-principal-policy --policy-source-arn <PRINCIPAL_ARN> --action-names iam:PassRole sts:AssumeRole s3:GetObject secretsmanager:GetSecretValue
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Effective Permissions · **Context:** Authenticated cloud principal · **Requires:** iam:SimulatePrincipalPolicy · **Noise:** Moderate · **Version:** AWS CLI v2 syntax

## Account authorization details
```bash
aws iam get-account-authorization-details --filter User Role Group LocalManagedPolicy
```
**Tool:** AWS CLI · **Platform:** Cross-platform · **Tags:** AWS, IAM, Inventory · **Context:** Authenticated cloud principal · **Requires:** iam:GetAccountAuthorizationDetails · **Noise:** Moderate · **Version:** AWS CLI v2 syntax

**Related:** [Cloud Storage](storage.md) · [Metadata Services](metadata.md) · [Cloud Inventory](inventory.md)

# Azure Identity

<span class="ol-search-aliases">azure entra az ad role assignment tenant subscription managed identity</span>

<div class="ol-section-kicker"><span>AZ</span><strong>Identity</strong></div>

## Current account
```bash
az account show --query '{tenant:tenantId,subscription:id,user:user.name}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Identity, Subscription · **Context:** Authenticated cloud principal · **Requires:** Azure CLI login · **Noise:** Quiet · **Version:** Azure CLI current syntax

## List subscriptions
```bash
az account list --query '[].{Name:name,Subscription:id,Tenant:tenantId,State:state}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Subscriptions · **Context:** Authenticated cloud principal · **Requires:** Azure CLI login · **Noise:** Quiet · **Version:** Azure CLI current syntax

## Signed-in Entra user
```bash
az ad signed-in-user show --query '{displayName:displayName,userPrincipalName:userPrincipalName,id:id}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Entra ID, User · **Context:** Authenticated user · **Requires:** Microsoft Graph access · **Noise:** Quiet · **Version:** Azure CLI current syntax

## Role assignments for current user
```bash
az role assignment list --assignee "$(az ad signed-in-user show --query id -o tsv)" --all -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, RBAC, Roles · **Context:** Authenticated user · **Requires:** Role assignment read access · **Noise:** Quiet · **Version:** Azure CLI current syntax

## List service principals
```bash
az ad sp list --all --query '[].{Name:displayName,AppId:appId,Id:id}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Entra ID, Service Principal · **Context:** Authenticated cloud principal · **Requires:** Directory read access · **Noise:** Moderate · **Version:** Azure CLI current syntax

## Managed identities
```bash
az identity list --query '[].{Name:name,PrincipalId:principalId,ClientId:clientId,ResourceGroup:resourceGroup}' -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, Managed Identity · **Context:** Authenticated cloud principal · **Requires:** Subscription read access · **Noise:** Quiet · **Version:** Azure CLI current syntax

## Role assignments at subscription scope
```bash
az role assignment list --scope /subscriptions/<SUBSCRIPTION_ID> --all -o table
```
**Tool:** Azure CLI · **Platform:** Cross-platform · **Tags:** Azure, RBAC, Subscription · **Context:** Authenticated cloud principal · **Requires:** Role assignment read access · **Noise:** Moderate · **Version:** Azure CLI current syntax

**Related:** [Cloud Storage](storage.md) · [Metadata Services](metadata.md) · [Cloud Inventory](inventory.md)

# Start Here

Use the site as a fast reference, or follow one of these compact paths if you are still building familiarity.

<div class="ol-section-kicker"><span>START</span><strong>Suggested paths</strong></div>

## Foundation

1. [Recon](recon/) - domains, DNS, HTTP probing and ports.
2. [Web](web/) - VHosts, content, parameters, auth and APIs.
3. [Windows](windows/) and [Linux](linux/) - host enumeration and privilege checks.

## Active Directory

1. [Domain Discovery](active-directory/domain-discovery.md)
2. [Users & Groups](active-directory/users-groups.md)
3. [Kerberos](active-directory/kerberos.md)
4. [Delegation](active-directory/delegation.md)
5. [BloodHound](active-directory/bloodhound.md)

## Cloud and Kubernetes

1. [Cloud Overview](cloud/)
2. [AWS IAM](cloud/aws-iam.md), [Azure Identity](cloud/azure-identity.md), [GCP IAM](cloud/gcp-iam.md)
3. [Kubernetes RBAC](kubernetes/rbac.md)
4. [Service Accounts](kubernetes/service-accounts.md)
5. [Privilege Signals](kubernetes/privilege-signals.md)

## Operator workflow

1. Find the task.
2. Check **Context**, **Requires** and **Noise** where present.
3. Replace placeholders such as `<TARGET>`, `<DOMAIN>` and `<USER>`.
4. Validate the command against the installed tool version with `--help` or `--version` when syntax may drift.

**Related:** [Conventions](conventions.md) · [Tools](tools/) · [Changelog](changelog.md)

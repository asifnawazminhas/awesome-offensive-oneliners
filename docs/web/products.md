---
hide:
  - toc
---

# Popular software fingerprints

Fast local checks for widely deployed software and frameworks.

<div class="ol-section-kicker"><span>WEB</span></div>

## WordPress fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'wp-content|wp-includes|wp-json|wordpress' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** WordPress · **Context:** No auth


## WordPress REST API check

```bash
curl -skI https://<TARGET>/wp-json/
```

**Tool:** curl · **Platform:** Cross-platform · **Context:** No auth


## Next.js fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio '__NEXT_DATA__|/_next/static/|/_next/image' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Next.js · **Context:** No auth


## Moodle fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'moodle|/theme/[^"/]+|/lib/javascript.php' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Moodle · **Context:** No auth


## Joomla fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'joomla|/media/system/js/|com_[A-Za-z0-9_]+' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Joomla · **Context:** No auth


## Drupal fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'drupal|sites/default|sites/all|drupalSettings' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Drupal · **Context:** No auth


## Laravel fingerprint headers

```bash
curl -skI https://<TARGET> | grep -Ei 'laravel|XSRF-TOKEN|laravel_session'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Laravel · **Context:** User


## Django fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'csrfmiddlewaretoken|django' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Django · **Context:** No auth


## Jenkins fingerprint

```bash
curl -skI https://<TARGET> | grep -Ei 'X-Jenkins|X-Hudson'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Jenkins · **Context:** No auth


## Grafana fingerprint

```bash
curl -sk https://<TARGET>/login | grep -Ei 'grafana|public/build' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Grafana · **Context:** No auth


## GitLab fingerprint

```bash
curl -skI https://<TARGET> | grep -Ei 'gitlab|_gitlab_session'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** GitLab · **Context:** User


## Kibana fingerprint

```bash
curl -skI https://<TARGET> | grep -Ei 'kbn-name|kibana'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Kibana · **Context:** No auth


## Tomcat fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'Apache Tomcat|/manager/html' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Tomcat · **Context:** No auth


## Confluence fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'confluence|ajs-version-number|Atlassian' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Confluence · **Context:** No auth


## Jira fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'jira|ajs-version-number|Atlassian' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Jira · **Context:** No auth

## Keycloak fingerprint

```bash
curl -sk https://<TARGET>/ | grep -Ei 'keycloak|/realms/|account-console' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Keycloak · **Context:** No auth

## SonarQube fingerprint

```bash
curl -sk https://<TARGET>/api/system/status | jq .
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Tags:** SonarQube · **Context:** No auth

## Elasticsearch fingerprint

```bash
curl -sk https://<TARGET>/ | jq '.name,.cluster_name,.version.number'
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Tags:** Elasticsearch · **Context:** No auth

## Prometheus fingerprint

```bash
curl -sk https://<TARGET>/-/ready
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Prometheus · **Context:** No auth

## Nexus Repository fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'nexus|NX-ANTI-CSRF-TOKEN'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Nexus · **Context:** No auth

## JFrog Artifactory fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'artifactory|X-Artifactory'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Artifactory · **Context:** No auth

## VMware vCenter fingerprint

```bash
curl -sk https://<TARGET>/ | grep -Ei 'VMware|vSphere|vCenter' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** VMware, vCenter · **Context:** No auth

## Citrix Gateway fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'Citrix|NSC_|NetScaler'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Citrix, NetScaler · **Context:** No auth

## Fortinet fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'FortiGate|Fortinet|APSCOOKIE'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Fortinet · **Context:** User

## Palo Alto GlobalProtect fingerprint

```bash
curl -sk https://<TARGET>/global-protect/login.esp | grep -Ei 'GlobalProtect|Palo Alto' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Palo Alto, GlobalProtect · **Context:** No auth

## Microsoft Exchange OWA fingerprint

```bash
curl -skI https://<TARGET>/owa/ | grep -Ei 'X-OWA-Version|X-FEServer|OutlookSession'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Exchange, OWA · **Context:** User

## SharePoint fingerprint

```bash
curl -skI https://<TARGET>/_layouts/15/start.aspx | grep -Ei 'MicrosoftSharePointTeamServices|SPRequestGuid'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** SharePoint · **Context:** No auth

## Apache Airflow fingerprint

```bash
curl -sk https://<TARGET>/health | jq .
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Tags:** Airflow · **Context:** No auth

## RabbitMQ Management fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'RabbitMQ|X-Powered-By'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** RabbitMQ · **Context:** No auth

---

**Related:** [Overview](./) · [Path Traversal Lfi](path-traversal-lfi.md) · [Prototype Pollution](prototype-pollution.md)

# Popular software fingerprints

Fast local checks for widely deployed software and frameworks.

<div class="ol-section-kicker"><span>WEB</span></div>

## WordPress fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'wp-content|wp-includes|wp-json|wordpress' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** WordPress


## WordPress REST API check

```bash
curl -skI https://<TARGET>/wp-json/
```

**Tool:** curl · **Platform:** Cross-platform


## Next.js fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio '__NEXT_DATA__|/_next/static/|/_next/image' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Next.js


## Moodle fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'moodle|/theme/[^"/]+|/lib/javascript.php' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Moodle


## Joomla fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'joomla|/media/system/js/|com_[A-Za-z0-9_]+' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Joomla


## Drupal fingerprint

```bash
curl -sk https://<TARGET> | grep -Eio 'drupal|sites/default|sites/all|drupalSettings' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Drupal


## Laravel fingerprint headers

```bash
curl -skI https://<TARGET> | grep -Ei 'laravel|XSRF-TOKEN|laravel_session'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Laravel


## Django fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'csrfmiddlewaretoken|django' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Django


## Jenkins fingerprint

```bash
curl -skI https://<TARGET> | grep -Ei 'X-Jenkins|X-Hudson'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Jenkins


## Grafana fingerprint

```bash
curl -sk https://<TARGET>/login | grep -Ei 'grafana|public/build' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Grafana


## GitLab fingerprint

```bash
curl -skI https://<TARGET> | grep -Ei 'gitlab|_gitlab_session'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** GitLab


## Kibana fingerprint

```bash
curl -skI https://<TARGET> | grep -Ei 'kbn-name|kibana'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Kibana


## Tomcat fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'Apache Tomcat|/manager/html' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Tomcat


## Confluence fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'confluence|ajs-version-number|Atlassian' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Confluence


## Jira fingerprint

```bash
curl -sk https://<TARGET> | grep -Ei 'jira|ajs-version-number|Atlassian' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Jira

## Keycloak fingerprint

```bash
curl -sk https://<TARGET>/ | grep -Ei 'keycloak|/realms/|account-console' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Keycloak

## SonarQube fingerprint

```bash
curl -sk https://<TARGET>/api/system/status | jq .
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Tags:** SonarQube

## Elasticsearch fingerprint

```bash
curl -sk https://<TARGET>/ | jq '.name,.cluster_name,.version.number'
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Tags:** Elasticsearch

## Prometheus fingerprint

```bash
curl -sk https://<TARGET>/-/ready
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Prometheus

## Nexus Repository fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'nexus|NX-ANTI-CSRF-TOKEN'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Nexus

## JFrog Artifactory fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'artifactory|X-Artifactory'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Artifactory

## VMware vCenter fingerprint

```bash
curl -sk https://<TARGET>/ | grep -Ei 'VMware|vSphere|vCenter' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** VMware, vCenter

## Citrix Gateway fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'Citrix|NSC_|NetScaler'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Citrix, NetScaler

## Fortinet fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'FortiGate|Fortinet|APSCOOKIE'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Fortinet

## Palo Alto GlobalProtect fingerprint

```bash
curl -sk https://<TARGET>/global-protect/login.esp | grep -Ei 'GlobalProtect|Palo Alto' | head
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Palo Alto, GlobalProtect

## Microsoft Exchange OWA fingerprint

```bash
curl -skI https://<TARGET>/owa/ | grep -Ei 'X-OWA-Version|X-FEServer|OutlookSession'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** Exchange, OWA

## SharePoint fingerprint

```bash
curl -skI https://<TARGET>/_layouts/15/start.aspx | grep -Ei 'MicrosoftSharePointTeamServices|SPRequestGuid'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** SharePoint

## Apache Airflow fingerprint

```bash
curl -sk https://<TARGET>/health | jq .
```

**Tool:** curl + jq · **Platform:** Cross-platform · **Tags:** Airflow

## RabbitMQ Management fingerprint

```bash
curl -skI https://<TARGET>/ | grep -Ei 'RabbitMQ|X-Powered-By'
```

**Tool:** curl · **Platform:** Cross-platform · **Tags:** RabbitMQ

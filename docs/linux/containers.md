# Docker & LXC Checks

One-liners for container-group membership, sockets, images and host-mount clues.

<div class="ol-section-kicker"><span>LNX</span><strong>6 one-liners</strong></div>

## Docker group membership

```bash
id | grep -E "docker|lxd|lxc"
```

**Tool:** id · **Platform:** Linux · **Tags:** Docker, LXC, groups · **Context:** User · **Noise:** Quiet

## Docker socket permissions

```bash
ls -l /var/run/docker.sock 2>/dev/null
```

**Tool:** ls · **Platform:** Linux · **Tags:** Docker, socket · **Context:** User · **Noise:** Quiet

## Docker info

```bash
docker info 2>/dev/null | head -40
```

**Tool:** Docker · **Platform:** Linux · **Tags:** Docker, environment · **Context:** User · **Noise:** Quiet

## Docker images

```bash
docker images 2>/dev/null
```

**Tool:** Docker · **Platform:** Linux · **Tags:** Docker, images · **Context:** User · **Noise:** Quiet

## LXD containers

```bash
lxc list 2>/dev/null
```

**Tool:** LXC · **Platform:** Linux · **Tags:** LXD, containers · **Context:** User · **Noise:** Quiet

## Container mounts

```bash
mount | grep -Ei "docker|overlay|lxc|container"
```

**Tool:** mount · **Platform:** Linux · **Tags:** containers, mounts · **Context:** User · **Noise:** Quiet

---

**Related:** Container Detection · Capabilities · NFS

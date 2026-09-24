# Container Detection

One-liners for determining whether the current Linux process is inside a container or namespace-isolated environment.

<div class="ol-section-kicker"><span>LNX</span><strong>5 one-liners</strong></div>

## Docker marker

```bash
test -f /.dockerenv && echo Docker
```

**Tool:** bash · **Platform:** Linux · **Tags:** Docker, detection · **Context:** User

## cgroup clues

```bash
cat /proc/1/cgroup | grep -Ei "docker|kubepods|containerd|lxc"
```

**Tool:** procfs · **Platform:** Linux · **Tags:** container, detection · **Context:** User

## PID 1 identity

```bash
ps -p 1 -o pid,comm,args
```

**Tool:** ps · **Platform:** Linux · **Tags:** container, process · **Context:** User

## Mount namespace clues

```bash
mount | grep -Ei "overlay|docker|containerd|kubepods"
```

**Tool:** mount · **Platform:** Linux · **Tags:** container, mounts · **Context:** User

## Kubernetes service account

```bash
ls -la /var/run/secrets/kubernetes.io/serviceaccount 2>/dev/null
```

**Tool:** ls · **Platform:** Linux · **Tags:** Kubernetes, detection · **Context:** User

---

**Related:** Docker & LXC · Environment · Capabilities

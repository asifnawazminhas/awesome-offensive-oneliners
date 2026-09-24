# NFS Checks

One-liners for exports, mount options and no_root_squash discovery.

<div class="ol-section-kicker"><span>LNX</span><strong>5 one-liners</strong></div>

## Local exports

```bash
cat /etc/exports 2>/dev/null
```

**Tool:** cat · **Platform:** Linux · **Tags:** NFS, exports · **Context:** User · **Noise:** Quiet

## Find no_root_squash

```bash
grep -RHi "no_root_squash" /etc/exports /etc/exports.d 2>/dev/null
```

**Tool:** grep · **Platform:** Linux · **Tags:** NFS, no_root_squash · **Context:** User · **Noise:** Quiet

## Remote exports

```bash
showmount -e <TARGET>
```

**Tool:** showmount · **Platform:** Linux · **Tags:** NFS, exports · **Context:** No auth · **Noise:** Quiet

## Nmap NFS scripts

```bash
nmap -Pn -p111,2049 --script nfs-showmount,nfs-ls <TARGET>
```

**Tool:** Nmap · **Platform:** Linux · **Tags:** NFS, RPC · **Context:** No auth · **Noise:** Quiet

## Mounted NFS filesystems

```bash
mount | grep -i nfs
```

**Tool:** mount · **Platform:** Linux · **Tags:** NFS, mounts · **Context:** User · **Noise:** Quiet

---

**Related:** Containers · Writable Services · Networking & Files

# Tunneling

Common pivoting and port-forwarding one-liners.

### Ligolo proxy

```bash
./proxy -selfcert -laddr 0.0.0.0:11601
```

**Tool:** Ligolo-ng · **Platform:** Linux · **Tags:** Tunneling, Pivoting

### Ligolo agent

```powershell
.\agent.exe -connect <SERVER>:11601 -ignore-cert
```

**Tool:** Ligolo-ng · **Platform:** Windows · **Tags:** Tunneling, Pivoting

### Chisel reverse server

```bash
chisel server --reverse --port 8000
```

**Tool:** Chisel · **Platform:** Linux · **Tags:** Tunneling, Reverse

### Chisel SOCKS client

```bash
chisel client <SERVER>:8000 R:socks
```

**Tool:** Chisel · **Platform:** Linux/Windows · **Tags:** Tunneling, SOCKS

### SSH dynamic SOCKS

```bash
ssh -N -D 1080 <USER>@<HOST>
```

**Tool:** OpenSSH · **Platform:** Linux/macOS · **Tags:** SSH, SOCKS

### SSH local forward

```bash
ssh -N -L 127.0.0.1:<LOCAL_PORT>:<INTERNAL_HOST>:<REMOTE_PORT> <USER>@<JUMP_HOST>
```

**Tool:** OpenSSH · **Platform:** Linux/macOS · **Tags:** SSH, Port Forward


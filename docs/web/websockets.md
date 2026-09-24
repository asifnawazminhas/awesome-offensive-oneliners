# WebSocket Discovery

One-liners for finding WebSocket endpoints and probing upgrade behavior.

<div class="ol-section-kicker"><span>WEB</span><strong>5 one-liners</strong></div>

## Find ws/wss URLs in JavaScript

```bash
grep -RIEo "wss?://[^"' ]+" <JS_DIR> | sort -u
```

**Tool:** grep · **Platform:** Linux · **Tags:** Web, WebSockets, JavaScript · **Context:** User

## Search crawled URLs for WebSockets

```bash
grep -Ei "(^|/)ws($|/)|websocket|socket.io" urls.txt | sort -u
```

**Tool:** grep · **Platform:** Linux · **Tags:** Web, WebSockets · **Context:** User

## Manual upgrade probe

```bash
curl -sk --http1.1 -i -H "Connection: Upgrade" -H "Upgrade: websocket" -H "Sec-WebSocket-Version: 13" -H "Sec-WebSocket-Key: SGVsbG9Xb3JsZA==" https://<TARGET>/<WS_PATH>
```

**Tool:** curl · **Platform:** Any · **Tags:** Web, WebSockets, upgrade · **Context:** No auth

## websocat connect

```bash
websocat -v wss://<TARGET>/<WS_PATH>
```

**Tool:** websocat · **Platform:** Linux · **Tags:** Web, WebSockets · **Context:** No auth

## wscat connect

```bash
wscat -c wss://<TARGET>/<WS_PATH>
```

**Tool:** wscat · **Platform:** Any · **Tags:** Web, WebSockets · **Context:** No auth

---

**Related:** JavaScript · Authentication · APIs & GraphQL

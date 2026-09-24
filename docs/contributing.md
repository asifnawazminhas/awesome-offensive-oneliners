# Contributing

Contributions are welcome when they keep the project fast to scan, consistent and easy to use.

## Command conventions

Use predictable placeholders everywhere:

| Placeholder | Meaning |
| --- | --- |
| `<TARGET>` | Hostname, IP address or URL |
| `<CIDR>` | Network range |
| `<DOMAIN>` | Active Directory or DNS domain |
| `<USER>` | Username |
| `<PASSWORD>` | Password |
| `<HASH>` | Password or NTLM hash |
| `<DC>` / `<DC_IP>` | Domain controller / address |
| `<PORT>` | TCP or UDP port |
| `<FILE>` | Local or remote file path |

## Entry format

Use one task per entry:

````markdown
### Short action-oriented title

```bash
command --with <PLACEHOLDERS>
```

**Tool:** Tool name · **Platform:** Linux/Windows/macOS · **Tags:** Tag1, Tag2 · **Context:** No auth / User / Domain user / Local admin / SYSTEM · **Noise:** Quiet
````

## Rules

1. Keep the command on one logical line whenever practical.
2. Use the shared placeholders above.
3. Avoid organisation-specific hostnames, credentials or secrets.
4. Do not duplicate an existing command unless the variant materially changes the workflow.
5. Keep explanations short. This is a one-liner reference, not a full methodology guide.
6. Test the command before opening a pull request.
7. Run `mkdocs build --strict` before submitting changes.

## Local preview

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && mkdocs serve
```

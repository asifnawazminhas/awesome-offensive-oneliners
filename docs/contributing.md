# Contributing

Contributions are welcome when they keep the project fast to scan and easy to use.

## Entry format

Use one task per entry:

````markdown
### Short action-oriented title

```bash
command --with <PLACEHOLDERS>
```

**Tool:** Tool name · **Platform:** Linux/Windows/macOS · **Tags:** Tag1, Tag2
````

## Rules

1. Keep the command on one logical line whenever practical.
2. Use obvious placeholders such as `<TARGET>`, `<DOMAIN>`, `<USER>`, `<PASSWORD>` and `<HASH>`.
3. Avoid organisation-specific hostnames, credentials or secrets.
4. Do not duplicate an existing command unless the variant changes the technique or authentication method.
5. Keep explanations short. This is a one-liner reference, not a full methodology guide.
6. Test the command before opening a pull request.
7. Run `mkdocs build --strict` before submitting changes.

## Local preview

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && mkdocs serve
```

# ZenTao integration

The configured site is ZenTao 18.12 at `https://cd.houjiemeishi.com/` and uses PATH_INFO URLs.

## Environment

```text
ZENTAO_URL=https://cd.houjiemeishi.com/
ZENTAO_USERNAME=<account>
ZENTAO_PASSWORD=<password>
ZENTAO_INSECURE=0
```

The helper logs in through the same random-salt MD5 flow used by the ZenTao 18.12 web client, keeps cookies in memory, and reads a bug through the model API. Set `ZENTAO_INSECURE=1` only for a certificate problem that has been explicitly accepted.

## Commands

```text
python3 scripts/zentao_client.py get-bug 1287
python3 scripts/zentao_client.py raw /bug-view-1287.json
```

The helper is read-only. ZenTao comments and status changes must use an authenticated, inspected request matching the deployed version; do not guess write endpoints.

If the model endpoint changes, first inspect the authenticated response and update the helper. Never fall back to scraping a title while silently dropping steps, attachments, or history.

#!/usr/bin/env python3
"""Read-only ZenTao 18.x client. Credentials come only from environment variables."""

import argparse
import hashlib
import http.cookiejar
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request


class ZenTaoClient:
    def __init__(self):
        self.base = os.environ.get("ZENTAO_URL", "https://cd.houjiemeishi.com/").rstrip("/") + "/"
        self.username = os.environ.get("ZENTAO_USERNAME", "")
        self.password = os.environ.get("ZENTAO_PASSWORD", "")
        insecure = os.environ.get("ZENTAO_INSECURE", "0") == "1"
        context = ssl._create_unverified_context() if insecure else ssl.create_default_context()
        cookies = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(cookies),
            urllib.request.HTTPSHandler(context=context),
        )
        self.opener.addheaders = [("User-Agent", "Codex-ZenTao-Bug-Fix/1.0")]

    def request(self, path, data=None):
        url = urllib.parse.urljoin(self.base, path.lstrip("/"))
        encoded = urllib.parse.urlencode(data).encode("utf-8") if data is not None else None
        with self.opener.open(url, encoded, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")

    def login(self):
        if not self.username or not self.password:
            raise RuntimeError("Set ZENTAO_USERNAME and ZENTAO_PASSWORD environment variables")
        self.request("user-login-Lw==.html")
        random_text = self.request("user-refreshRandom.html").strip()
        first = hashlib.md5(self.password.encode("utf-8")).hexdigest()
        encrypted = hashlib.md5((first + random_text).encode("utf-8")).hexdigest()
        payload = {
            "account": self.username,
            "password": encrypted,
            "passwordStrength": "2",
            "referer": "/",
            "verifyRand": random_text,
            "keepLogin": "0",
            "captcha": "",
        }
        result = json.loads(self.request("user-login.html", payload))
        if result.get("result") == "fail":
            raise RuntimeError("ZenTao login failed: " + str(result.get("message", "unknown error")))

    def get_json(self, path):
        body = self.request(path)
        try:
            return json.loads(body)
        except json.JSONDecodeError as exc:
            raise RuntimeError("ZenTao returned non-JSON content; login or endpoint may have changed") from exc

    def get_bug(self, bug_id):
        return self.get_json(f"api-getModel-bug-getById-id={bug_id}.json")


def main():
    parser = argparse.ArgumentParser(description="Read ZenTao bug data without modifying ZenTao")
    sub = parser.add_subparsers(dest="command", required=True)
    get_bug = sub.add_parser("get-bug", help="Read a bug by numeric ID")
    get_bug.add_argument("bug_id", type=int)
    raw = sub.add_parser("raw", help="GET an authenticated JSON path")
    raw.add_argument("path")
    args = parser.parse_args()

    client = ZenTaoClient()
    client.login()
    result = client.get_bug(args.bug_id) if args.command == "get-bug" else client.get_json(args.path)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

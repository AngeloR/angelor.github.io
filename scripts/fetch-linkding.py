#!/usr/bin/env python3
import json
import os
import sys
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone


DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "linkding.json")


def read_existing():
    if not os.path.exists(DATA_PATH):
        return {"bookmarks": [], "last_sync": None}
    with open(DATA_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_data(payload):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def request_json(url, token):
    headers = {
        "Authorization": f"Token {token}",
        "User-Agent": "xangelo-linkding-sync/1.0",
        "Accept": "application/json",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        body = err.read().decode("utf-8", errors="replace")
        print(f"Request failed ({err.code}) for {url}")
        if body:
            print(body)
        raise


def normalize_url(base_url, value):
    if not value:
        return value
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return urllib.parse.urljoin(base_url, value)


def main():
    base_url = os.environ.get("LINKDING_BASE_URL")
    token = os.environ.get("LINKDING_TOKEN")
    limit = int(os.environ.get("LINKDING_LIMIT", "100"))

    if not base_url or not token:
        print("LINKDING_BASE_URL and LINKDING_TOKEN are required.")
        return 1

    base_url = base_url.rstrip("/")

    print(base_url)
    print(token)

    existing = read_existing()
    last_sync = existing.get("last_sync")
    existing_items = {item["id"]: item for item in existing.get("bookmarks", []) if "id" in item}

    params = {"limit": str(limit), "offset": "0"}
    if last_sync:
        params["added_since"] = last_sync

    fetched = 0
    while True:
        url = f"{base_url}/api/bookmarks/shared/?{urllib.parse.urlencode(params)}"
        payload = request_json(url, token)
        results = payload.get("results", [])
        if not results:
            break

        for item in results:
            normalized = {
                "id": item.get("id"),
                "url": item.get("url"),
                "title": item.get("title"),
                "description": item.get("description"),
                "notes": item.get("notes"),
                "tag_names": item.get("tag_names", []),
                "date_added": item.get("date_added"),
                "date_modified": item.get("date_modified"),
                "favicon_url": normalize_url(base_url, item.get("favicon_url")),
                "preview_image_url": normalize_url(base_url, item.get("preview_image_url")),
            }
            if normalized.get("id") is not None:
                existing_items[normalized["id"]] = normalized
            fetched += 1

        next_url = payload.get("next")
        if not next_url:
            break
        params["offset"] = str(int(params["offset"]) + limit)

    merged = sorted(
        existing_items.values(),
        key=lambda item: item.get("date_added") or "",
        reverse=True,
    )
    now = datetime.now(timezone.utc).isoformat()
    output = {
        "last_sync": now,
        "count": len(merged),
        "bookmarks": merged,
    }
    write_data(output)

    print(f"Fetched {fetched} bookmark(s). Total stored: {len(merged)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

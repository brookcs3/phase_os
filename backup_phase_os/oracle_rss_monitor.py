# Oracle RSS Monitor (Option 3)
# Fetches sample-relevant headlines and blog posts from curated sources

import feedparser
from datetime import datetime

FEEDS = [
    "https://www.factmag.com/feed/",
    "https://ra.co/rss/news",
    "https://www.whosampled.com/news/feed/",
    "https://www.tinymixtapes.com/feed",
    "https://www.xlr8r.com/feed"
]

DIGEST_FILE = "./oracle_rss_digest.md"


def fetch():
    entries = []
    for url in FEEDS:
        print(f"🌐 Fetching: {url}")
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            entries.append({
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "source": url
            })
    return entries


def write_digest(entries):
    stamp = datetime.now().strftime("%Y-%m-%d")
    with open(DIGEST_FILE, 'w') as f:
        f.write(f"# Oracle RSS Monitor — {stamp}\n\n")
        for e in entries:
            f.write(f"## {e['title']}\n🔗 {e['link']}\n📡 Source: {e['source']}\n\n")
    print(f"📰 RSS digest saved: {DIGEST_FILE}")

if __name__ == "__main__":
    items = fetch()
    write_digest(items)

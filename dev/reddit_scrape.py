"""
reddit_scrape.py — fetch a Reddit thread and save it as a .md file in dev/

Usage:
    python3 dev/reddit_scrape.py <reddit_url>

Example:
    python3 dev/reddit_scrape.py https://www.reddit.com/r/Homeschooling/comments/1rxz0v1/created_a_website_with_games_to_help_my_son_with/

Output:
    dev/reddit_<post_id>.md
"""

import json
import sys
import subprocess
from datetime import datetime


def fetch_thread(url):
    # Strip trailing slash, force .json
    url = url.rstrip("/")
    if not url.endswith(".json"):
        url += ".json"
    result = subprocess.run(
        ["curl", "-s", "-H",
         "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
         url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"curl failed: {result.stderr}")
    return json.loads(result.stdout)


def extract_comments(comments_data, depth=0):
    """Recursively extract comments and replies into a flat list of dicts."""
    results = []
    if not comments_data or comments_data.get("kind") != "Listing":
        return results
    for child in comments_data.get("data", {}).get("children", []):
        kind = child.get("kind")
        data = child.get("data", {})
        if kind == "t1":  # comment
            results.append({
                "depth": depth,
                "author": data.get("author", "[deleted]"),
                "score": data.get("score", 0),
                "body": data.get("body", ""),
            })
            # Recurse into replies
            replies = data.get("replies")
            if replies and isinstance(replies, dict):
                results.extend(extract_comments(replies, depth + 1))
        elif kind == "more":
            pass  # "load more comments" placeholders — skipped
    return results


def scrape(url):
    print(f"Fetching: {url}")
    thread = fetch_thread(url)

    post_data = thread[0]["data"]["children"][0]["data"]
    comments_data = thread[1]

    post_id = post_data.get("id", "unknown")
    title = post_data.get("title", "")
    author = post_data.get("author", "[deleted]")
    subreddit = post_data.get("subreddit", "")
    score = post_data.get("score", 0)
    selftext = post_data.get("selftext", "").strip()
    permalink = "https://www.reddit.com" + post_data.get("permalink", "")
    created = datetime.utcfromtimestamp(post_data.get("created_utc", 0)).strftime("%Y-%m-%d")

    comments = extract_comments(comments_data)

    # Build markdown
    lines = []
    lines.append(f"# Reddit Thread: {title}")
    lines.append(f"")
    lines.append(f"**Subreddit:** r/{subreddit}  ")
    lines.append(f"**Author:** u/{author}  ")
    lines.append(f"**Score:** {score}  ")
    lines.append(f"**Date:** {created}  ")
    lines.append(f"**URL:** {permalink}  ")
    lines.append(f"**Scraped:** {datetime.utcnow().strftime('%Y-%m-%d')}  ")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Original Post")
    lines.append(f"")
    lines.append(selftext if selftext else "*[No text body — link post or deleted]*")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Comments ({len(comments)} total)")
    lines.append(f"")

    for c in comments:
        indent = "  " * c["depth"]
        prefix = ">" * (c["depth"] + 1)  # markdown blockquote depth
        header = f"{indent}**u/{c['author']}** (score: {c['score']})"
        lines.append(header)
        # Indent each line of the body
        for body_line in c["body"].splitlines():
            lines.append(f"{indent}{body_line}")
        lines.append(f"")

    output = "\n".join(lines)

    outfile = f"dev/reddit_{post_id}.md"
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Saved: {outfile}")
    print(f"  {len(comments)} comments extracted")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dev/reddit_scrape.py <reddit_url>")
        sys.exit(1)
    scrape(sys.argv[1])

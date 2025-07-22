import feedparser
import os
import re
import frontmatter
from markdownify import markdownify as md
import html
from datetime import datetime
import requests
from urllib.parse import urlparse

RSS_URL = "https://medium.com/feed/@xangelo"
OUTPUT_DIR = "content/posts/medium"
EXISTING_SLUGS = {f[:-3] for f in os.listdir(OUTPUT_DIR) if f.endswith(".md")}

def slugify(title):
    return re.sub(r"[^\w-]", "", re.sub(r"\s+", "-", title.lower())).strip("-")

def resolve_medium_media_links(content):
    """
    Find Medium media links in the content and resolve them to direct GitHub Gist URLs if applicable.
    Medium media links look like: <https://medium.com/media/c7634bd7099d8b4a3c68e75789d29869/href>
    """
    # Pattern to match Medium media links
    medium_media_pattern = r'<(https://medium\.com/media/[a-f0-9]+/href)>'
    
    def replace_link(match):
        medium_url = match.group(1)
        try:
            # Follow the Medium media link to see where it redirects
            response = requests.get(medium_url, allow_redirects=True, timeout=10)
            final_url = response.url
            
            # Check if the final URL is a GitHub Gist
            parsed_url = urlparse(final_url)
            if parsed_url.netloc == 'gist.github.com':
                print(f"Resolved Medium media link: {medium_url} -> {final_url}")
                return f"<script src=\"{final_url}\"></script>"
            else:
                print(f"Medium media link does not resolve to GitHub Gist: {medium_url} -> {final_url}")
                return match.group(0)  # Return original if not a gist
                
        except requests.RequestException as e:
            print(f"Failed to resolve Medium media link {medium_url}: {e}")
            return match.group(0)  # Return original on error
    
    return re.sub(medium_media_pattern, replace_link, content)

feed = feedparser.parse(RSS_URL)

print(f"Parsing {RSS_URL}, {len(feed.entries)} posts")

for entry in feed.entries:
    slug = slugify(entry.title)
    if slug in EXISTING_SLUGS:
        continue

    content_html = entry.get("content", [{}])[0].get("value", "") or entry.get("summary", "")
    markdown_content = md(html.unescape(content_html))

    post = frontmatter.Post(markdown_content)
    post["title"] = entry.title
    post["date"] = entry.published
    post["slug"] = slug
    post["draft"] = False
    post["medium_link"] = entry.link

    # Resolve Medium media links to GitHub Gists
    post["content"] = resolve_medium_media_links(post["content"])

    # the last line of a post is a stat line that looks like this:
    # ![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=ca9ab4d5b529)
    # we should strip these out so that they don't count towards the viewer count on medium
    post["content"] = post["content"].replace("![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=ca9ab4d5b529)", "")

    # add a line to the bottom of the post to indicate that it's from Medium
    post["content"] += "\n\n---\n\nThis was originally published on Medium - " + entry.link

    output_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))

    print(f"Saved: {output_path}")
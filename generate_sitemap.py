import os
import glob
from datetime import datetime

BASE_URL = "https://skfurniture.com"
SITEMAP_FILE = "sitemap.xml"
ROBOTS_FILE = "robots.txt"

# Priority Map
PRIORITY = {
    "index.html": "1.0",
    "solutions.html": "0.9",
    "product": "0.8",  # Products in product/ directory
    "blog": "0.7",     # Blog posts in blog/ directory, and blog.html
    "other": "0.6"
}

def get_priority(filename, is_product=False, is_blog=False):
    if filename == "index.html":
        return PRIORITY["index.html"]
    if filename == "solutions.html":
        return PRIORITY["solutions.html"]
    if is_product:
        return PRIORITY["product"]
    if is_blog:
        return PRIORITY["blog"]
    return PRIORITY["other"]

def generate_sitemap():
    print(f"Generating {SITEMAP_FILE}...")

    pages = []

    # 1. Core HTML pages in root
    for filepath in glob.glob("*.html"):
        if filepath == "google9068598421008b8d.html": # skip verification file if any
            continue

        last_mod = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')
        priority = get_priority(filepath)
        if filepath == "blog.html":
            priority = PRIORITY["blog"]

        pages.append({
            "loc": f"{BASE_URL}/{filepath}",
            "lastmod": last_mod,
            "priority": priority
        })

    # 2. Product Pages
    if os.path.exists("product"):
        for filepath in glob.glob("product/*.html"):
            last_mod = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')
            pages.append({
                "loc": f"{BASE_URL}/{filepath}",
                "lastmod": last_mod,
                "priority": PRIORITY["product"]
            })

    # 3. Blog Posts
    if os.path.exists("blog"):
        for filepath in glob.glob("blog/*.html"):
            last_mod = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')
            pages.append({
                "loc": f"{BASE_URL}/{filepath}",
                "lastmod": last_mod,
                "priority": PRIORITY["blog"]
            })

    # Write XML
    with open(SITEMAP_FILE, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for page in pages:
            f.write('  <url>\n')
            f.write(f'    <loc>{page["loc"]}</loc>\n')
            f.write(f'    <lastmod>{page["lastmod"]}</lastmod>\n')
            f.write(f'    <priority>{page["priority"]}</priority>\n')
            f.write('  </url>\n')

        f.write('</urlset>')

    print(f"Sitemap generated with {len(pages)} URLs.")

def generate_robots():
    print(f"Generating {ROBOTS_FILE}...")
    content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/{SITEMAP_FILE}
"""
    with open(ROBOTS_FILE, "w") as f:
        f.write(content)
    print("robots.txt generated.")

if __name__ == "__main__":
    generate_sitemap()
    generate_robots()

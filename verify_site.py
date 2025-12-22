import os
from playwright.sync_api import sync_playwright

def verify_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to current directory
        cwd = os.getcwd()

        # Verify index.html
        print("Verifying index.html...")
        page.goto(f"file://{cwd}/index.html")
        page.screenshot(path="verify_index.png", full_page=True)

        # Verify blog.html
        print("Verifying blog.html...")
        page.goto(f"file://{cwd}/blog.html")
        page.screenshot(path="verify_blog.png", full_page=True)

        # Verify services.html
        print("Verifying services.html...")
        page.goto(f"file://{cwd}/services.html")
        page.screenshot(path="verify_services.png", full_page=True)

        # Verify dealer.html
        print("Verifying dealer.html...")
        page.goto(f"file://{cwd}/dealer.html")
        page.screenshot(path="verify_dealer.png", full_page=True)

        # Verify manufacturing.html
        print("Verifying manufacturing.html...")
        page.goto(f"file://{cwd}/manufacturing.html")
        page.screenshot(path="verify_manufacturing.png", full_page=True)

        # Verify product-detail.html
        print("Verifying product-detail.html...")
        page.goto(f"file://{cwd}/product-detail.html")
        page.screenshot(path="verify_product_detail.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_site()

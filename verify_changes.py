from playwright.sync_api import sync_playwright
import os

def verify_changes():
    cwd = os.getcwd()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Verify Home Page Name Change
        page.goto(f"file://{cwd}/index.html")
        page.screenshot(path="/home/jules/verification/index_page.png")
        print("Captured index.html")

        # Check Title
        title = page.title()
        if "skinterios" in title:
             print("PASS: Index title contains skinterios")
        else:
             print(f"FAIL: Index title is {title}")

        # Check Logo
        logo_text = page.locator(".logo").text_content()
        if "skinterios" in logo_text:
             print("PASS: Logo text contains skinterios")
        else:
             print(f"FAIL: Logo text is {logo_text}")

        # 2. Verify About Page Content
        page.goto(f"file://{cwd}/about.html")
        page.screenshot(path="/home/jules/verification/about_page.png")
        print("Captured about.html")

        # Check for specific text
        content = page.content()
        if "Sai Krupa Furniture & Fabrication Works" in content:
            print("PASS: About page contains 'Sai Krupa Furniture & Fabrication Works'")
        else:
            print("FAIL: About page missing company full name")

        # 3. Verify New Product Page (Whiteboard)
        page.goto(f"file://{cwd}/product/whiteboard.html")
        page.screenshot(path="/home/jules/verification/whiteboard_page.png")
        print("Captured product/whiteboard.html")

        # Check Title
        title = page.title()
        if "Whiteboard - skinterios" in title:
             print("PASS: Whiteboard title is correct")
        else:
             print(f"FAIL: Whiteboard title is {title}")

        # Check Image
        img_src = page.locator("#currentImage").get_attribute("src")
        if "whiteboard.jpg" in img_src:
             print("PASS: Whiteboard image source seems correct")
        else:
             print(f"FAIL: Whiteboard image source is {img_src}")

        browser.close()

if __name__ == "__main__":
    verify_changes()

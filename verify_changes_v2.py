from playwright.sync_api import sync_playwright
import os

def verify_changes():
    cwd = os.getcwd()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Verify Home Page Logo
        page.goto(f"file://{cwd}/index.html")
        page.screenshot(path="/home/jules/verification/index_logo.png")
        print("Captured index.html")

        # Check Logo Image
        logo_img = page.locator(".logo img")
        if logo_img.count() > 0:
            src = logo_img.get_attribute("src")
            if "logo.jpg" in src:
                print("PASS: Logo image found on Index")
            else:
                print(f"FAIL: Logo image src is {src}")
        else:
            print("FAIL: Logo image not found on Index")

        # 2. Verify Service Card Image
        # The first card in the services grid
        card_img = page.locator(".service-card.main-service img").first
        if card_img.count() > 0:
            src = card_img.get_attribute("src")
            if "classroom 2.jpg" in src or "desk-bench.png" not in src: # Checking change
                 print(f"PASS: Service card image updated to {src}")
            else:
                 print(f"FAIL: Service card image is still {src}")
        else:
            print("FAIL: Service card image not found")

        # 3. Verify Manufacturing Page UI
        page.goto(f"file://{cwd}/manufacturing.html")
        page.screenshot(path="/home/jules/verification/manufacturing_ui.png")
        print("Captured manufacturing.html")

        # Check for grid layout in timeline
        timeline = page.locator(".timeline-container")
        display = timeline.evaluate("element => getComputedStyle(element).display")
        if display == "grid":
             print("PASS: Timeline container is using grid layout")
        else:
             print(f"FAIL: Timeline container display is {display}")

        browser.close()

if __name__ == "__main__":
    verify_changes()

from playwright.sync_api import sync_playwright
import os

def verify_site():
    # Define the list of files to check
    files_to_check = [
        "index.html",
        "solutions.html",  # Renamed from products.html
        "manufacturing.html",
        "services.html",
        "projects.html",
        "blog.html",
        "inquiry.html",
        "product-detail.html"
    ]

    # Files that should NOT exist
    files_not_exist = ["dealer.html"]

    # Verify files exist/don't exist
    missing_files = []
    for f in files_to_check:
        if not os.path.exists(f):
            missing_files.append(f)

    for f in files_not_exist:
        if os.path.exists(f):
            print(f"ERROR: {f} should have been deleted.")

    if missing_files:
        print(f"Error: Missing files: {missing_files}")
        return

    print("All required HTML files found.")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Set viewport to desktop
        page.set_viewport_size({"width": 1280, "height": 800})

        for filename in files_to_check:
            print(f"Verifying {filename}...")
            # Use absolute path for file URL
            file_url = f"file://{os.path.abspath(filename)}"
            try:
                page.goto(file_url)
                # Take a screenshot
                screenshot_name = f"verify_{filename.replace('.html', '')}.png"
                page.screenshot(path=screenshot_name, full_page=True)
                print(f"Screenshot saved: {screenshot_name}")
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

        # Mobile View Verification (Home)
        print("Verifying Mobile View for index.html...")
        page.set_viewport_size({"width": 375, "height": 812}) # iPhone X
        page.goto(f"file://{os.path.abspath('index.html')}")
        page.screenshot(path="verify_mobile_index.png")
        print("Mobile screenshot saved.")

        browser.close()

if __name__ == "__main__":
    verify_site()

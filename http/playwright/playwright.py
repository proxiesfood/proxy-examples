# pip install playwright, then: playwright install chromium
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(proxy={
        "server": "http://proxies.proxiesfood.com:81",
        "username": "USERNAME",
        "password": "PASSWORD",
    })
    page = browser.new_page()
    page.goto("https://icanhazip.com")
    print(page.inner_text("body"))
    browser.close()

import sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def capture_screenshot(proxy_ip, proxy_port, username, password):
    options = Options()
    options.headless = True

    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy_ip)
    profile.set_preference("network.proxy.http_port", proxy_port)
    profile.set_preference("network.proxy.ssl", proxy_ip)
    profile.set_preference("network.proxy.ssl_port", proxy_port)
    profile.set_preference("network.proxy.autoconfig_url", "")
    profile.set_preference("network.proxy.no_proxies_on", "localhost, 127.0.0.1")

    # Set proxy authentication credentials
    profile.set_preference("network.proxy.username", username)
    profile.set_preference("network.proxy.password", password)

    profile.update_preferences()

    driver = webdriver.Firefox(options=options, firefox_profile=profile)
    driver.get("https://whatismyipaddress.com/")
    time.sleep(5)  # Allow time for the page to load

    driver.save_screenshot(f"/home/ubuntu/screenshots/screenshot_{proxy_ip.split('.')[-1]}.png")
    driver.quit()

if __name__ == "__main__":
    proxy_ip = f"172.18.0.{sys.argv[1]}"
    proxy_port = 3128
    username = "flash"
    password = "flash"

    capture_screenshot(proxy_ip, proxy_port, username, password)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

def capture_screenshot(index):
    options = Options()
    service = Service('/path/to/geckodriver')
    options.headless = True
    options.add_argument('--log-level=DEBUG')

    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", f"172.18.0.{index}")
    profile.set_preference("network.proxy.http_port", 3128)
    profile.set_preference("network.proxy.ssl", f"172.18.0.{index}")
    profile.set_preference("network.proxy.ssl_port", 3128)
    profile.update_preferences()

    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://whatismyipaddress.com/")
    time.sleep(5)  # Allow time for the page to load

    driver.save_screenshot(f"/home/ubuntu/screenshots/screenshot_{index}.png")
    driver.quit()

if __name__ == "__main__":
    import sys
    index = int(sys.argv[1])
    capture_screenshot(index)

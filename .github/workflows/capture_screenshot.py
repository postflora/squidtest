from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def capture_screenshot(index):
    options = Options()
    options.headless = True
    options.add_argument('--log-level=DEBUG')

    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", f"172.18.0.{index}")
    profile.set_preference("network.proxy.http_port", 3128)
    profile.set_preference("network.proxy.ssl", f"172.18.0.{index}")
    profile.set_preference("network.proxy.ssl_port", 3128)
    profile.update_preferences()

    # Using executable_path to specify GeckoDriver path
    driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path='/usr/local/bin/geckodriver')
    
    try:
        driver.get("https://whatismyipaddress.com/")
        time.sleep(5)  # Allow time for the page to load
        driver.save_screenshot(f"/home/ubuntu/screenshots/screenshot_{index}.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    import sys
    index = int(sys.argv[1])
    capture_screenshot(index)

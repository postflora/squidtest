from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import sys

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
    service = Service('/usr/local/bin/geckodriver')
    
    driver = webdriver.Firefox(service=service, options=options, firefox_profile=profile)
    
    try:
        # Set page load timeout to 30 seconds
        driver.set_page_load_timeout(30)

        driver.get("https://whatismyipaddress.com/")
        time.sleep(5)  # Allow time for the page to load
        driver.save_screenshot(f"/home/ubuntu/screenshots/screenshot_{index}.png")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python capture_screenshot.py <index>")
        sys.exit(1)
    
    index = int(sys.argv[1])
    capture_screenshot(index)

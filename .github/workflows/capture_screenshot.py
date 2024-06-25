from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import sys

def capture_screenshot(index):
    options = Options()
    options.headless = True
    options.add_argument('--log-level=DEBUG')

    # Assign unique proxy settings based on index
    proxy_host = f"172.18.0.{index}"
    proxy_port = 3128

    # Proxy configuration for Selenium
    proxy = f"{proxy_host}:{proxy_port}"
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL",
    }

    # Using executable_path to specify geckodriver path
    gecko_driver_path = '/usr/local/bin/geckodriver'  # Replace with your actual path
    driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options, capabilities=firefox_capabilities)
    
    try:
        # Set page load timeout to 60 seconds (adjust as needed)
        driver.set_page_load_timeout(60)

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

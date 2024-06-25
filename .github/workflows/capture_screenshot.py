from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import sys

def capture_screenshot(index, proxy_port):
    options = Options()
    options.headless = True
    options.add_argument('--log-level=DEBUG')

    # Proxy settings
    proxy_host = f"172.18.0.{index}"
    
    options.set_preference('network.proxy.type', 1)
    options.set_preference('network.proxy.http', proxy_host)
    options.set_preference('network.proxy.http_port', proxy_port)
    options.set_preference('network.proxy.ssl', proxy_host)
    options.set_preference('network.proxy.ssl_port', proxy_port)
    
    # Using executable_path to specify geckodriver path
    gecko_driver_path = '/usr/local/bin/geckodriver'
    driver = webdriver.Firefox(executable_path=gecko_driver_path, options=options)
    
    try:
        # Set page load timeout to 30 seconds
        driver.set_page_load_timeout(60)

        driver.get("https://whatismyipaddress.com/")
        time.sleep(5)  # Allow time for the page to load
        driver.save_screenshot(f"/home/ubuntu/screenshots/screenshot_{index}.png")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python capture_screenshot.py <index> <proxy_port>")
        sys.exit(1)
    
    index = int(sys.argv[1])
    proxy_port = int(sys.argv[2])
    capture_screenshot(index, proxy_port)

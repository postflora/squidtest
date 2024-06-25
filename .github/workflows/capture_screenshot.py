from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

def capture_screenshot(index):
    options = Options()
    options.headless = True
    options.add_argument('--log-level=DEBUG')

    # Proxy settings
    proxy_host = f"172.18.0.{index}"
    proxy_port = 3128
    options.add_argument(f'--proxy-server=http://{proxy_host}:{proxy_port}')

    # Using executable_path to specify ChromeDriver path
    chrome_driver_path = '/usr/local/bin/chromedriver'  # Replace with your actual path
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    
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

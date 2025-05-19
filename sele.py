from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Required for newer Selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set path to chromedriver.exe
chromedriver_path = 'F:\\chromedriver-win64\\chromedriver.exe'

# Configure Chrome options
driver_option = Options()
driver_option.add_argument("--incognito")  # Corrected formatting
driver_option.add_experimental_option("detach", True)

# Function to create a WebDriver instance
def create_webdriver():
    service = Service(chromedriver_path)  # Create a Service object
    return webdriver.Chrome(service=service, options=driver_option)  # Use 'service' instead of 'executable_path'

# To use Brave, make sure brave.exe exists at this path
driver_option.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# Create WebDriver
browser = create_webdriver()

# Test by opening a website
browser.get("https://github.com/collections/machine-learning ")
print(browser.title)

projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")
project_list = {}

for proj in projects:
    proj_name = proj.text  # Project name
    link = proj.find_elements(By.XPATH, ".//a")  # Use dot to search relative to current element
    if link:  # Make sure link exists
        proj_url = link[0].get_attribute('href')  # Get href
        project_list[proj_name] = proj_url
        print(f"Project Name: {proj_name}, URL: {proj_url}")
# Close the browser
# browser.quit()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create Chrome options object
options = Options()
options.add_experimental_option('detach',True)
# Initialize Chrome webdriver with options
browser = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

browser.get("https://elzero.org")

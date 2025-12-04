from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def getWorkHTML(USERNAME, PASSWORD):
    LOGIN_URL = "https://ess.skycitygroup.com/ESS/login.aspx?"

    username = USERNAME
    password = PASSWORD

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    # Start Chrome driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    # Load the login page
    driver.get(LOGIN_URL)

    # Find username & password fields and login
    driver.find_element(By.NAME, "ctl00$MainContent$txtUserName").send_keys(username)
    driver.find_element(By.NAME, "ctl00$MainContent$txtPassword").send_keys(password)
    driver.find_element(By.NAME, "ctl00$MainContent$cmdLogin").click()

    # Wait for JavaScript to load (adjust timing as needed)
    time.sleep(5)

    # Get the full page source
    page_source = driver.page_source

    driver.quit()
    return page_source

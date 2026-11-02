from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--start-maximized")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
)

wait = WebDriverWait(driver, 5)

try:
    # open the websit 
    driver.get("https://www.klikindomaret.com/")

    # wait for the category

    wait.until(
        EC.all_of(
            EC.element_to_be_clickable((By.NAME, "keyword"))
        )
    )

    # fill the category
    input_element = driver.find_element(By.NAME, "keyword").send_keys("Madu" + Keys.ENTER)
   
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Madu"))
    # )
    # # find category
    # link = driver.find_element(By.PARTIAL_LINK_TEXT, "Madu")
    # link.click()

    time.sleep(15)

finally:

    driver.quit()
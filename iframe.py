
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



scr_obj = Service("C:\drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=scr_obj)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame") # will switch the focus to packagelistFrame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

driver.switch_to.default_content()  # will switch back to main page
driver.implicitly_wait(10)

driver.switch_to.frame("classFrame")
#WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, "Help"))
driver.find_element(By.LINK_TEXT, "Help").click()

driver.close()

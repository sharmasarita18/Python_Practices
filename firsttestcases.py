
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

scr_obj = Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver= webdriver.Chrome(service=scr_obj)

#driver.get("https://phptravels.com/demo/")
driver.get("https://omayo.blogspot.com/")
#print(driver.title)
first_name_txt = driver.find_element(By.ID, "ta1")
first_name_txt.clear()
first_name_txt.send_keys("ABCDhhjjkkjkllkjlguddan.")
last_name_txt = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[3]/div[1]/textarea")
last_name_txt.clear()
last_name_txt.send_keys("Sharma")
#dropdown = driver.find_element(By.ID, "multiselect1")
if driver.find_element(By.ID, "multiselect1").get_attribute("multiple"):
    print("multiple select options can be chosen")
    select_fr = Select(driver.find_element(By.ID, "multiselect1"))
    input1 = len(select_fr.options)
    #print(input1)
    select_fr.select_by_index(1)
    select_fr.select_by_value("audix")


else:
    print("only one select option can be selected")

select_drop1 = Select(driver.find_element(By.ID, "drop1"))
select_drop1.select_by_visible_text("doc 2")
window_before = driver.window_handles[0]
driver.find_element(By.LINK_TEXT, "SeleniumTutorial").click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
#driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[12]/div[1]/button[2]").click()
print(f"Page title is {driver.title}")

driver.close()
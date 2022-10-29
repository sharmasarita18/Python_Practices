import imp
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service

opt = webdriver.ChromeOptions()
scr_obj = Service("chrome.exe")
driver = webdriver.Chrome(service=scr_obj, options=opt)
opt.add_argument("--disable_notifications")
 
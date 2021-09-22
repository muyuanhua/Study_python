from selenium import webdriver
import time
import logging


driver=webdriver.Chrome()
driver.get("http://one.heartdub.cn:8880/#/index")
# driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/a').click()
time.sleep(2)
# try:
driver.find_element_by_xpath('//*[@id="loginBox"]/div/div[1]/form/div[1]/div/div/input').send_keys('muyuanhua666@163.com')
driver.find_element_by_xpath('//*[@id="loginBox"]/div/div[1]/form/div[2]/div/div/input').send_keys('myh123')
driver.find_element_by_css_selector('button[class]').click()
driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/nav/ul/li[2]/a/div[2]').click()


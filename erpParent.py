from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import argparse
import sys
import itertools
from queue import Queue
import threading
import os

driver = webdriver.PhantomJS()
start_time = time.time()
try:
    driver.get("https://nucleus.niituniversity.in")
    emailFieldID = ".//*[@id='SchSel_txtUserName']"
    passFieldID = ".//*[@id='SchSel_txtPassword']"
    loginButtonXPath = ".//*[@id='SchSel_btnLogin']"
    #flLogoXpath = ".//*[@id='divUpper']/table/tbody/tr/td/table/tbody/tr[1]/td/u"
    emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailFieldID))
    passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passFieldID))
    loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))
    emailFieldElement.click()
    emailFieldElement.clear()
    emailFieldElement.send_keys("Enrolemnt Number")
    passFieldElement.click()
    passFieldElement.clear()
    passFieldElement.send_keys("Password")
    loginButtonElement.click()
    #WebDriverWait(driver, 15).until(lambda driver.url: "https://nucleus.niituniversity.in/WebApp/Index.aspx")
    time.sleep(0.5)
    driver.save_screenshot("erp_login.png")
    print("\n    Time Executed - " + str(time.time() - start_time))
    if driver.current_url == "https://nucleus.niituniversity.in/WebApp/Index.aspx":
        print("Login Succesfully!!")
    else:
        print("Login Failed!!")
except Exception as e:
    print(str(e))
    driver.save_screenshot("erp_error.png")
driver.quit()
# display.stop()

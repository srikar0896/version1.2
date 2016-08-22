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
#userId = "Email"
start_time = time.time()

driver.get("https://www.facebook.com")
fbUsername = "Mail Id"
emailFieldID = ".//*[@id='email']"
passFieldID = ".//*[@id='pass']"
loginButtonXPath = ".//input[@value='Log In']"
flLogoXpath = "(//a[contains(@href, 'logo')])[1]"
emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailFieldID))
passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passFieldID))
loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXPath))
emailFieldElement.click()
emailFieldElement.clear()
emailFieldElement.send_keys(fbUsername)
passFieldElement.click()
passFieldElement.clear()
passFieldElement.send_keys("Password")
loginButtonElement.click()
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(flLogoXpath))
driver.save_screenshot("yah.png")
print("\n    Time Executed - " + str(time.time() - start_time))

driver.quit()
# display.stop()
